from inkontor_resources.classes import Parcel, Product


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
