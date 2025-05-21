@echo off
echo Updating server for Vercel frontend integration...

echo Copying the Vercel-specific app.py file...
copy /Y src\app.py.vercel src\app.py

echo Building and pushing Docker image to Docker Hub...
docker build -t ynodev/alumni-server:vercel -f Dockerfile.render .
docker push ynodev/alumni-server:vercel

echo.
echo Server update complete!
echo.
echo To update your Render.com deployment:
echo 1. Go to https://dashboard.render.com/
echo 2. Navigate to your alumni-server-1-zato service
echo 3. Click on "Settings"
echo 4. Update the Docker image URL to: docker.io/ynodev/alumni-server:vercel
echo 5. Make sure the following environment variables are set:
echo    - MONGODB_URI: mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement
echo    - DATABASE_NAME: alumni_management
echo    - JWT_SECRET_KEY: your_super_secret_key_for_jwt_tokens
echo    - PORT: 5000
echo    - CORS_ALLOW_ORIGINS: https://alumni-client-three.vercel.app
echo 6. Click "Save Changes"
echo 7. Click on "Manual Deploy" > "Deploy latest image"
echo.
echo After updating both the frontend and backend, your application will be fully functional with:
echo - Frontend: https://alumni-client-three.vercel.app
echo - Backend API: https://alumni-server-1-zato.onrender.com
echo.
pause
