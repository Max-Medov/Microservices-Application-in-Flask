****The system divided into three microservices, each responsible for a specific domain of functionality:****


**User Service:** Manages user-related operations, including registration, authentication, and profile updates.
Endpoints:
/register: Register a new user.
/login: Authenticate a user.
/profile: Retrieve or update user profile.

**Product Service:** Handles all product-related operations, such as managing product inventory and viewing details.
Endpoints:
/add: Add a new product.
/delete: Remove a product.
/view: View product details.

**Order Service:** Oversees the order lifecycle, from creation to payment processing and tracking order status.
Endpoints:
/create_order: Create a new order.
/process_payment: Process payment for an order.
/track_order: Track the status of an order.

----------------------------------------------

****Kubernetes Deployment (Manual)****

Git clone https://github.com/Max-Medov/Microservices-Application-in-Flask.git

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

kubectl get pods -n ingress-nginx

---------------------------------------------------------------------

****Kubernetes Deployment (Script)****

Git clone https://github.com/Max-Medov/Microservices-Application-in-Flask.git


chmod+x deploy.sh

./deploy.sh

Kubernetes Cleanup (Script)

--

chmod+x clenup.sh

./clenup.sh


----------------------------------------------------------------------

****Testing the Microservices****

**User Service**

**Register a User:**

curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser","password":"testpass"}' http://user.local/register





**Login a User:**

curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser","password":"testpass"}' http://user.local/login




**View a User:**

curl http://user.local/profile





**Product Service**

**Add a Product:**

curl -X POST -H "Content-Type: application/json" -d '{"name": "Product A", "price": 29.99}' http://product.local/add




**View a Product:**

curl http://product.local/view/1



**Delete a Product:**

curl -X DELETE http://product.local/delete/1





**Order Service**

Add a Products:
curl -X POST -H "Content-Type: application/json" -d '{"name": "Product A", "price": 36}' http://product.local/add
curl -X POST -H "Content-Type: application/json" -d '{"name": "Product B", "price": 25.5}' http://product.local/add




**Create an order:**

curl -X POST -H "Content-Type: application/json" -d '{
  "products": [
    {"id": "2", "quantity": 2},
    {"id": "3", "quantity": 1}
  ]
}' http://order.local/create_order




**Process Payment:**

curl -X POST -H "Content-Type: application/json" -d '{"order_id": "<order-id>", "payment_method": "credit_card"}' http://order.local/process_payment



**Track an order:**

curl http://order.local/track_order/<order-id>




