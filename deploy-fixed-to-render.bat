@echo off
echo Deploying fixed Alumni Management System to Render.com...

echo Building Docker image...
docker build -t ynodev/alumni-combined:latest -f Dockerfile.combined.fixed .

echo Pushing image to Docker Hub...
docker push ynodev/alumni-combined:latest

echo.
echo Docker image pushed successfully!
echo.
echo Now deploying to Render.com...
echo.
echo Please follow these steps:
echo 1. Go to https://dashboard.render.com/
echo 2. Click on "New" and select "Web Service"
echo 3. Select "Docker" as the environment
echo 4. Enter "docker.io/ynodev/alumni-combined:latest" as the Docker image
echo 5. Set the name to "alumni-combined"
echo 6. Click "Create Web Service"
echo.
echo After deployment, your application will be available at:
echo https://alumni-combined.onrender.com
echo.
echo Opening Render dashboard...
start https://dashboard.render.com/

echo.
echo Deployment process initiated!
