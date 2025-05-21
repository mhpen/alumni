@echo off
echo Deploying Alumni Management System to Render.com from GitHub...

echo.
echo Please follow these steps:
echo 1. Go to https://dashboard.render.com/
echo 2. Click on "New" and select "Web Service"
echo 3. Connect your GitHub repository (mhpen/alumni)
echo 4. Configure the service:
echo    - Name: alumni-combined
echo    - Environment: Docker
echo    - Branch: main
echo    - Docker Command: (leave empty)
echo 5. Click "Create Web Service"
echo.
echo After deployment, your application will be available at:
echo https://alumni-combined.onrender.com
echo.
echo Opening Render dashboard...
start https://dashboard.render.com/

echo.
echo Deployment process initiated!
