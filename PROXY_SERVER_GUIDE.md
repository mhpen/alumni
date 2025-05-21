# Proxy Server Guide for Alumni Management System

This guide explains how to set up a proxy server to solve CORS issues between your Vercel frontend and Render.com backend.

## What is a Proxy Server?

A proxy server acts as an intermediary between your frontend and backend. It receives requests from the frontend, forwards them to the backend, and returns the responses to the frontend. This approach solves CORS issues because:

1. The proxy server adds the necessary CORS headers to the responses
2. The frontend communicates with the proxy server, which is on the same domain or has proper CORS configuration

## Step 1: Build and Push the Proxy Server Docker Image

1. Run the `build-proxy.bat` script to build and push the Docker image:
   ```
   build-proxy.bat
   ```

## Step 2: Deploy the Proxy Server on Render.com

1. Go to https://dashboard.render.com/
2. Click on "New" and select "Web Service"
3. Select "Docker" as the environment
4. Enter "docker.io/ynodev/alumni-proxy:latest" as the Docker image
5. Set the name to "alumni-proxy"
6. Click "Create Web Service"

## Step 3: Update the Client's API URL

1. Open `client/src/utils/api.js`
2. Update the `getBaseUrl` function to use the proxy server URL:
   ```javascript
   const getBaseUrl = () => {
     // Use environment variable if available
     if (process.env.REACT_APP_API_URL) {
       return process.env.REACT_APP_API_URL;
     }

     // Check if we're in production (deployed on Vercel)
     if (process.env.NODE_ENV === 'production') {
       // Use the proxy server URL
       return 'https://alumni-proxy.onrender.com/api';
     }

     // For local development, use the local API
     return '/api';
   };
   ```

3. Deploy the updated client to Vercel

## Step 4: Test the Solution

1. Go to your frontend: https://alumni-client-three.vercel.app
2. Try to log in with the default credentials:
   - Email: admin@alumni.edu
   - Password: admin123
3. Navigate through the application to verify that it's working correctly

## How It Works

1. The frontend makes requests to the proxy server
2. The proxy server forwards the requests to the backend
3. The proxy server adds CORS headers to the responses
4. The frontend receives the responses with the proper CORS headers

This approach solves CORS issues without requiring changes to the backend code.

## Troubleshooting

If you still encounter CORS issues:

1. Check the proxy server logs on Render.com
2. Make sure the proxy server is correctly forwarding requests to the backend
3. Verify that the client is using the correct proxy server URL
