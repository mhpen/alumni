#!/bin/bash

echo "Building and pushing Alumni Management System Docker images to Docker Hub..."

echo "Building Docker images..."
docker-compose build

echo "Pushing images to Docker Hub..."
docker push ynodev/alumni-server:latest
docker push ynodev/alumni-client:latest

echo ""
echo "Push complete!"
echo ""
echo "The Docker images are now available at:"
echo "- Server: docker.io/ynodev/alumni-server:latest"
echo "- Client: docker.io/ynodev/alumni-client:latest"
echo ""
echo "To deploy from Docker Hub, run: docker-compose up -d"
