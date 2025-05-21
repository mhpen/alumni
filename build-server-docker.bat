@echo off
echo Building and pushing server Docker image...

echo Building Docker image...
docker build -t ynodev/alumni-server:latest -f server/Dockerfile.render server

echo Pushing image to Docker Hub...
docker push ynodev/alumni-server:latest

echo.
echo Build and push complete!
echo.
echo The Docker image is now available at:
echo - Server: docker.io/ynodev/alumni-server:latest
echo.
echo To deploy on Render.com, use this image URL in your Web Service configuration.
pause
