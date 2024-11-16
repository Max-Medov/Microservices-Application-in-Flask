from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import uuid
import json

app = Flask(__name__)

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@postgres-db:5432/mydb')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Order model
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.String(36), primary_key=True)  # UUID
    products = db.Column(db.Text, nullable=False)  # JSON string
    status = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.get_json()
    products = data.get('products')
    if not products:
        return jsonify({'message': 'No products provided.'}), 400
    order_id = str(uuid.uuid4())
    new_order = Order(
        id=order_id,
        products=json.dumps(products),
        status='pending',
        payment_status='unpaid'
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully.', 'order_id': order_id}), 201

@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    order_id = data.get('order_id')
    payment_method = data.get('payment_method')
    if not order_id or not payment_method:
        return jsonify({'message': 'Order ID and payment method are required.'}), 400
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found.'}), 404
    order.payment_status = 'paid'
    order.status = 'processing'
    db.session.commit()
    return jsonify({'message': 'Payment processed successfully.', 'order_id': order_id}), 200

@app.route('/track_order/<order_id>', methods=['GET'])
def track_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found.'}), 404
    return jsonify({
        'order_id': order.id,
        'status': order.status,
        'payment_status': order.payment_status,
        'products': json.loads(order.products)
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

