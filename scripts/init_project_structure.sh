#!/bin/bash

# Set absolute base path
BASE_DIR="/d/Next_JS/pomodoro"

echo "Creating folder structure in: $BASE_DIR"

# Frontend folders
mkdir -p "$BASE_DIR/frontend/app"
mkdir -p "$BASE_DIR/frontend/components"
mkdir -p "$BASE_DIR/frontend/contexts"
mkdir -p "$BASE_DIR/frontend/styles"
mkdir -p "$BASE_DIR/frontend/utils"
mkdir -p "$BASE_DIR/frontend/public"

# Frontend files
touch "$BASE_DIR/frontend/.env.local"
touch "$BASE_DIR/frontend/next.config.js"
touch "$BASE_DIR/frontend/package.json"
touch "$BASE_DIR/frontend/README.md"

# Backend folders
mkdir -p "$BASE_DIR/backend/app/api/v1/endpoints"
mkdir -p "$BASE_DIR/backend/app/api/deps"
mkdir -p "$BASE_DIR/backend/app/core"
mkdir -p "$BASE_DIR/backend/app/db"
mkdir -p "$BASE_DIR/backend/app/models"
mkdir -p "$BASE_DIR/backend/app/services"
mkdir -p "$BASE_DIR/backend/app/utils"

# Backend files
touch "$BASE_DIR/backend/app/main.py"
touch "$BASE_DIR/backend/app/__init__.py"
touch "$BASE_DIR/backend/.env"
touch "$BASE_DIR/backend/requirements.txt"
touch "$BASE_DIR/backend/Dockerfile"

# Kubernetes folder and files
mkdir -p "$BASE_DIR/k8s"
touch "$BASE_DIR/k8s/backend-deployment.yaml"
touch "$BASE_DIR/k8s/mongodb-deployment.yaml"
touch "$BASE_DIR/k8s/janusgraph-deployment.yaml"
touch "$BASE_DIR/k8s/minio-deployment.yaml"
touch "$BASE_DIR/k8s/ingress.yaml"

echo "Done! Folder structure created in $BASE_DIR"
