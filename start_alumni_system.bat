@echo off
echo Starting Alumni Management System

REM Start the server in a new window
start cmd /k "cd server && start_server.bat"

REM Start the React client in a new window
start cmd /k "cd client && start_client.bat"

REM Wait for the server and client to start
echo Waiting for server and client to start...
timeout /t 10 /nobreak > nul

REM Open the client in the default browser
echo Opening client in browser...
start "" "http://localhost:3000"

echo Alumni Management System started successfully!
echo Server is running at http://localhost:5000
echo Client is running at http://localhost:3000

pause
