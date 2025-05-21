@echo off
echo Building and pushing fixed Alumni Management System Docker image...

echo Building Docker image...
docker-compose -f docker-compose.fixed.yml build

echo Pushing image to Docker Hub...
docker push ynodev/alumni-combined:fixed

echo.
echo Build and push complete!
echo.
echo The Docker image is now available at:
echo - Fixed App: docker.io/ynodev/alumni-combined:fixed
echo.
echo To deploy on Render.com, use this image URL in your Web Service configuration.
