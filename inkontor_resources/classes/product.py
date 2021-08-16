from inkontor_resources.classes.parcel import Parcel


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
        for parcel in self.parcels:
            print(f'parcel {parcel.sku} in {self.sku})!')

    # provide information which parcels the product holds
    def get_parcels(self):
        print(f'Product {self.name} (sku: {self.sku}) has sub-parcels:')
        for parcel in self.parcels:
            print(f' - Sku: {parcel.sku}, Parcel name: {parcel.name}')

    # Sets the weight for the products by summing up the weight of each sub parcel
    def update_weight(self):
        self.weight = 0
        for parcel in self.parcels:
            self.weight = self.weight + parcel.weight


# Test the classes ...
# if __name__ == '__main__':
