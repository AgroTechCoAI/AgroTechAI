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

## Remove env for vite
RUN rm .env

# Build the frontend application (no environment variables needed)
RUN npm run build

# Skip building binary - we'll install Python directly in final stage

# Final production stage - Start with Ollama base image
FROM alpine/ollama:latest

# Install nginx, supervisor, curl, and Python for Wolfi
RUN apk add --no-cache \
    nginx \
    supervisor \
    curl \
    python3 \
    py3-pip \
    && adduser -D -s /bin/false -H -h /var/cache/nginx nginx

# Create necessary directories
RUN mkdir -p /var/log/supervisor \
    && mkdir -p /app/server \
    && mkdir -p /var/run \
    && mkdir -p /var/log/nginx \
    && mkdir -p /usr/share/nginx/html \
    && mkdir -p /usr/local/bin/

# Models will be pulled dynamically at runtime via environment variables

# Copy backend source code
COPY server/ /app/server/

# Install Python dependencies directly (avoiding pyproject.toml setup issues)
WORKDIR /app/server
RUN pip install --no-cache-dir \
    fastapi==0.116.1 \
    uvicorn[standard]==0.35.0 \
    requests==2.31.0 \
    websockets==12.0 \
    urllib3==2.1.0 \
    && pip install --no-cache-dir --only-binary=all Pillow==10.1.0 || \
    pip install --no-cache-dir Pillow

# Copy frontend build to nginx html directory
COPY --from=frontend-builder /app/client/dist /usr/share/nginx/html

# Copy configuration files
COPY env-deployment/nginx.conf /etc/nginx/nginx.conf
COPY env-deployment/supervisord.conf /etc/supervisor/supervisord.conf

# Copy and make executable the model pulling script
COPY env-deployment/pull-models.sh /usr/local/bin/pull-models.sh
RUN chmod +x /usr/local/bin/pull-models.sh

# Set working directory for the application
WORKDIR /app/server

# Create a health check script that checks nginx, backend, and ollama
RUN echo '#!/bin/sh\ncurl -f http://localhost/health && curl -f http://localhost:11434/api/tags || exit 1' > /usr/local/bin/healthcheck.sh \
    && chmod +x /usr/local/bin/healthcheck.sh

# Expose ports (nginx and ollama)
EXPOSE 80 11434

# Add health check that checks both nginx and ollama
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD /usr/local/bin/healthcheck.sh

# Override the ollama entrypoint and start supervisor to manage nginx, FastAPI, and Ollama
ENTRYPOINT []
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
