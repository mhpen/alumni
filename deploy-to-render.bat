@echo off
echo ===================================================
echo Alumni Management System - Render.com Deployment
echo ===================================================
echo.
echo This script will help you deploy the Alumni Management System to Render.com.
echo.
echo Steps:
echo 1. Make sure you have pushed your changes to GitHub
echo 2. Go to https://dashboard.render.com/
echo 3. Click on "New" and select "Blueprint"
echo 4. Connect your GitHub account and select the repository
echo 5. Render.com will automatically detect the render.yaml file and create the service
echo 6. Click "Apply" to deploy the service
echo.
echo Alternatively, you can deploy using the Docker image:
echo 1. Go to https://dashboard.render.com/
echo 2. Click on "New" and select "Web Service"
echo 3. Select "Docker" as the environment
echo 4. Enter the GitHub repository URL: https://github.com/mhpen/alumni.git
echo 5. Set the name to "alumni-combined"
echo 6. Click "Create Web Service"
echo.
echo Opening Render.com dashboard...
start https://dashboard.render.com/
echo.
echo Done! Follow the steps above to complete the deployment.
pause
