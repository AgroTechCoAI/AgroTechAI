#!/usr/bin/env python3
"""
AgroTechAI WebSocket Performance Benchmark

Este script mide las métricas de rendimiento del sistema AgroTechAI:
- Latencia total de análisis (p50, p99, avg, min, max)
- Latencia por agente (ImageVision, AgriVision, SoilSense, CropMaster)
- Throughput (análisis por minuto)

Uso:
    python benchmark_websocket.py --image test_image.jpg --requests 10
    python benchmark_websocket.py --image test_image.jpg --requests 20 --host localhost --port 5000
"""

import asyncio
import websockets
import json
import base64
import time
import argparse
import statistics
from dataclasses import dataclass, field
from typing import Optional
from pathlib import Path


@dataclass
class AgentTiming:
    """Tiempos de cada agente en una request"""
    image_vision: float = 0.0
    agri_vision: float = 0.0
    soil_sense: float = 0.0
    crop_master: float = 0.0
    total: float = 0.0


@dataclass
class BenchmarkResult:
    """Resultados agregados del benchmark"""
    num_requests: int = 0
    successful: int = 0
    failed: int = 0
    timings: list = field(default_factory=list)
    errors: list = field(default_factory=list)
    wall_clock_ms: float = 0.0  # Tiempo total real (para throughput concurrente)


def load_image_as_base64(image_path: str) -> str:
    """Carga una imagen y la convierte a base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def calculate_percentile(data: list, percentile: float) -> float:
    """Calcula el percentil de una lista de valores"""
    if not data:
        return 0.0
    sorted_data = sorted(data)
    index = int(len(sorted_data) * percentile / 100)
    index = min(index, len(sorted_data) - 1)
    return sorted_data[index]


async def run_single_analysis(
    uri: str,
    image_b64: str,
    environment_description: str,
    request_id: int,
    verbose: bool = False
) -> tuple[Optional[AgentTiming], Optional[str]]:
    """
    Ejecuta un análisis completo y mide tiempos por agente.

    Returns:
        tuple: (AgentTiming o None, error_message o None)
    """
    timing = AgentTiming()

    try:
        async with websockets.connect(uri, ping_interval=None) as ws:
            # Enviar request de análisis
            start_total = time.perf_counter()
            agent_start = start_total

            message = {
                "type": "image_analysis",
                "image_data": image_b64,
                "environment_description": environment_description
            }

            await ws.send(json.dumps(message))

            if verbose:
                print(f"  [Request {request_id}] Enviado análisis...")

            # Recibir respuestas hasta completar
            current_agent = None
            completed_agents = set()

            while True:
                try:
                    response = await asyncio.wait_for(ws.recv(), timeout=120)
                    data = json.loads(response)
                    msg_type = data.get("type", "")

                    if msg_type == "status":
                        status_msg = data.get("message", "")

                        # Detectar inicio de agentes
                        if "ImageVision" in status_msg:
                            current_agent = "ImageVision"
                            agent_start = time.perf_counter()
                        elif "AgriVision" in status_msg or "SoilSense" in status_msg:
                            if "ImageVision" in completed_agents:
                                agent_start = time.perf_counter()
                        elif "CropMaster" in status_msg:
                            current_agent = "CropMaster"
                            agent_start = time.perf_counter()
                        elif "completado" in status_msg.lower():
                            timing.total = (time.perf_counter() - start_total) * 1000
                            break

                    elif msg_type == "agent_result":
                        agent_name = data.get("agent", "")
                        elapsed = (time.perf_counter() - agent_start) * 1000

                        if agent_name == "ImageVision":
                            timing.image_vision = elapsed
                            completed_agents.add("ImageVision")
                            agent_start = time.perf_counter()  # Reset para concurrent
                        elif agent_name == "AgriVision":
                            timing.agri_vision = elapsed
                            completed_agents.add("AgriVision")
                        elif agent_name == "SoilSense":
                            timing.soil_sense = elapsed
                            completed_agents.add("SoilSense")
                        elif agent_name == "CropMaster":
                            timing.crop_master = elapsed
                            completed_agents.add("CropMaster")

                        if verbose:
                            print(f"    [{agent_name}] {elapsed:.2f}ms")

                    elif msg_type == "error":
                        error_msg = data.get("message", "Unknown error")
                        return None, error_msg

                except asyncio.TimeoutError:
                    return None, "Timeout esperando respuesta (120s)"

            # Calcular total si no se capturó
            if timing.total == 0:
                timing.total = (time.perf_counter() - start_total) * 1000

            return timing, None

    except websockets.exceptions.ConnectionClosed as e:
        return None, f"Conexión cerrada: {e}"
    except Exception as e:
        return None, f"Error: {str(e)}"


async def run_benchmark(
    host: str,
    port: int,
    image_path: str,
    num_requests: int,
    environment_description: str,
    verbose: bool = False,
    concurrent: int = 1
) -> BenchmarkResult:
    """Ejecuta el benchmark completo"""

    uri = f"ws://{host}:{port}/ws"
    result = BenchmarkResult(num_requests=num_requests)

    mode = "CONCURRENTE" if concurrent > 1 else "SECUENCIAL"

    print(f"\n{'='*60}")
    print(f"AgroTechAI WebSocket Benchmark ({mode})")
    print(f"{'='*60}")
    print(f"Endpoint: {uri}")
    print(f"Imagen: {image_path}")
    print(f"Requests: {num_requests}")
    if concurrent > 1:
        print(f"Concurrencia: {concurrent} requests simultáneos")
    print(f"{'='*60}\n")

    # Cargar imagen
    try:
        image_b64 = load_image_as_base64(image_path)
        print(f"Imagen cargada: {len(image_b64)} bytes (base64)")
    except FileNotFoundError:
        print(f"ERROR: No se encontró la imagen: {image_path}")
        return result

    # Verificar conexión
    print(f"\nVerificando conexión a {uri}...")
    try:
        async with websockets.connect(uri, ping_interval=None) as ws:
            await ws.send(json.dumps({"type": "ping"}))
            response = await asyncio.wait_for(ws.recv(), timeout=10)
            data = json.loads(response)
            if data.get("type") == "pong":
                print("Conexión verificada OK\n")
            else:
                print(f"Respuesta inesperada: {data}")
    except Exception as e:
        print(f"ERROR: No se pudo conectar: {e}")
        return result

    # Ejecutar requests
    if concurrent > 1:
        # Modo concurrente
        print(f"Ejecutando {num_requests} análisis con concurrencia {concurrent}...\n")
        result = await run_concurrent_benchmark(
            uri, image_b64, environment_description, num_requests, concurrent, verbose
        )
    else:
        # Modo secuencial (original)
        print(f"Ejecutando {num_requests} análisis secuencialmente...\n")

        for i in range(num_requests):
            print(f"Request {i+1}/{num_requests}...")

            timing, error = await run_single_analysis(
                uri=uri,
                image_b64=image_b64,
                environment_description=environment_description,
                request_id=i+1,
                verbose=verbose
            )

            if error:
                result.failed += 1
                result.errors.append(error)
                print(f"  FAILED: {error}")
            else:
                result.successful += 1
                result.timings.append(timing)
                print(f"  OK: {timing.total:.2f}ms total")

            # Pequeña pausa entre requests para no saturar
            if i < num_requests - 1:
                await asyncio.sleep(0.5)

    return result


async def run_concurrent_benchmark(
    uri: str,
    image_b64: str,
    environment_description: str,
    num_requests: int,
    concurrent: int,
    verbose: bool
) -> BenchmarkResult:
    """Ejecuta requests de forma concurrente en batches"""
    result = BenchmarkResult(num_requests=num_requests)

    # Dividir en batches de tamaño 'concurrent'
    batches = [range(i, min(i + concurrent, num_requests))
               for i in range(0, num_requests, concurrent)]

    total_start = time.perf_counter()
    request_id = 0

    for batch_num, batch in enumerate(batches, 1):
        batch_size = len(list(batch))
        print(f"Batch {batch_num}/{len(batches)} ({batch_size} requests concurrentes)...")

        # Crear tareas concurrentes para este batch
        tasks = []
        for i in batch:
            request_id += 1
            task = run_single_analysis(
                uri=uri,
                image_b64=image_b64,
                environment_description=environment_description,
                request_id=request_id,
                verbose=verbose
            )
            tasks.append(task)

        # Ejecutar todas las tareas del batch concurrentemente
        batch_start = time.perf_counter()
        results = await asyncio.gather(*tasks, return_exceptions=True)
        batch_elapsed = (time.perf_counter() - batch_start) * 1000

        # Procesar resultados
        for i, res in enumerate(results):
            if isinstance(res, Exception):
                result.failed += 1
                result.errors.append(str(res))
                print(f"  Request {batch.start + i + 1}: FAILED - {res}")
            else:
                timing, error = res
                if error:
                    result.failed += 1
                    result.errors.append(error)
                    print(f"  Request {batch.start + i + 1}: FAILED - {error}")
                else:
                    result.successful += 1
                    result.timings.append(timing)
                    if verbose:
                        print(f"  Request {batch.start + i + 1}: OK - {timing.total:.2f}ms")

        print(f"  Batch completado en {batch_elapsed:.2f}ms")

        # Pequeña pausa entre batches
        if batch_num < len(batches):
            await asyncio.sleep(0.5)

    total_elapsed = (time.perf_counter() - total_start) * 1000
    print(f"\nTiempo total wall-clock: {total_elapsed:.2f}ms ({total_elapsed/1000:.2f}s)")

    # Agregar métrica de wall-clock time para throughput real
    result.wall_clock_ms = total_elapsed

    return result


def print_results(result: BenchmarkResult, ctq_latency_ms: float = 5000):
    """Imprime los resultados del benchmark"""

    print(f"\n{'='*60}")
    print(f"RESULTADOS DEL BENCHMARK")
    print(f"{'='*60}\n")

    print(f"Requests totales: {result.num_requests}")
    print(f"Exitosos: {result.successful}")
    print(f"Fallidos: {result.failed}")
    print(f"Tasa de éxito: {(result.successful/result.num_requests)*100:.1f}%")

    if not result.timings:
        print("\nNo hay datos de timing para analizar.")
        return

    # Extraer métricas
    totals = [t.total for t in result.timings]
    image_vision = [t.image_vision for t in result.timings if t.image_vision > 0]
    agri_vision = [t.agri_vision for t in result.timings if t.agri_vision > 0]
    soil_sense = [t.soil_sense for t in result.timings if t.soil_sense > 0]
    crop_master = [t.crop_master for t in result.timings if t.crop_master > 0]

    print(f"\n--- Latencia Total (ms) ---")
    print(f"  p50:  {calculate_percentile(totals, 50):.2f}")
    print(f"  p90:  {calculate_percentile(totals, 90):.2f}")
    print(f"  p99:  {calculate_percentile(totals, 99):.2f}")
    print(f"  avg:  {statistics.mean(totals):.2f}")
    print(f"  min:  {min(totals):.2f}")
    print(f"  max:  {max(totals):.2f}")
    if len(totals) > 1:
        print(f"  std:  {statistics.stdev(totals):.2f}")

    print(f"\n--- Latencia por Agente (ms) - Promedios ---")
    if image_vision:
        print(f"  ImageVision:  {statistics.mean(image_vision):.2f} (p99: {calculate_percentile(image_vision, 99):.2f})")
    if agri_vision:
        print(f"  AgriVision:   {statistics.mean(agri_vision):.2f} (p99: {calculate_percentile(agri_vision, 99):.2f})")
    if soil_sense:
        print(f"  SoilSense:    {statistics.mean(soil_sense):.2f} (p99: {calculate_percentile(soil_sense, 99):.2f})")
    if crop_master:
        print(f"  CropMaster:   {statistics.mean(crop_master):.2f} (p99: {calculate_percentile(crop_master, 99):.2f})")

    # Validación CTQ
    p99_total = calculate_percentile(totals, 99)
    ctq_pass = p99_total < ctq_latency_ms

    print(f"\n--- Validación CTQ ---")
    print(f"  Objetivo:  p99 < {ctq_latency_ms}ms")
    print(f"  Resultado: p99 = {p99_total:.2f}ms")
    print(f"  Estado:    {'CUMPLE' if ctq_pass else 'NO CUMPLE'}")

    # Throughput
    if result.wall_clock_ms > 0:
        # Modo concurrente: usar wall-clock time real
        wall_clock_seconds = result.wall_clock_ms / 1000
        throughput_real = result.successful / wall_clock_seconds if wall_clock_seconds > 0 else 0
        print(f"\n--- Throughput (Concurrente) ---")
        print(f"  Tiempo wall-clock: {result.wall_clock_ms:.2f}ms ({wall_clock_seconds:.2f}s)")
        print(f"  Análisis/segundo:  {throughput_real:.2f}")
        print(f"  Análisis/minuto:   {throughput_real * 60:.2f}")
    else:
        # Modo secuencial: suma de tiempos individuales
        total_time_seconds = sum(totals) / 1000
        throughput = result.successful / total_time_seconds if total_time_seconds > 0 else 0
        print(f"\n--- Throughput (Secuencial) ---")
        print(f"  Análisis/segundo: {throughput:.2f}")
        print(f"  Análisis/minuto:  {throughput * 60:.2f}")

    if result.errors:
        print(f"\n--- Errores ({len(result.errors)}) ---")
        for i, error in enumerate(result.errors[:5]):  # Mostrar máx 5
            print(f"  {i+1}. {error}")
        if len(result.errors) > 5:
            print(f"  ... y {len(result.errors) - 5} más")

    print(f"\n{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description="AgroTechAI WebSocket Performance Benchmark",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python benchmark_websocket.py --image cultivo.jpg --requests 10
  python benchmark_websocket.py --image cultivo.jpg --requests 20 --verbose
  python benchmark_websocket.py --image cultivo.jpg --requests 5 --host 192.168.1.100 --port 8000
        """
    )

    parser.add_argument(
        "--image", "-i",
        required=True,
        help="Ruta a la imagen de prueba (JPG, PNG)"
    )

    parser.add_argument(
        "--requests", "-n",
        type=int,
        default=10,
        help="Número de requests a ejecutar (default: 10)"
    )

    parser.add_argument(
        "--host",
        default="localhost",
        help="Host del servidor WebSocket (default: localhost)"
    )

    parser.add_argument(
        "--port", "-p",
        type=int,
        default=5000,
        help="Puerto del servidor WebSocket (default: 5000)"
    )

    parser.add_argument(
        "--environment", "-e",
        default="Humedad del suelo 65%, Temperatura 23°C, pH 6.7, condiciones normales",
        help="Descripción del ambiente para el análisis"
    )

    parser.add_argument(
        "--ctq",
        type=float,
        default=5000,
        help="Objetivo CTQ de latencia p99 en ms (default: 5000)"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Mostrar detalles de cada agente"
    )

    parser.add_argument(
        "--concurrent", "-c",
        type=int,
        default=1,
        help="Número de requests concurrentes (default: 1 = secuencial)"
    )

    args = parser.parse_args()

    # Verificar que la imagen existe
    if not Path(args.image).exists():
        print(f"ERROR: La imagen '{args.image}' no existe")
        return 1

    # Ejecutar benchmark
    result = asyncio.run(run_benchmark(
        host=args.host,
        port=args.port,
        image_path=args.image,
        num_requests=args.requests,
        environment_description=args.environment,
        verbose=args.verbose,
        concurrent=args.concurrent
    ))

    # Mostrar resultados
    print_results(result, ctq_latency_ms=args.ctq)

    return 0 if result.failed == 0 else 1


if __name__ == "__main__":
    exit(main())

