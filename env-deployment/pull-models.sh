#!/bin/sh
# Script to pull Ollama models based on environment variables

# Default model if none specified
DEFAULT_MODELS="gemma3:270m"

# Get models from environment variable or use default
MODELS="${OLLAMA_MODELS:-$DEFAULT_MODELS}"

echo "🤖 Starting Ollama model management..."
echo "📋 Models to pull: $MODELS"

# Use existing Ollama server managed by supervisor
echo "🚀 Connecting to existing Ollama server..."

# Wait for Ollama to be ready
echo "⏳ Waiting for Ollama server to be ready..."
for i in $(seq 1 30); do
    if curl -s http://localhost:11434/api/tags >/dev/null 2>&1; then
        echo "✅ Ollama server is ready!"
        break
    fi
    echo "⏳ Attempt $i/30: Ollama not ready yet, waiting..."
    sleep 2
done

# Check if Ollama is ready
if ! curl -s http://localhost:11434/api/tags >/dev/null 2>&1; then
    echo "❌ Ollama server is not available"
    exit 1
fi

# Pull each model (comma-separated list support)
echo "📥 Pulling models..."
for model in $(echo $MODELS | tr ',' ' '); do
    model=$(echo $model | xargs)  # trim whitespace
    if [ -n "$model" ]; then
        echo "📦 Pulling model: $model"
        if /usr/bin/ollama pull "$model"; then
            echo "✅ Successfully pulled: $model"
        else
            echo "❌ Failed to pull: $model"
        fi
    fi
done

echo "🎉 Model pulling complete!"
