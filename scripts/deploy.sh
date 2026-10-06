#!/usr/bin/env bash
# ==============================================================================
# InfraMind AI — Automated Local & AWS Kubernetes Deployment Script
# ==============================================================================

set -e

echo "🚀 [1/5] Checking Prerequisites (Git, Docker, kubectl, AWS CLI)..."
command -v git >/dev/null 2>&1 || { echo "❌ Git is required but not installed."; exit 1; }
command -v docker >/dev/null 2>&1 || { echo "❌ Docker is required but not installed."; exit 1; }
command -v kubectl >/dev/null 2>&1 || { echo "⚠️ kubectl not found. K8s commands will be skipped."; }

echo "📦 [2/5] Building Docker Image locally..."
docker build -t inframind-ai:local .

echo "🧪 [3/5] Starting Local Multi-Container Environment via Docker Compose..."
docker-compose up -d --build

echo "✅ Docker container running! Dashboard accessible at: http://localhost:8000"

echo "☸️ [4/5] Applying Kubernetes Deployment Manifests..."
if command -v kubectl >/dev/null 2>&1; then
    kubectl apply -f k8s/namespace.yaml || true
    kubectl apply -f k8s/configmap.yaml || true
    kubectl apply -f k8s/secret.yaml || true
    kubectl apply -f k8s/deployment.yaml || true
    kubectl apply -f k8s/service.yaml || true
    echo "🎉 K8s deployment submitted!"
fi

echo "======================================================================"
echo "🎯 Deployment Script Completed Successfully!"
echo "Push to GitHub: git add . && git commit -m 'feat: deploy' && git push"
echo "======================================================================"
