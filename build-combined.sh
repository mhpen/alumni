#!/bin/bash

echo "Building and pushing combined Alumni Management System Docker image..."

echo "Building Docker image..."
docker-compose -f docker-compose.combined.yml build

echo "Pushing image to Docker Hub..."
docker push ynodev/alumni-combined:latest

echo ""
echo "Build and push complete!"
echo ""
echo "The Docker image is now available at:"
echo "- Combined App: docker.io/ynodev/alumni-combined:latest"
echo ""
echo "To deploy on Render.com, use this image URL in your Web Service configuration."
