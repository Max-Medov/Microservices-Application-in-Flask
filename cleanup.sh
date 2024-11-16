#!/bin/bash

# Delete Kubernetes resources
echo "Deleting Kubernetes resources..."
kubectl delete -f /k8s/Microservices-Application-in-Flask

# Remove entries from /etc/hosts
echo "Removing entries from /etc/hosts (requires sudo)..."
sudo sed -i '/user\.local$/d' /etc/hosts
sudo sed -i '/product\.local$/d' /etc/hosts
sudo sed -i '/order\.local$/d' /etc/hosts

# Stop Minikube
echo "Stopping Minikube..."
minikube stop

echo "Cleanup completed."

