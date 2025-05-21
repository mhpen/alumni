# Deploying Alumni Management System to Render.com from GitHub

This guide explains how to deploy the Alumni Management System directly from GitHub to Render.com without using Docker Hub.

## Prerequisites

- GitHub repository with your Alumni Management System code
- Render.com account

## Deployment Steps

### 1. Create a Web Service on Render.com

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click on "New" and select "Web Service"
3. Connect your GitHub repository
   - Select "GitHub" as the deployment method
   - Connect your GitHub account if not already connected
   - Search for and select your repository (e.g., `mhpen/alumni`)

### 2. Configure the Web Service

1. **Name**: Enter a name for your service (e.g., `alumni-management-system`)
2. **Environment**: Select "Docker"
3. **Branch**: Select the branch you want to deploy (e.g., `main`)
4. **Docker Command**: Leave empty to use the CMD in your Dockerfile
5. **Advanced Settings**:
   - Set any environment variables needed for your application
   - Configure auto-deploy settings as desired

### 3. Deploy the Service

1. Click "Create Web Service"
2. Render will automatically build and deploy your application
3. You can monitor the build and deployment logs on the Render dashboard

## Using the New Dockerfile

Make sure your repository has the `Dockerfile.new` file. You can tell Render to use this specific Dockerfile by adding a `render.yaml` file to your repository:

```yaml
services:
  - type: web
    name: alumni-management-system
    env: docker
    dockerfilePath: ./Dockerfile.new
    plan: free
    branch: main
```

## Troubleshooting

If you encounter issues with the deployment:

1. Check the build logs on Render.com for specific error messages
2. Verify that all required files are present in your GitHub repository
3. Make sure your Dockerfile is correctly configured for your application
4. Check that all environment variables are properly set

## Accessing Your Deployed Application

Once deployed, your application will be available at:
`https://your-service-name.onrender.com`

For example:
`https://alumni-management-system.onrender.com`

## Updating Your Deployment

To update your deployment:

1. Push changes to your GitHub repository
2. Render will automatically rebuild and redeploy your application (if auto-deploy is enabled)
3. You can also manually trigger a deploy from the Render dashboard

## Blueprint Deployment

This deployment approach serves as a blueprint that can be easily replicated for similar applications. The key components are:

1. A well-structured GitHub repository
2. A properly configured Dockerfile
3. A render.yaml file for Render.com configuration
4. Clear documentation for future deployments
