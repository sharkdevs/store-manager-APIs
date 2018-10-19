from flask import make_response, jsonify

products = [] # a list to contain all the products
sales = [] # A list of all sale records

class Sales():
    """" Initialize a sales description"""
    def __init__(self, sales_id, product_id, quantity, sales_price, sales_date):
        self.product_id = product_id
        self.sales_id = sales_id
        self.quantity = quantity
        self.sales_date = sales_date
        self.amount = sales_price

    """ Create a product sale."""
    def make_a_sale(self):
        sale = {
            "sales_id" : self.sales_id,
            "product_id" : self.product_id,
            "quantity" : self.quantity,
            "sales_amount" : self.amount,
            "sales_date" : self.sales_date
        }
        return sale

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
        if id<=len(products) and id!=0:
            for p in products:
                if p["product_id"] == id:
                    return make_response(jsonify({
                        "product" : p
                    }), 200)
        else:
            return make_response(jsonify({
                "Message" : "The product requested is not in store"
            }), 404)