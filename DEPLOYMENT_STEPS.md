# Deployment Steps for Alumni Management System

## Step 1: Update Your Vercel Frontend

1. **Open Docker Desktop** if it's not already running

2. **Log in to GitHub** in your browser:
   - Go to https://github.com/login
   - Enter your credentials

3. **Push your updated frontend code to GitHub**:
   - Open a Command Prompt or PowerShell window
   - Navigate to your project directory:
   ```
   cd C:\Users\mhrkp\OneDrive\Desktop\AlumniManagementSystem\client
   ```
   - Add all files to Git:
   ```
   git add .
   ```
   - Commit the changes:
   ```
   git commit -m "Update API URL to point to Render.com server"
   ```
   - Push to GitHub:
   ```
   git push
   ```

4. **Deploy on Vercel**:
   - Go to https://vercel.com/dashboard
   - Select your alumni-client project
   - If automatic deployments are enabled, Vercel will deploy the changes automatically
   - Otherwise, click "Deploy" to trigger a manual deployment

## Step 2: Update Your Render.com Backend

1. **Log in to Docker Hub** through Docker Desktop:
   - Click on the Docker icon in your system tray
   - Click on "Sign in" if you're not already signed in
   - Enter your Docker Hub credentials (username: ynodev)

2. **Build and push the Docker image**:
   - Open a Command Prompt or PowerShell window
   - Navigate to your project directory:
   ```
   cd C:\Users\mhrkp\OneDrive\Desktop\AlumniManagementSystem
   ```
   - Copy the updated app.py file:
   ```
   copy server\src\app.py.vercel server\src\app.py
   ```
   - Build the Docker image:
   ```
   docker build -t ynodev/alumni-server:vercel -f server/Dockerfile.render server
   ```
   - Push the image to Docker Hub:
   ```
   docker push ynodev/alumni-server:vercel
   ```

3. **Update your Render.com deployment**:
   - Go to https://dashboard.render.com/
   - Navigate to your alumni-server-1-zato service
   - Click on "Settings"
   - Update the Docker image URL to: `docker.io/ynodev/alumni-server:vercel`
   - Make sure the following environment variables are set:
     - `MONGODB_URI`: `mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement`
     - `DATABASE_NAME`: `alumni_management`
     - `JWT_SECRET_KEY`: `your_super_secret_key_for_jwt_tokens`
     - `PORT`: `5000`
     - `CORS_ALLOW_ORIGINS`: `https://alumni-client-three.vercel.app`
   - Click "Save Changes"
   - Click on "Manual Deploy" > "Deploy latest image"

## Step 3: Verify the Integration

1. **Wait for both deployments to complete**

2. **Test the frontend-backend integration**:
   - Go to your frontend: https://alumni-client-three.vercel.app
   - Try to log in with the default credentials:
     - Email: admin@alumni.edu
     - Password: admin123
   - Navigate through the application to verify that it's working correctly

3. **Check for any errors**:
   - Open your browser's developer tools (F12)
   - Go to the Console tab
   - Look for any API-related errors

## Troubleshooting

If you encounter any issues:

1. **Check the Render.com logs**:
   - Go to your Render.com dashboard
   - Navigate to your alumni-server-1-zato service
   - Click on "Logs" to view any error messages

2. **Check the CORS configuration**:
   - Make sure the `CORS_ALLOW_ORIGINS` environment variable is set correctly
   - Verify that your frontend is making requests to the correct API URL

3. **Test the API directly**:
   - Open a browser and go to https://alumni-server-1-zato.onrender.com/api
   - You should see a JSON response with the message "Alumni Management System API"
