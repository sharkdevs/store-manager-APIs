from app.api.v1.models import products

class Product:
    """Get the list of products in the list"""
    def get(self):
        return products