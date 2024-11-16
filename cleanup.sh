#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Delete Kubernetes resources from the script's directory
echo "Deleting Kubernetes resources..."
kubectl delete -f "$SCRIPT_DIR/k8s/"

# Remove entries from /etc/hosts
echo "Removing entries from /etc/hosts (requires sudo)..."
sudo sed -i '/user\.local$/d' /etc/hosts
sudo sed -i '/product\.local$/d' /etc/hosts
sudo sed -i '/order\.local$/d' /etc/hosts

# Stop Minikube
echo "Stopping Minikube..."
minikube stop

echo "Cleanup completed."

