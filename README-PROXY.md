# Alumni Management System - CORS Proxy Solution

This document explains the CORS proxy solution implemented to fix the communication issues between the Vercel frontend and Render.com backend.

## The Problem

The Alumni Management System was experiencing CORS (Cross-Origin Resource Sharing) issues when the frontend deployed on Vercel tried to communicate with the backend deployed on Render.com. This resulted in errors like:

```
Access to XMLHttpRequest at 'https://alumni-server-1-zato.onrender.com/api/admin/login' from origin 'https://alumni-client-three.vercel.app' has been blocked by CORS policy
```

## The Solution

We implemented a proxy server solution to fix the CORS issues:

1. **Created a Node.js Proxy Server**:
   - Uses Express.js to create a simple server
   - Uses http-proxy-middleware to proxy requests to the Render.com backend
   - Adds proper CORS headers to all responses

2. **Deployed the Proxy Server on Render.com**:
   - Built and pushed a Docker image to Docker Hub
   - Deployed the Docker image on Render.com

3. **Updated the Client Configuration**:
   - Modified the Vercel configuration to proxy requests through the proxy server
   - Updated the API service to handle errors better

## How It Works

1. The frontend makes requests to `/api/*` endpoints
2. Vercel's rewrites forward these requests to the proxy server at `https://alumni-proxy.onrender.com/api/*`
3. The proxy server forwards the requests to the backend at `https://alumni-server-1-zato.onrender.com/api/*`
4. The proxy server adds CORS headers to the responses
5. The frontend receives the responses with the proper CORS headers

## Deployment Details

### Proxy Server

- **Docker Image**: `docker.io/ynodev/alumni-proxy:latest`
- **Deployment URL**: `https://alumni-proxy.onrender.com`

### Frontend

- **Deployment URL**: `https://alumni-client-three.vercel.app`
- **Vercel Configuration**: Uses rewrites to proxy requests through the proxy server

### Backend

- **Deployment URL**: `https://alumni-server-1-zato.onrender.com`
- **Docker Image**: `docker.io/ynodev/alumni-server:vercel-fix`

## Troubleshooting

If you encounter CORS issues:

1. Check the proxy server logs on Render.com
2. Make sure the proxy server is correctly forwarding requests to the backend
3. Verify that the client is using the correct proxy server URL
4. Check the browser console for specific error messages

## Maintenance

To update the proxy server:

1. Modify the proxy server code in `proxy-server.js`
2. Build and push a new Docker image:
   ```
   docker build -t ynodev/alumni-proxy:latest -f Dockerfile.proxy .
   docker push ynodev/alumni-proxy:latest
   ```
3. Redeploy the proxy server on Render.com
