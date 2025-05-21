#!/bin/bash

echo "Building and deploying Alumni Management System with Docker..."

echo "Building Docker images and starting containers..."
docker-compose up -d --build

echo ""
echo "Deployment complete!"
echo ""
echo "The application is now running at:"
echo "- Frontend: http://localhost"
echo "- Backend API: http://localhost:5000"
echo ""
echo "To stop the application, run: docker-compose down"
