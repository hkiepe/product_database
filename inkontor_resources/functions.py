import openpyxl, os, math
from inkontor_resources.classes.product import Product
from inkontor_resources.classes.parcel import Parcel


# todo maybe this check should be included in the parcel class better?
def check_weight(value, parcel):
    if isinstance(value, str):
        raise ValueError(f'weight cant be a string for parcel {parcel.sku}')
        return False
    if value == 0:
        raise ValueError(f'weight cant be 0 for parcel {parcel.sku}')
        return False
    else:
        return value


# Check if all sub parcels have a corresponding product if not it will raise value error.
def check_sub_parcels(project_path, parcels_file, parcels_workbook):
    os.chdir(project_path)
    sku_workbook = openpyxl.load_workbook(parcels_file)
    sku_sheet = sku_workbook[parcels_workbook]
    products = []
    parcels = []
    # iterate the source and create an array with all sub parcels
    for i in range(3, sku_sheet.max_row + 1):
        # read the whole first column in products array because we need it later to check if sub parcels are in
        # products array
        if sku_sheet.cell(row=i, column=1).value not in products:
            products.append(sku_sheet.cell(row=i, column=1).value)
        # here we create the sub parcel array
        for j in range(12, 18):
            if sku_sheet.cell(row=i, column=j).value is not None and sku_sheet.cell(row=i, column=j).value != '-':
                if sku_sheet.cell(row=i, column=j).value not in parcels:
                    parcels.append(sku_sheet.cell(row=i, column=j).value)
    # check if the sub parcels have a corresponding value in the product array. If not we raise an ValueError
    for parcel in parcels:
        if parcel not in products:
            raise ValueError(f'{parcel} has no values in source file')


# Read in all products into objects from the source file and create a products array with all product objects.
def read_in_all_products(project_path, parcels_file, parcels_workbook):
    os.chdir(project_path)
    sku_workbook = openpyxl.load_workbook(parcels_file)
    sku_sheet = sku_workbook[parcels_workbook]
    products = []
    # creates the products array with Products objects
    for i in range(3, sku_sheet.max_row + 1):
        products.append(Product(sku_sheet.cell(row=i, column=1).value, sku_sheet.cell(row=i, column=2).value))
    return products


# Read in all parcels to the parcel objects and create a parcels array with all parcels
def read_in_all_parcels(project_path, parcels_file, parcels_workbook):
    os.chdir(project_path)
    sku_workbook = openpyxl.load_workbook(parcels_file)
    sku_sheet = sku_workbook[parcels_workbook]
    parcels_sku = []
    parcels = []
    # First we grab all the sub parcels sku in one array. Then we iterate the array to create the sub parcels with
    # values from source file
    for i in range(3, sku_sheet.max_row + 1):
        # here we create the parcels_sku array
        for j in range(12, 18):
            if sku_sheet.cell(row=i, column=j).value is not None and sku_sheet.cell(row=i, column=j).value != '-':
                if sku_sheet.cell(row=i, column=j).value not in parcels_sku:
                    parcels_sku.append(sku_sheet.cell(row=i, column=j).value)
    # now we iterate through the source file and when we find an sku which is also in parcels_sku array we create the
    # parcel object.
    for i in range(3, sku_sheet.max_row + 1):
        if sku_sheet.cell(row=i, column=1).value in parcels_sku:
            parcels.append(Parcel(sku_sheet.cell(row=i, column=1).value, sku_sheet.cell(row=i, column=2).value))
    return parcels
