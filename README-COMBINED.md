# Alumni Management System - Combined Deployment

This document explains how to deploy the Alumni Management System as a combined application on Render.com.

## Why Combined Deployment?

Deploying the frontend and backend as a single application has several advantages:

1. **No CORS Issues**: Since both the frontend and backend are served from the same domain, there are no CORS issues.
2. **Simplified Deployment**: You only need to manage one deployment instead of two.
3. **Reduced Costs**: You only need one service on Render.com instead of two.
4. **Improved Performance**: The frontend and backend can communicate more efficiently.

## How It Works

The combined deployment uses a multi-stage Docker build:

1. **Stage 1**: Build the React frontend
2. **Stage 2**: Create a Python Flask application that serves both:
   - The React frontend as static files
   - The API endpoints at the `/api` path

## Deployment Steps

1. **Build and Push the Docker Image**:
   - Run the `build-combined.bat` script to build and push the Docker image to Docker Hub.

2. **Deploy on Render.com**:
   - Go to https://dashboard.render.com/
   - Click on "New" and select "Web Service"
   - Select "Docker" as the environment
   - Enter "docker.io/ynodev/alumni-combined:latest" as the Docker image
   - Set the name to "alumni-combined"
   - Click "Create Web Service"

3. **Access the Application**:
   - Once deployed, your application will be available at:
   - https://alumni-combined.onrender.com

## Technical Details

### Dockerfile

The `Dockerfile.combined` file defines a multi-stage build:

1. **Frontend Build Stage**:
   - Uses Node.js to build the React frontend
   - Outputs the built files to `/app/frontend/build`

2. **Final Stage**:
   - Uses Python to run the Flask backend
   - Copies the built frontend files to `/app/static`
   - Creates a server that serves both the API and static files

### Server Configuration

The combined server uses Flask to:

1. Mount the API app at the `/api` path
2. Serve the React frontend as static files
3. Handle client-side routing by serving `index.html` for unknown paths

## Troubleshooting

If you encounter issues with the combined deployment:

1. **Check the Render.com Logs**:
   - Go to your service on Render.com
   - Click on "Logs" to see the server logs
   - Look for any error messages

2. **Check the Application**:
   - Open the browser console to see any frontend errors
   - Try accessing the API directly at `/api/health` to check if it's working

3. **Common Issues**:
   - **404 Not Found**: Make sure the server is correctly serving the frontend files
   - **API Errors**: Make sure the API is correctly mounted at the `/api` path
   - **Database Connection**: Make sure the database connection string is correctly set in the environment variables
