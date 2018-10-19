from flask import make_response, jsonify

products = [] # a list to contain all the products
class Product():
    """" Initialize a product description"""
    def __init__(self, product_name, product_price, description, quantity, product_image):
        self.product_id = len(products)+1
        self.product_name = product_name
        self.product_price = product_price
        self.description = description
        self.quantity = quantity
        self.product_image = product_image

    """ Create a product."""
    def create_a_product(self):
        product = {
            "product_id" : self.product_id,
            "product_name" : self.product_name,
            "product_price" : self.product_price,
            "description" : self.description,
            "quantity" : self.quantity,
            "product_image" : self.product_image
        }
        return product
    def get_one_product(self,id):
        
        for p in products:
            if p["product_id"] == id:
                return make_response(jsonify({
                    "product" : p
                }), 200)
       