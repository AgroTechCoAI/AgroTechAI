# Multi-stage build for React frontend
FROM node:22-alpine AS frontend-builder

# Set working directory for frontend build
WORKDIR /app/client

# Copy package files for frontend
COPY client/package*.json ./

# Install frontend dependencies
RUN npm ci --silent

# Copy frontend source code
COPY client/ ./

# Build the frontend application (no environment variables needed)
RUN npm run build

# Python backend stage - Build binary with PyInstaller (Alpine-based)
FROM python:3.12-alpine AS backend-builder

# Install system dependencies needed for PyInstaller on Alpine
RUN apk add --no-cache \
    binutils \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

# Set working directory for backend
WORKDIR /app/server

# Copy backend source code
COPY server/ ./

# Install dependencies and PyInstaller
RUN pip install --no-cache-dir -e . && \
    pip install --no-cache-dir pyinstaller

# Create binary executable
RUN pyinstaller --onefile --name agrotech-server \
    --hidden-import uvicorn \
    --hidden-import uvicorn.lifespan.on \
    --hidden-import uvicorn.lifespan.off \
    --hidden-import uvicorn.protocols.websockets.auto \
    --hidden-import uvicorn.protocols.http.auto \
    --hidden-import fastapi \
    --collect-all uvicorn \
    main.py

# Final production stage - Alpine with Nginx (no Python needed!)
FROM nginx:alpine

# Install only supervisor and curl (much smaller!)
RUN apk add --no-cache \
    supervisor \
    curl

# Create necessary directories
RUN mkdir -p /var/log/supervisor \
    && mkdir -p /app/server

# Copy the compiled binary from backend builder
COPY --from=backend-builder /app/server/dist/agrotech-server /usr/local/bin/agrotech-server

# Make binary executable
RUN chmod +x /usr/local/bin/agrotech-server

# Copy frontend build to nginx html directory
COPY --from=frontend-builder /app/client/dist /usr/share/nginx/html

# Copy configuration files
COPY env-deployment/nginx.conf /etc/nginx/nginx.conf
COPY env-deployment/supervisord.conf /etc/supervisor/supervisord.conf

# Set working directory for the application
WORKDIR /app/server

# Create a health check script
RUN echo '#!/bin/sh\ncurl -f http://localhost/health || exit 1' > /usr/local/bin/healthcheck.sh \
    && chmod +x /usr/local/bin/healthcheck.sh

# Expose port 80 (nginx)
EXPOSE 80

# Add health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD /usr/local/bin/healthcheck.sh

# Start supervisor to manage both nginx and FastAPI
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
