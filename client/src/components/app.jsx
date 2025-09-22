/* eslint-disable react-hooks/exhaustive-deps */
// App.jsx
import React, { useState, useEffect, useCallback, useRef } from 'react';
import ScenarioForm from './ScenarioForm.jsx';
import {
    createWebSocketConnection,
    sendAnalysisRequest,
    sendHeartbeat,
    calculateReconnectDelay,
    parseWebSocketMessage,
    isWebSocketReady
} from '../utils/websocket-utils.js';
import { getWebSocketUrl } from '../utils/websocket-config.js';
import '~/styles.css';

function App() {
    // WebSocket URL configuration - supports both local dev and Docker deployment
    const wsUrl = getWebSocketUrl();

    const [agentData, setAgentData] = useState({
        ImageVision: null,
        AgriVision: null,
        SoilSense: null,
        CropMaster: null
    });

    const [isAnalyzing, setIsAnalyzing] = useState(false);
    const [ws, setWs] = useState(null);

    // Enhanced connection state management
    const [connectionState, setConnectionState] = useState({
        isConnected: false,
        isReconnecting: false,
        attempts: 0,
        lastError: null,
        status: 'connecting' // 'connecting', 'connected', 'disconnected', 'reconnecting', 'failed'
    });

    // Configuration constants
    const maxReconnectAttempts = 5;
    const wsRef = useRef(null);
    const reconnectTimeoutRef = useRef(null);
    const heartbeatIntervalRef = useRef(null);

    // Enhanced WebSocket connection function with reconnection logic
    const connectWebSocket = useCallback((wsUrl) => {
        // Skip if already connected
        if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
            console.log('🔌 WebSocket already connected, skipping');
            return;
        }

        // Clear any pending reconnection attempts
        if (reconnectTimeoutRef.current) {
            clearTimeout(reconnectTimeoutRef.current);
        }

        console.log(`🔌 Attempting WebSocket connection to ${wsUrl} (attempt ${connectionState.attempts + 1})`);

        setConnectionState(prev => ({
            ...prev,
            status: prev.attempts === 0 ? 'connecting' : 'reconnecting',
            isReconnecting: prev.attempts > 0
        }));

        const websocket = createWebSocketConnection(wsUrl, {
            onOpen: () => {
                console.log('✅ WebSocket connected successfully');
                setConnectionState({
                    isConnected: true,
                    isReconnecting: false,
                    attempts: 0,
                    lastError: null,
                    status: 'connected'
                });
                setWs(websocket);

                // Start heartbeat
                startHeartbeat(websocket);
            },

            onMessage: (event) => {
                const message = parseWebSocketMessage(event.data);
                if (!message) {
                    setConnectionState(prev => ({
                        ...prev,
                        lastError: 'Failed to parse server message'
                    }));
                    return;
                }

                console.log('📨 Received message:', message);

                // Handle different message types
                switch (message.type) {
                    case 'agent_result':
                        setAgentData(prev => ({
                            ...prev,
                            [message.agent]: message.data
                        }));
                        break;

                    case 'status':
                        if (message.message.includes('completado')) {
                            setIsAnalyzing(false);
                        }
                        break;

                    case 'pong':
                        // Heartbeat response - connection is alive
                        console.log('💓 Heartbeat received');
                        break;

                    case 'error':
                        console.error('❌ Server error:', message.message);
                        setConnectionState(prev => ({
                            ...prev,
                            lastError: message.message
                        }));
                        break;

                    default:
                        console.log('❓ Unknown message type:', message.type);
                }
            },

            onError: (error) => {
                console.error('❌ WebSocket error:', error);
                setConnectionState(prev => ({
                    ...prev,
                    lastError: 'Connection error occurred',
                    status: 'disconnected'
                }));
            },

            onClose: (event) => {
                console.log(`🔌 WebSocket connection closed (code: ${event.code}, reason: ${event.reason})`);

                // Stop heartbeat
                stopHeartbeat();

                setConnectionState(prev => {
                    const newState = {
                        ...prev,
                        isConnected: false,
                        status: 'disconnected'
                    };

                    // Attempt reconnection if not manually closed and under attempt limit
                    if (event.code !== 1000 && prev.attempts < maxReconnectAttempts) {
                        const delay = calculateReconnectDelay(prev.attempts);
                        console.log(`🔄 Reconnecting in ${delay}ms (attempt ${prev.attempts + 1}/${maxReconnectAttempts})`);

                        reconnectTimeoutRef.current = setTimeout(() => {
                            setConnectionState(currentState => ({
                                ...currentState,
                                attempts: currentState.attempts + 1
                            }));
                        }, delay);

                        newState.status = 'reconnecting';
                        newState.isReconnecting = true;
                    } else if (prev.attempts >= maxReconnectAttempts) {
                        console.error('❌ Max reconnection attempts reached');
                        newState.status = 'failed';
                        newState.lastError = 'Maximum reconnection attempts exceeded';
                    }

                    return newState;
                });

                setWs(null);
            }
        });

        wsRef.current = websocket;

    }, [connectionState.attempts]);

    // Heartbeat mechanism to keep connection alive
    const startHeartbeat = (websocket) => {
        heartbeatIntervalRef.current = setInterval(() => {
            if (sendHeartbeat(websocket)) {
                console.log('💓 Heartbeat sent');
            }
        }, 4000); // Send ping every 4 seconds
    };

    const stopHeartbeat = () => {
        if (heartbeatIntervalRef.current) {
            clearInterval(heartbeatIntervalRef.current);
            heartbeatIntervalRef.current = null;
        }
    };

    // Initialize connection on component mount
    useEffect(() => {
        connectWebSocket(wsUrl);

        // Cleanup on unmount
        return () => {
            console.log('🧹 Cleaning up WebSocket connection');
            stopHeartbeat();
            if (reconnectTimeoutRef.current) {
                clearTimeout(reconnectTimeoutRef.current);
            }
            if (wsRef.current) {
                wsRef.current.close(1000, 'Component unmounting');
            }
        };
    }, [wsUrl]);

    // Trigger reconnection when attempts change
    useEffect(() => {
        if (connectionState.attempts > 0 && connectionState.attempts <= maxReconnectAttempts) {
            connectWebSocket(wsUrl);
        }
    }, [wsUrl, connectionState.attempts]);

    const handleCustomScenario = (imageBase64, environmentDescription) => {
        if (isWebSocketReady(ws)) {
            setIsAnalyzing(true);
            setAgentData({
                ImageVision: null,
                AgriVision: null,
                SoilSense: null,
                CropMaster: null
            });

            const success = sendAnalysisRequest(ws, imageBase64, environmentDescription);
            if (!success) {
                console.warn('⚠️ Failed to send analysis request');
                setConnectionState(prev => ({
                    ...prev,
                    lastError: 'Failed to send analysis request'
                }));
            }
        } else {
            console.warn('⚠️ Cannot send message: WebSocket not connected');
            setConnectionState(prev => ({
                ...prev,
                lastError: 'Cannot send request: No active connection'
            }));
        }
    };

    // Manual reconnection function
    const handleManualReconnect = () => {
        console.log('🔄 Manual reconnection triggered');
        setConnectionState(prev => ({
            ...prev,
            attempts: 0,
            lastError: null,
            status: 'connecting'
        }));
        connectWebSocket(wsUrl);
    };

    return (
        <div className="min-h-screen bg-green-50 p-8">
            <h1 className="text-4xl font-bold text-center mb-8 text-green-800">
                🌱 AgroTech AI Agents Demo
            </h1>

            {/* Connection Status Banner */}
            <ConnectionStatusBanner
                connectionState={connectionState}
                onReconnect={handleManualReconnect}
            />

            {/* Custom Scenario Form */}
            <ScenarioForm
                onSubmit={handleCustomScenario}
                isConnected={connectionState.isConnected}
                isAnalyzing={isAnalyzing}
            />

            {/* AI Agents Dashboard */}
            <div className="space-y-6 mb-8">
                {/* Row 1: ImageVision Agent (Full Width) */}
                <div className="w-full">
                    <AgentCard
                        title="📸 ImageVision"
                        data={agentData.ImageVision}
                        color="purple"
                    />
                </div>

                {/* Row 2: AgriVision and SoilSense Agents (Side by Side, Full Width) */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <AgentCard
                        title="🔍 AgriVision"
                        data={agentData.AgriVision}
                        color="blue"
                    />
                    <AgentCard
                        title="🌍 SoilSense"
                        data={agentData.SoilSense}
                        color="brown"
                    />
                </div>

                {/* Row 3: CropMaster Agent (Full Width) */}
                <div className="w-full">
                    <AgentCard
                        title="🧠 CropMaster"
                        data={agentData.CropMaster}
                        color="green"
                    />
                </div>
            </div>

            {/* Panel de Decisión Final */}
            <DecisionPanel data={agentData.CropMaster} />
        </div>
    );
}

function ConnectionStatusBanner({ connectionState, onReconnect }) {
    const { status, isReconnecting, attempts, lastError } = connectionState;

    const getStatusConfig = () => {
        switch (status) {
            case 'connected':
                return {
                    bgColor: 'bg-green-100',
                    textColor: 'text-green-800',
                    borderColor: 'border-green-500',
                    icon: '✅',
                    message: 'Conectado al servidor'
                };
            case 'connecting':
                return {
                    bgColor: 'bg-blue-100',
                    textColor: 'text-blue-800',
                    borderColor: 'border-blue-500',
                    icon: '🔄',
                    message: 'Conectando al servidor...'
                };
            case 'reconnecting':
                return {
                    bgColor: 'bg-yellow-100',
                    textColor: 'text-yellow-800',
                    borderColor: 'border-yellow-500',
                    icon: '🔄',
                    message: `Reconectando... (intento ${attempts}/5)`
                };
            case 'disconnected':
                return {
                    bgColor: 'bg-gray-100',
                    textColor: 'text-gray-800',
                    borderColor: 'border-gray-500',
                    icon: '⚪',
                    message: 'Desconectado del servidor'
                };
            case 'failed':
                return {
                    bgColor: 'bg-red-100',
                    textColor: 'text-red-800',
                    borderColor: 'border-red-500',
                    icon: '❌',
                    message: 'Error de conexión'
                };
            default:
                return {
                    bgColor: 'bg-gray-100',
                    textColor: 'text-gray-800',
                    borderColor: 'border-gray-500',
                    icon: '❓',
                    message: 'Estado desconocido'
                };
        }
    };

    const config = getStatusConfig();

    // Only show banner if not connected or if there's an error
    if (status === 'connected' && !lastError) {
        return null;
    }

    return (
        <div className={`${config.bgColor} ${config.textColor} border-l-4 ${config.borderColor} p-4 mb-6 rounded-lg`}>
            <div className="flex items-center justify-between">
                <div className="flex items-center space-x-3">
                    <span className="text-lg">{config.icon}</span>
                    <div>
                        <p className="font-medium">{config.message}</p>
                        {lastError && (
                            <p className="text-sm opacity-75">Error: {lastError}</p>
                        )}
                        {isReconnecting && (
                            <p className="text-sm opacity-75">El sistema intentará reconectar automáticamente...</p>
                        )}
                    </div>
                </div>

                {(status === 'failed' || status === 'disconnected') && (
                    <button
                        onClick={onReconnect}
                        className="px-4 py-2 bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 text-sm font-medium"
                    >
                        🔄 Reconectar
                    </button>
                )}
            </div>
        </div>
    );
}

// A helper function to render values more intelligently
const renderValue = (value) => {
    if (typeof value === 'boolean') {
        return (
            <span
                className={`px-2 py-1 text-xs font-semibold rounded-full ${value ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'
                    }`}
            >
                {value ? 'Yes' : 'No'}
            </span>
        );
    }

    if (Array.isArray(value)) {
        return value.join(', ');
    }

    if (typeof value === 'object' && value !== null) {
        return <pre className="text-xs bg-gray-50 p-2 rounded">{JSON.stringify(value, null, 2)}</pre>;
    }

    // Convert numbers and other primitives to a string
    return String(value);
};

// IMPORTANT: A mapping for Tailwind's JIT compiler to find the classes
const colorVariants = {
    blue: 'border-blue-500',
    green: 'border-green-500',
    red: 'border-red-500',
    yellow: 'border-yellow-500',
    purple: 'border-purple-500',
    // Add any other colors you plan to use
};

function AgentCard({ title, data, color = 'blue' }) {
    return (
        <div className={`bg-white rounded-lg shadow-lg p-6 border-l-4 ${colorVariants[color] || colorVariants.blue}`}>
            <h3 className="text-xl font-semibold text-gray-800 mb-4 pb-2 border-b">{title}</h3>
            {data ? (
                // Use CSS Grid for a clean, two-column layout
                <div className="grid grid-cols-[max-content,1fr] gap-x-4 gap-y-3">
                    {Object.entries(data).map(([key, value]) => (
                        // Use a React Fragment for each row to avoid adding extra divs to the DOM
                        <React.Fragment key={key}>
                            <span className="text-gray-500 font-medium text-right capitalize">
                                {key.replace(/_/g, ' ')}:
                            </span>
                            <span className="text-gray-900 font-medium break-words">
                                {renderValue(value)}
                            </span>
                        </React.Fragment>
                    ))}
                </div>
            ) : (
                // An improved "skeleton" loading state
                <div className="space-y-4 animate-pulse">
                    <div className="h-4 bg-gray-200 rounded w-3/4"></div>
                    <div className="h-4 bg-gray-200 rounded w-1/2"></div>
                    <div className="h-4 bg-gray-200 rounded w-5/6"></div>
                </div>
            )}
        </div>
    );
}


function DecisionPanel({ data }) {
    if (!data) return null;

    const statusColors = {
        excellent: 'bg-green-100 text-green-800',
        good: 'bg-blue-100 text-blue-800',
        warning: 'bg-yellow-100 text-yellow-800',
        critical: 'bg-red-100 text-red-800'
    };

    return (
        <div className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold mb-6 text-center">📊 Decisión Final del Sistema</h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <h3 className="text-lg font-semibold mb-3">Estado General</h3>
                    <span className={`px-4 py-2 rounded-full ${statusColors[data.overall_status]}`}>
                        {data.overall_status?.toUpperCase()}
                    </span>
                </div>

                <div>
                    <h3 className="text-lg font-semibold mb-3">Acciones Prioritarias</h3>
                    <ul className="list-disc list-inside space-y-1">
                        {data.priority_actions?.map((action, index) => (
                            <li key={index} className="text-gray-700">{action}</li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default App;