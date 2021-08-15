# Class Parcel is the parent class. Each parcel has an sku and a weight
class Parcel:

    def __init__(self, sku, name):
        self.sku = sku
        self.name = name
        self.weight = 0
        self.products = []
        self.prices = []

    # provide basic product or parcel info
    def get_info(self):
        print(f'sku: {self.sku}, Product name: {self.name}, Weight: {self.weight} kg')

    # sets the weight for the parcel or the product
    def set_weight(self, weight):
        self.weight = weight
        # call set weight in each product of products list
        for product in self.products:
            product.update_weight()

    def update_parcels(self, product):
        self.products.append(product)
        print(f'Parcel {self.sku} is present in the following products:')
        for product in self.products:
            print(product.sku)