# Docker Deployment Fix for Alumni Management System

## Issue Fixed

The original Docker build was failing with the following error:

```
[frontend-build 4/6] RUN npm install:
npm ERR! code ENOENT
npm ERR! syscall open
npm ERR! path /app/client/package.json
npm ERR! errno -2
npm ERR! enoent ENOENT: no such file or directory, open '/app/client/package.json'
```

## Root Cause

The issue was in the Dockerfile.combined file where the COPY command for the package.json file was not correctly referencing the file path. In Docker, the COPY command paths are relative to the build context (the directory where you run the docker build command), not relative to the WORKDIR inside the container.

## Solution

The fix includes two important changes:

1. Added explicit path references in the COPY commands by adding `./` prefix to make it clear that the paths are relative to the build context:

```dockerfile
# Original (problematic)
COPY client/package*.json ./

# Fixed
COPY ./client/package*.json ./
```

2. Fixed the utils directory copy command since the directory exists but appears to be empty:

```dockerfile
# Original (problematic)
mkdir -p /app/utils && \
cp -r /app/src/utils/* /app/utils/

# Fixed
mkdir -p /app/utils
```

## How to Use the Fixed Dockerfile

1. Use the new Dockerfile.combined.fixed file for your builds
2. Run the build-combined-fixed.bat script to build and push the Docker image

```
build-combined-fixed.bat
```

## Deployment Instructions

After building the Docker image:

1. Go to https://dashboard.render.com/
2. Click on "New" and select "Web Service"
3. Select "Docker" as the environment
4. Enter "docker.io/ynodev/alumni-combined:latest" as the Docker image
5. Set the name to "alumni-combined"
6. Click "Create Web Service"

Your application will be available at: https://alumni-combined.onrender.com

## Separate Deployment Strategy

As per your preference, you can continue to:
- Deploy the frontend separately on GitHub (alumni-client repository)
- Deploy the server on Docker/Render

This combined Docker image is an alternative approach that packages both frontend and backend together for simpler deployment.
