@echo off
echo Preparing server for Render.com deployment...

echo Copying the Render-specific app.py file...
copy /Y src\app.py.render src\app.py

echo Building and pushing Docker image to Docker Hub...
docker build -t ynodev/alumni-server:latest -f Dockerfile.render .
docker push ynodev/alumni-server:latest

echo.
echo Server preparation complete!
echo.
echo To deploy on Render.com:
echo 1. Go to https://dashboard.render.com/
echo 2. Click on "New" and select "Web Service"
echo 3. Choose "Deploy an existing image from a registry"
echo 4. Enter the image URL: docker.io/ynodev/alumni-server:latest
echo 5. Configure the environment variables:
echo    - MONGODB_URI: mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement
echo    - DATABASE_NAME: alumni_management
echo    - JWT_SECRET_KEY: your_super_secret_key_for_jwt_tokens
echo    - PORT: 5000
echo    - CORS_ALLOW_ORIGINS: https://alumni-client-three.vercel.app
echo.
echo After deploying the server, your application will be fully functional with:
echo - Frontend: https://alumni-client-three.vercel.app
echo - Backend API: https://your-render-service-name.onrender.com
echo.
pause
