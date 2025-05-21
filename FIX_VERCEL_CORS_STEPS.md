# Fix CORS Issues for Vercel Frontend

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
   - Copy the Vercel-specific app.py file:
   ```
   copy server\src\app.py.vercel-fix server\src\app.py
   ```
   - Build the Docker image:
   ```
   docker build -t ynodev/alumni-server:vercel-fix -f server/Dockerfile.render server
   ```
   - Push the image to Docker Hub:
   ```
   docker push ynodev/alumni-server:vercel-fix
   ```

## Step 2: Update Your Render.com Deployment

1. **Go to your Render.com dashboard**:
   - Navigate to https://dashboard.render.com/
   - Log in to your account

2. **Update your server service**:
   - Navigate to your alumni-server-1-zato service
   - Click on "Settings"
   - Update the Docker image URL to: `docker.io/ynodev/alumni-server:vercel-fix`
   - Click "Save Changes"

3. **Update the environment variables**:
   - Click on "Environment" in the left sidebar
   - Find the `CORS_ALLOW_ORIGINS` variable
   - Update it to include all your Vercel domains:
   ```
   https://alumni-client-three.vercel.app,https://alumni-client-c09kk4d6h-mhpens-projects.vercel.app,https://alumni-client-git-main-mhpens-projects.vercel.app,https://alumni-client-mhpens-projects.vercel.app
   ```
   - Click "Save Changes"

4. **Deploy the updated server**:
   - Click on "Manual Deploy" in the left sidebar
   - Select "Deploy latest image"
   - Wait for the deployment to complete

## Step 3: Verify the Fix

1. **Test the CORS configuration**:
   - Open a browser and go to:
   ```
   https://alumni-server-1-zato.onrender.com/api/cors-test
   ```
   - You should see a JSON response indicating that CORS is working correctly and listing your Vercel domains

2. **Test the frontend-backend integration**:
   - Go to your frontend: https://alumni-client-c09kk4d6h-mhpens-projects.vercel.app
   - Try to log in with the default credentials:
     - Email: admin@alumni.edu
     - Password: admin123
   - Navigate through the application to verify that it's working correctly

## What Was Fixed

The CORS issue was fixed by:

1. **Updating the CORS configuration in Flask**:
   - Added explicit support for your specific Vercel domain
   - Added an after_request handler to ensure CORS headers are added to all responses
   - Included multiple Vercel domains to handle preview deployments

2. **Updating the environment variables on Render.com**:
   - Added your specific Vercel domain to the CORS_ALLOW_ORIGINS variable

## Troubleshooting

If you still encounter CORS issues:

1. **Check the exact domain of your Vercel deployment**:
   - The domain might change slightly with each deployment
   - Make sure the exact domain is included in the CORS configuration

2. **Try using a wildcard for Vercel domains**:
   - If you continue to have issues with specific domains, you can try using a wildcard:
   ```
   https://alumni-client-*.vercel.app
   ```
   - Note: This is less secure but more flexible

3. **Check the browser console for specific CORS errors**:
   - The error message will provide more details about what's failing
