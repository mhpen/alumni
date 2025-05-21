# Fix CORS Issues for Alumni Management System

This guide will help you fix the CORS issues preventing your Vercel frontend from communicating with your Render.com backend.

## Step 1: Update Your Backend Server

1. **Open Docker Desktop** if it's not already running

2. **Log in to Docker Hub** through Docker Desktop:
   - Click on the Docker icon in your system tray
   - Click on "Sign in" if you're not already signed in
   - Enter your Docker Hub credentials (username: ynodev)

3. **Update your server code**:
   - Open a Command Prompt or PowerShell window
   - Navigate to your project directory:
   ```
   cd C:\Users\mhrkp\OneDrive\Desktop\AlumniManagementSystem
   ```
   - Copy the CORS-fixed app.py file:
   ```
   copy server\src\app.py.cors server\src\app.py
   ```
   - Build the Docker image:
   ```
   docker build -t ynodev/alumni-server:cors-fixed -f server/Dockerfile.render server
   ```
   - Push the image to Docker Hub:
   ```
   docker push ynodev/alumni-server:cors-fixed
   ```

## Step 2: Update Your Render.com Deployment

1. **Go to your Render.com dashboard**:
   - Navigate to https://dashboard.render.com/
   - Log in to your account

2. **Update your server service**:
   - Navigate to your alumni-server-1-zato service
   - Click on "Settings"
   - Update the Docker image URL to: `docker.io/ynodev/alumni-server:cors-fixed`
   - Make sure the following environment variables are set:
     - `MONGODB_URI`: `mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement`
     - `DATABASE_NAME`: `alumni_management`
     - `JWT_SECRET_KEY`: `your_super_secret_key_for_jwt_tokens`
     - `PORT`: `5000`
     - `CORS_ALLOW_ORIGINS`: `https://alumni-client-three.vercel.app`
   - Click "Save Changes"
   - Click on "Manual Deploy" > "Deploy latest image"

## Step 3: Verify the Fix

1. **Wait for the deployment to complete**

2. **Test the CORS configuration**:
   - Open a browser and go to:
   ```
   https://alumni-server-1-zato.onrender.com/api/cors-test
   ```
   - You should see a JSON response indicating that CORS is working correctly

3. **Test the frontend-backend integration**:
   - Go to your frontend: https://alumni-client-three.vercel.app
   - Try to log in with the default credentials:
     - Email: admin@alumni.edu
     - Password: admin123
   - Navigate through the application to verify that it's working correctly

## What Was Fixed

The CORS issue was fixed by:

1. **Configuring CORS properly in Flask**:
   - Added explicit support for the OPTIONS method (preflight requests)
   - Added the necessary CORS headers to allow requests from your Vercel frontend
   - Added support for credentials in CORS requests

2. **Adding explicit handling for OPTIONS requests**:
   - Created a route handler for OPTIONS requests to ensure proper CORS headers are returned

3. **Adding a CORS test endpoint**:
   - Created a `/api/cors-test` endpoint to verify that CORS is working correctly

## Troubleshooting

If you still encounter CORS issues:

1. **Check the browser console for specific CORS errors**:
   - The error message will provide more details about what's failing

2. **Verify that the environment variables are set correctly**:
   - Make sure `CORS_ALLOW_ORIGINS` is set to exactly `https://alumni-client-three.vercel.app`

3. **Check the Render.com logs**:
   - Look for any errors related to CORS or the OPTIONS method
