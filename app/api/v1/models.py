from flask import make_response, jsonify, request
from flask_jwt_extended import create_access_token
from flask_restful import reqparse

products = [] # a list to contain all the products
sales = [] # A list of all sale records
users = [] #a list of users


"""Required details for login"""
required = reqparse.RequestParser()
required.add_argument('email', help = "You should enter you email to login", required = True)
required.add_argument('password',help = "Password required to continue", required = True)

class Sales():
    """" Initialize a sales description"""
    def __init__(self, product_id, quantity, sales_price, sales_date):
        self.product_id = product_id
        self.sales_id = len(sales)+1
        self.quantity = quantity
        self.sales_date = sales_date
        self.amount = sales_price

    """ Create a product sale."""
    def make_a_sale_object(self):
        sale = {
            "sales_id" : self.sales_id,
            "product_id" : self.product_id,
            "quantity" : self.quantity,
            "sales_amount" : self.amount,
            "sales_date" : self.sales_date
        }
        return sale

    def get_one_sale_record(self, id):
        if id<=len(sales) and id!=0:
            for s in sales:
                if s["sales_id"] == id:
                    return make_response(jsonify({
                        "sales Order" : s
                    }), 200)
        else:
            return make_response(jsonify({
                "Message" : "The sales order is not available"
            }), 404)

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
class Users:
    """ Initialize the user """
    def __init__(self, username, email, password, role):
        self.userid = len(users)+1
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def create_user(self):
        user = {
            "userid": self.userid,
            "username" : self.username,
            "email" : self.email,
            "password" : self.password,
            "role" : self.role
        }
        return user
    
    def filter_user_detail(self,email):
        user = [user for user in users if user['email']==email]
        return user

    def userlogin(self,email,password):
        
        registered_user = Users.filter_user_detail(self,email) #check whether the iser is registered
        if not registered_user:
            return make_response(jsonify({
                "Message" : "{} is not a registered user".format(email)
            }))

        if registered_user[0]['password'] == password: #check user password
            return Processess.generate_auth_token(self, registered_user[0]['role']) #generate auth token
        else:
            return make_response(jsonify({
                "Message" : "Incorrect Password"
            }))
    
class Processess:

    """Process to create a sale record"""
    def make_a_sale(self):
        self.data = request.get_json()
        self.p_id = self.data['product_id']
        self.quant = self.data['quantity']
        self.s_amt = self.data['sales_amount']
        self.s_date = self.data['sales_date']

        #check whether the product is in store and in stock
        for product in products:
            if product['product_id']==self.p_id and product['quantity']>self.quant:
                # create one sale order
                sale = Sales(self.p_id,self.quant,self.s_amt,self.s_date).make_a_sale_object()

                # add to the sales list and return it
                sales.append(sale)
                return make_response(jsonify({
                    "sales" : sales
                }), 201)
            else:
                return make_response(jsonify({ "Message" : "Product requested not in store"}),404)


    def generate_auth_token(self,role):
        auth_token = create_access_token(identity = role)
        return auth_token

    