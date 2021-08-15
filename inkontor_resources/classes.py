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


# Class Product is child class from Parcel. They have an additional parcels array because they can hold diffrerent
# parcels which build the product.
class Product(Parcel):

    def __init__(self, sku, name):
        super().__init__(sku, name)
        weight = 0
        self.prices = []
        self.parcels = []

    # adds a parcel to parcels array
    def add_parcel(self, parcel, product):
        self.parcels.append(parcel)
        parcel.update_parcels(product)
        print(f'{parcel.sku} added to {self.name} (sku: {self.sku})!')

    # provide information which parcels the product holds
    def get_parcels(self):
        print(f'Product {self.name} (sku: {self.sku}) has sub-parcels:')
        for parcel in self.parcels:
            print(f' - Sku: {parcel.sku}, Parcel name: {parcel.name}')

    # Sets the weight for the products by summing up the weight of each parcel
    def update_weight(self):
        self.weight = 0
        for parcel in self.parcels:
            self.weight = self.weight + parcel.weight


# Test the classes ...
# if __name__ == '__main__':
