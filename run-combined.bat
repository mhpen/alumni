@echo off
echo Running combined Alumni Management System Docker image...

docker-compose -f docker-compose.combined.yml up -d

echo.
echo Deployment complete!
echo.
echo The application is now running at:
echo - http://localhost:5000
echo.
echo To stop the application, run: docker-compose -f docker-compose.combined.yml down
