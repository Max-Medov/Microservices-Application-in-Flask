from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@postgres-db:5432/mydb')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Product model
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/add', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    if not name or price is None:
        return jsonify({'message': 'Product name and price are required.'}), 400
    new_product = Product(name=name, price=price)
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully.', 'product_id': new_product.id}), 201

@app.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully.'}), 200
    else:
        return jsonify({'message': 'Product not found.'}), 404

@app.route('/view/<int:product_id>', methods=['GET'])
def view_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            'id': product.id,
            'name': product.name,
            'price': product.price
        }), 200
    else:
        return jsonify({'message': 'Product not found.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

