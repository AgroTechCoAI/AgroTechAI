# Development build for Vite dev server
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies (including dev dependencies)
RUN npm ci --silent

# Copy source code
COPY . .

# Expose port 5173 (default Vite dev server port)
EXPOSE 5173 3000

# Start Vite dev server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]
