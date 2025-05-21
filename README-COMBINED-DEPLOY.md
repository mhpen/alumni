# Alumni Management System - Combined Deployment Guide

This guide explains how to deploy the Alumni Management System as a single application on Render.com using the combined deployment approach.

## What is the Combined Deployment?

The combined deployment approach serves both the frontend and backend from a single server. This has several advantages:

1. **No CORS Issues**: Since both the frontend and backend are served from the same domain, there are no CORS issues.
2. **Simplified Deployment**: You only need to manage one deployment instead of two.
3. **Reduced Costs**: You only need one service on Render.com instead of two.
4. **Improved Performance**: The frontend and backend can communicate more efficiently.

## Deployment Options

There are two ways to deploy the combined application on Render.com:

### Option 1: Deploy using render.yaml (Recommended)

1. **Fork or Clone the Repository**:
   - Fork or clone this repository to your GitHub account.

2. **Connect to Render.com**:
   - Go to https://dashboard.render.com/
   - Click on "New" and select "Blueprint"
   - Connect your GitHub account and select the repository
   - Render.com will automatically detect the render.yaml file and create the service

3. **Deploy the Service**:
   - Click "Apply" to deploy the service
   - Render.com will build and deploy the application

### Option 2: Deploy using Docker Image

If you prefer to use a pre-built Docker image:

1. **Go to Render.com Dashboard**:
   - Visit https://dashboard.render.com/

2. **Create a New Web Service**:
   - Click on "New" and select "Web Service"
   - Select "Docker" as the environment
   - Enter "docker.io/ynodev/alumni-combined:latest" as the Docker image
   - Set the name to "alumni-combined"
   - Click "Create Web Service"

3. **Configure Environment Variables**:
   - In the "Environment" section, add the following variables:
     - MONGODB_URI: mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement
     - DATABASE_NAME: alumni_management
     - JWT_SECRET_KEY: your_super_secret_key_for_jwt_tokens
     - PORT: 5000

## Testing the Deployment

1. **Access the Application**:
   - Once deployed, your application will be available at the URL provided by Render.com
   - For example: https://alumni-combined.onrender.com

2. **Log In**:
   - Use the default credentials:
     - Email: admin@alumni.edu
     - Password: admin123

3. **Check the API**:
   - The API endpoints will be available at `/api/*`
   - For example: https://alumni-combined.onrender.com/api/health

## Troubleshooting

If you encounter issues with the deployment:

1. **Check the Render.com Logs**:
   - Go to your service on Render.com
   - Click on "Logs" to see the server logs
   - Look for any error messages

2. **Common Issues**:
   - **Build Failures**: Make sure the Dockerfile.combined is correct
   - **Runtime Errors**: Check the logs for any Python or Node.js errors
   - **Database Connection**: Make sure the MongoDB connection string is correct

3. **Contact Support**:
   - If you continue to experience issues, contact Render.com support or open an issue on the GitHub repository
