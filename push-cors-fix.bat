@echo off
echo Pushing CORS fix to Docker Hub...

echo Building Docker image...
docker build -t ynodev/alumni-server:cors-fixed -f server/Dockerfile.render server

echo Pushing image to Docker Hub...
docker push ynodev/alumni-server:cors-fixed

echo.
echo Build and push complete!
echo.
echo The Docker image is now available at:
echo - Server: docker.io/ynodev/alumni-server:cors-fixed
echo.
echo To update your Render.com deployment:
echo 1. Go to https://dashboard.render.com/
echo 2. Navigate to your alumni-server-1-zato service
echo 3. Click on "Settings"
echo 4. Update the Docker image URL to: docker.io/ynodev/alumni-server:cors-fixed
echo 5. Click "Save Changes"
echo 6. Click on "Manual Deploy" > "Deploy latest image"
echo.
pause
