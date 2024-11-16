#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Start Minikube if not running
if ! minikube status &>/dev/null; then
  echo "Starting Minikube..."
  minikube start
fi

# Enable Ingress addon
echo "Enabling Ingress addon..."
minikube addons enable ingress

# Apply Kubernetes manifests from the script's directory
echo "Applying Kubernetes manifests..."
kubectl apply -f "$SCRIPT_DIR"

# Get Minikube IP
MINIKUBE_IP=$(minikube ip)

# Update /etc/hosts
echo "Updating /etc/hosts (requires sudo)..."
sudo sh -c "echo '$MINIKUBE_IP user.local' >> /etc/hosts"
sudo sh -c "echo '$MINIKUBE_IP product.local' >> /etc/hosts"
sudo sh -c "echo '$MINIKUBE_IP order.local' >> /etc/hosts"

echo "Deployment completed. Services are accessible at:"
echo "http://user.local/"
echo "http://product.local/"
echo "http://order.local/"

