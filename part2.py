#Part 2: Backend and API Development with Python

#Task: Create a Flask-based RESTful API to manage a collection of product information, supporting operations for adding, retrieving, updating, and deleting records.


# Import the Flask library for creating a web server
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Initialize an empty dictionary to store product data in memory
products = {}

# Route for adding a new product
@app.route('/product', methods=['POST'])
def add_product():
    # Parse the JSON data from the incoming request
    data = request.get_json()
    
    # Generate a unique ID for each product using the length of the dictionary
    product_id = len(products) + 1
    
    # Add the new product data to the dictionary with the generated ID as the key
    products[product_id] = data
    
    # Return a response with the newly created product and a 201 Created status code
    return jsonify({"id": product_id, "product": data}), 201

# Route for retrieving all products
@app.route('/products', methods=['GET'])
def get_products():
    # Return all products in the dictionary as a JSON response
    return jsonify(products), 200

# Route for retrieving a single product by ID
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Check if the product ID exists in the dictionary
    if product_id in products:
        # If found, return the product data
        return jsonify(products[product_id]), 200
    else:
        # If not found, return an error message with a 404 Not Found status code
        return jsonify({"error": "Product not found"}), 404

# Route for updating a product by ID
@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Check if the product exists in the dictionary
    if product_id in products:
        # Parse the JSON data from the request
        data = request.get_json()
        
        # Update the existing product with the new data
        products[product_id] = data
        
        # Return the updated product data
        return jsonify(products[product_id]), 200
    else:
        # Return an error if the product ID is not found
        return jsonify({"error": "Product not found"}), 404

# Route for deleting a product by ID
@app.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Check if the product exists
    if product_id in products:
        # Remove the product from the dictionary
        del products[product_id]
        
        # Return a success message
        return jsonify({"message": "Product deleted"}), 200
    else:
        # Return an error if the product ID is not found
        return jsonify({"error": "Product not found"}), 404

# Run the Flask application on port 5000 when the script is executed
if __name__ == '__main__':
    app.run(port=5000)
