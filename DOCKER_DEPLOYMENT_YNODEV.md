# Docker Deployment Guide for Alumni Management System

This guide explains how to deploy the Alumni Management System using Docker with the Docker Hub username "ynodev".

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system
- [Docker Compose](https://docs.docker.com/compose/install/) installed on your system
- Docker Hub account (username: ynodev)

## Deployment Options

### Option 1: Deploy Locally (Build Images Locally)

Run the deployment script:

```bash
# On Windows
deploy.bat

# On Linux/Mac
chmod +x deploy.sh
./deploy.sh
```

This command will:
- Build the Docker images for both the client and server locally
- Start the containers in detached mode

### Option 2: Push Images to Docker Hub

If you want to push the images to Docker Hub:

1. Make sure you're logged in to Docker Hub:
   ```bash
   docker login -u ynodev
   ```

2. Run the push script:
   ```bash
   # On Windows
   push-to-dockerhub.bat

   # On Linux/Mac
   chmod +x push-to-dockerhub.sh
   ./push-to-dockerhub.sh
   ```

### Option 3: Deploy from Docker Hub

If you want to deploy using the pre-built images from Docker Hub:

```bash
# On Windows
deploy-from-dockerhub.bat

# On Linux/Mac
chmod +x deploy-from-dockerhub.sh
./deploy-from-dockerhub.sh
```

This command will:
- Pull the Docker images from Docker Hub
- Start the containers in detached mode

## Access the Application

Once the deployment is complete, you can access the application at:

- Frontend: http://localhost
- Backend API: http://localhost:5000

## Default Login Credentials

Use the following credentials to log in:

- Email: admin@alumni.edu
- Password: admin123

## Stop the Application

To stop the application, run:

```bash
# On Windows
stop.bat

# On Linux/Mac
chmod +x stop.sh
./stop.sh
```

## Docker Architecture

The application is containerized using Docker with the following components:

1. **Server Container (alumni-server)**
   - Python Flask backend
   - Connects to MongoDB Atlas
   - Exposes port 5000
   - Docker Hub image: ynodev/alumni-server:latest

2. **Client Container (alumni-client)**
   - React frontend
   - Nginx web server
   - Exposes port 80
   - Proxies API requests to the server container
   - Docker Hub image: ynodev/alumni-client:latest

## Troubleshooting

### Container Logs

To view logs for a specific container:

```bash
# View server logs
docker logs alumni-server

# View client logs
docker logs alumni-client
```

### Restarting Containers

If you need to restart the containers:

```bash
docker-compose restart
```

### Rebuilding Containers

If you've made changes to the code and need to rebuild:

```bash
docker-compose up -d --build
```
