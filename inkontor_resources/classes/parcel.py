# Class Parcel is the parent class. Each parcel has an sku and a weight
class Parcel:

    def __init__(self, sku, name):
        self.sku = sku
        self.name = name
        self.weight = 0
        self.products = []
        self.prices = {}
        self.weight_out_of_range = False

    # provide basic product or parcel info
    def show_info(self):
        print(f'sku: {self.sku}, Product name: {self.name}, Weight: {self.weight} kg')

    # sets the weight for the parcel or the product
    def set_weight(self, weight):
        self.weight = weight
        # call set weight in each product of products list
        for product in self.products:
            product.update_weight()

    def update_out_of_range(self):
        self.weight_out_of_range = True
        for product in self.products:
            product.update_out_of_range()

    def update_parcels(self, product):
        self.products.append(product)

    # gets a price dictionary with value pairs {'country': price}. If price out of range is set, price is 0
    def set_price(self, prices):
        self.prices = prices
        # call update price in each product of products list
        for product in self.products:
            product.update_price()
