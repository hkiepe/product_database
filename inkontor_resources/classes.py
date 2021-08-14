# Class Parcel is the parent class. Each parcel has an sku and a weight
class Parcel:

    def __init__(self, sku, name):
        self.sku = sku
        self.name = name
        self.weight = 0
        self.prices = []

    # provide basic product or parcel info
    def get_info(self):
        print(f'sku: {self.sku}, Product name: {self.name}, Weight: {self.weight} kg')

    # sets the weight for the parcel or the product
    def set_weight(self, weight):
        self.weight = weight


# Class Product is child class from Parcel. They have an additional parcels array because they can hold diffrerent
# parcels which build the product.
class Product(Parcel):

    def __init__(self, sku, name):
        super().__init__(sku, name)
        self.prices = []
        self.parcels = []

    # adds a parcel to parcels array
    def add_parcel(self, parcel):
        self.parcels.append(parcel)
        print(f'{parcel.sku} added to {self.name} (sku: {self.sku})!')

    # provide information which parcels the product holds
    def get_parcels(self):
        print(f'Product {self.name} (sku: {self.sku}) has sub-parcels:')
        for parcel in self.parcels:
            print(f' - Sku: {parcel.sku}, Parcel name: {parcel.name}')


# Test the classes ...
if __name__ == '__main__':
    product = Product('07.10.00.00', 'BERG XL Extra Blue BFR')
    parcel_1 = Parcel('07.50.00.01', 'BERG XL Frame BFR')
    parcel_2 = Parcel('07.55.00.00', 'BERG Extra Blue Theme (excl. XL Frame)')

    product.add_parcel(parcel_1)
    product.add_parcel(parcel_2)

    parcel_1.set_weight(31.49)
    parcel_2.set_weight(19.9)

    product.get_parcels()

    product.get_info()
    parcel_1.get_info()
    parcel_2.get_info()