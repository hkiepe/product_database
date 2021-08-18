from inkontor_resources.classes.parcel import Parcel


# Class Product is child class from Parcel. They have an additional parcels array because they can hold diffrerent
# parcels which build the product.
class Product(Parcel):

    def __init__(self, sku, name):
        super().__init__(sku, name)
        self.parcels = []

    # adds a parcel to parcels array
    def add_parcel(self, parcel, product):
        self.parcels.append(parcel)
        parcel.update_parcels(product)

    # provide information which parcels the product holds
    def show_parcels(self):
        print(f'Product {self.name}, sku: {self.sku}, weight: {self.weight} has sub-parcels:')
        for parcel in self.parcels:
            print(f' - Sku: {parcel.sku}, Parcel name: {parcel.name}, Parcel weight {parcel.weight}')

    # Sets the weight for the products by summing up the weight of each sub parcel
    def update_weight(self):
        self.weight = 0
        for parcel in self.parcels:
            self.weight = self.weight + parcel.weight

    def update_price(self):
        self.prices = {}
        for parcel in self.parcels:
            for price in parcel.prices:
                if not self.weight_out_of_range:
                    self.prices[price] = self.prices.get(price, 0) + parcel.prices[price]
                else:
                    self.prices[price] = 0


# Test the classes ...
# if __name__ == '__main__':
