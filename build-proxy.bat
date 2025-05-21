@echo off
echo Building and pushing proxy server Docker image...

docker build -t ynodev/alumni-proxy:latest -f Dockerfile.proxy .
docker push ynodev/alumni-proxy:latest

echo.
echo Proxy server Docker image built and pushed successfully!
echo.
echo To deploy the proxy server on Render.com:
echo 1. Go to https://dashboard.render.com/
echo 2. Click on "New" and select "Web Service"
echo 3. Select "Docker" as the environment
echo 4. Enter "docker.io/ynodev/alumni-proxy:latest" as the Docker image
echo 5. Set the name to "alumni-proxy"
echo 6. Click "Create Web Service"
echo.
echo After deploying the proxy server, update the client's API URL to point to the proxy server:
echo - In client/src/utils/api.js, update the API_BASE_URL to point to your proxy server URL
echo.
pause
