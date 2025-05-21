@echo off
echo Deploying Alumni Management System from Docker Hub...

echo Pulling Docker images...
docker pull ynodev/alumni-server:latest
docker pull ynodev/alumni-client:latest

echo Starting containers...
docker-compose up -d

echo.
echo Deployment complete!
echo.
echo The application is now running at:
echo - Frontend: http://localhost
echo - Backend API: http://localhost:5000
echo.
echo To stop the application, run: docker-compose down
