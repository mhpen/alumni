# Use Node.js as base image
FROM node:18-slim AS client-builder

# Set working directory for client
WORKDIR /app/client

# Copy client package.json and package-lock.json
COPY client/package*.json ./

# Install client dependencies
RUN npm install

# Copy client source code
COPY client/ ./

# Build the client application
RUN npm run build

# Use Python as the base image for the final stage
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Install Node.js for the server
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy server package.json and package-lock.json
COPY server/package*.json ./server/

# Install server dependencies
WORKDIR /app/server
RUN npm install

# Copy server source code
COPY server/ ./

# Copy Python requirements
COPY server/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the built client from the client-builder stage
COPY --from=client-builder /app/client/build /app/client/build

# Set environment variables
ENV NODE_ENV=production
ENV PYTHON_VERSION=3.8.0
ENV PORT=5000

# Create directories for models if they don't exist
RUN mkdir -p /opt/models

# Copy model files if they exist
COPY employment_models /opt/models/ || true
COPY models /opt/models/ || true

# Expose the port
EXPOSE 5000

# Set the working directory back to the server directory
WORKDIR /app/server

# Start the combined application
CMD ["python", "combined_app.py"]
