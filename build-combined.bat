@echo off
echo Building and pushing combined Alumni Management System Docker image...

echo Building Docker image...
docker build -t ynodev/alumni-combined:latest -f Dockerfile.combined .

echo Pushing image to Docker Hub...
docker push ynodev/alumni-combined:latest

echo.
echo Build and push complete!
echo.
echo The Docker image is now available at:
echo - Combined App: docker.io/ynodev/alumni-combined:latest
echo.
echo To deploy on Render.com:
echo 1. Go to https://dashboard.render.com/
echo 2. Click on "New" and select "Web Service"
echo 3. Select "Docker" as the environment
echo 4. Enter "docker.io/ynodev/alumni-combined:latest" as the Docker image
echo 5. Set the name to "alumni-combined"
echo 6. Click "Create Web Service"
echo.
echo After deployment, your application will be available at:
echo https://alumni-combined.onrender.com
