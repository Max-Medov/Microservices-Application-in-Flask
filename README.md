The system will be divided into three microservices, each responsible for a specific domain of functionality:

1. User Service: Manages user-related operations, including registration, authentication, and profile updates.
Endpoints:
/register: Register a new user.
/login: Authenticate a user.
/profile: Retrieve or update user profile.

2. Product Service: Handles all product-related operations, such as managing product inventory and viewing details.
Endpoints:
/add: Add a new product.
/delete: Remove a product.
/view: View product details.

3. Order Service: Oversees the order lifecycle, from creation to payment processing and tracking order status.
Endpoints:
/create_order: Create a new order.
/process_payment: Process payment for an order.
/track_order: Track the status of an order.

----------------------------------------------

Kubernetes Deployment (Manual)

Minikube start

kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/user-deployment.yaml
kubectl apply -f k8s/product-deployment.yaml
kubectl apply -f k8s/order-deployment.yaml
kubectl apply -f k8s/ingress.yaml

minikube status

kubectl get pods
kubectl get services
kubectl get ingress

minikube ip

*Edit /etc/hosts and add the following:
<minikube-ip> user.local
<minikube-ip> product.local
<minikube-ip> order.local

Check if Ingress is enabled:
minikube addons list
If not enabled, enable it:
minikube addons enable ingress

*kubectl get pods -n ingress-nginx

---------------------------------------------------------------------

Kubernetes Deployment (Script)

chmod+x deploy.sh
./deploy.sh

