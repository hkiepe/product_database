from inkontor_resources.classes import Parcel, Product


if __name__ == '__main__':
    product_1 = Product('07.10.00.00', 'BERG XL Extra Blue BFR')
    # Todo: Check if product already exists by comparing the sku's of all products'
    product_2 = Product('07.10.01.00', 'BERG XL Extra Sport Blue BFR')
    parcel_1 = Parcel('07.50.00.01', 'BERG XL Frame BFR')
    parcel_2 = Parcel('07.55.00.00', 'BERG Extra Blue Theme (excl. XL Frame)')
    parcel_3 = Parcel('07.55.00.01', 'BERG Extra Sport Blue Theme (excl. XL Frame)')

    product_1.add_parcel(parcel_1, product_1)
    product_1.add_parcel(parcel_2, product_1)
    product_2.add_parcel(parcel_1, product_2)
    product_2.add_parcel(parcel_3, product_2)

    parcel_1.set_weight(31.49)
    parcel_2.set_weight(19.9)
    parcel_3.set_weight(20.6)

    print(f'Weight of product {product_1.sku} is {product_1.weight} kg')
    print(f'Weight of product {product_2.sku} is {product_2.weight} kg')

    # product.get_parcels()

    # product.get_info()
    # parcel_1.get_info()
    # parcel_2.get_info()
