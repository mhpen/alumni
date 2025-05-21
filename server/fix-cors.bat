@echo off
echo Fixing CORS issues for Vercel frontend integration...

echo Copying the CORS-fixed app.py file...
copy /Y src\app.py.cors src\app.py

echo Building and pushing Docker image to Docker Hub...
docker build -t ynodev/alumni-server:cors-fixed -f Dockerfile.render .
docker push ynodev/alumni-server:cors-fixed

echo.
echo CORS fix complete!
echo.
echo To update your Render.com deployment:
echo 1. Go to https://dashboard.render.com/
echo 2. Navigate to your alumni-server-1-zato service
echo 3. Click on "Settings"
echo 4. Update the Docker image URL to: docker.io/ynodev/alumni-server:cors-fixed
echo 5. Make sure the following environment variables are set:
echo    - MONGODB_URI: mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement
echo    - DATABASE_NAME: alumni_management
echo    - JWT_SECRET_KEY: your_super_secret_key_for_jwt_tokens
echo    - PORT: 5000
echo    - CORS_ALLOW_ORIGINS: https://alumni-client-three.vercel.app
echo 6. Click "Save Changes"
echo 7. Click on "Manual Deploy" > "Deploy latest image"
echo.
echo After updating the backend, your application should work correctly with:
echo - Frontend: https://alumni-client-three.vercel.app
echo - Backend API: https://alumni-server-1-zato.onrender.com
echo.
echo You can test if CORS is working by visiting:
echo https://alumni-server-1-zato.onrender.com/api/cors-test
echo.
pause
