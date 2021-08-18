from inkontor_resources.functions import check_sub_parcels, read_in_all_products,read_in_all_parcels,\
    add_parcels_to_product, add_weight, create_prices, set_out_of_range, set_parcel_prices, set_product_prices,\
    create_excel
from inkontor_resources.constants import PROJECT_PATH, PARCELS_WORKBOOK, PARCELS_FILE, PRICE_FILE_GLS,\
    PRICE_WORKBOOK_GLS, SHEET, TARGET_FILE


if __name__ == '__main__':
    # Check if all sub parcels have a corresponding product in the Berg source file. If not it will raise ValueError.
    check_sub_parcels(PROJECT_PATH, PARCELS_FILE, PARCELS_WORKBOOK)

    # Read in all products into objects from the source file and create a products array with all product objects.
    products = read_in_all_products(PROJECT_PATH, PARCELS_FILE, PARCELS_WORKBOOK)

    # Read in all parcels to the parcel objects and create a parcels array with all parcels
    parcels = read_in_all_parcels(PROJECT_PATH, PARCELS_FILE, PARCELS_WORKBOOK)

    # Add parcels to product
    add_parcels_to_product(PROJECT_PATH, PARCELS_FILE, PARCELS_WORKBOOK, products, parcels)

    # Add weight to parcels and to products which don't have sub parcels
    add_weight(PROJECT_PATH, PARCELS_FILE, PARCELS_WORKBOOK, products, parcels)

    # Create the price instances from class PriceGls
    prices = create_prices(PROJECT_PATH, PRICE_FILE_GLS, PRICE_WORKBOOK_GLS)

    # Set 'parcel weight out of range' flag for parcels and products, if weight is too heavy for the parcel forwarder
    set_out_of_range(products, parcels)

    # Set prices for parcels and products without sub parcels, for all parcels and products, where out of range flag is
    # not set to True
    set_product_prices(products, prices)
    set_parcel_prices(parcels, prices)

    create_excel(products, SHEET, TARGET_FILE)

    # for product in products:
    #     print(f'Sku: {product.sku}, Name:{product.name}, Weight: {product.weight}, '
    #           f'Flag: {product.weight_out_of_range}')
    #     for parcel in product.parcels:
    #         print(f' - Sku: {parcel.sku}, Name: {parcel.name}, Weight: {parcel.weight},'
    #               f'Flag: {parcel.weight_out_of_range}')
    #         print(f' - {parcel.prices}')
    #     print(product.prices)
