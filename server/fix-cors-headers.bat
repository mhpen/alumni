@echo off
echo Fixing CORS headers issue...

echo Copying the fixed app.py file...
copy /Y src\app.py.fixed src\app.py

echo Building and pushing Docker image to Docker Hub...
docker build -t ynodev/alumni-server:cors-headers-fixed -f Dockerfile.render .
docker push ynodev/alumni-server:cors-headers-fixed

echo.
echo CORS headers fix complete!
echo.
echo To update your Render.com deployment:
echo 1. Go to https://dashboard.render.com/
echo 2. Navigate to your alumni-server-1-zato service
echo 3. Click on "Settings"
echo 4. Update the Docker image URL to: docker.io/ynodev/alumni-server:cors-headers-fixed
echo 5. Click "Save Changes"
echo 6. Click on "Manual Deploy" > "Deploy latest image"
echo.
echo After updating the backend, your application should work correctly with:
echo - Frontend: https://alumni-client-three.vercel.app
echo - Backend API: https://alumni-server-1-zato.onrender.com
echo.
echo You can test if CORS is working by visiting:
echo https://alumni-server-1-zato.onrender.com/api/cors-test
echo.
pause
