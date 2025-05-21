@echo off
echo Deploying Alumni Management System using multiple approaches...

echo.
echo Step 1: Building and pushing robust Docker image (most likely to work)...
call .\build-robust.bat

echo.
echo Step 2: Building and pushing minimal Docker image...
call .\build-minimal.bat

echo.
echo Step 3: Building and pushing simple Docker image...
call .\build-simple.bat

echo.
echo Step 4: Building and pushing standalone Docker image...
call .\build-standalone.bat

echo.
echo Step 5: Building and pushing prebuilt Docker image...
call .\build-prebuilt.bat

echo.
echo Step 6: Building and pushing nginx Docker image...
call .\build-nginx.bat

echo.
echo All Docker images have been built and pushed!
echo.
echo To deploy on Render.com:
echo 1. Go to https://dashboard.render.com/
echo 2. Click on "New" and select "Web Service"
echo 3. Connect your GitHub repository
echo 4. Render will use the render.yaml file to configure all services
echo 5. Click "Create Web Service"
echo.
echo Opening Render dashboard...
start https://dashboard.render.com/

echo.
echo Deployment process initiated!
echo.
echo For more information, please refer to the COMPREHENSIVE_DEPLOYMENT_GUIDE.md file.
