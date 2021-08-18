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
    # read the whole first column in products array because we need it later to check if sub parcels are in
    # products array
    for i in range(3, sku_sheet.max_row + 1):
        if sku_sheet.cell(row=i, column=1).value not in products:
            products.append(sku_sheet.cell(row=i, column=1).value)
    # here we create the sub parcel array
    parcels = get_parcels_sku(project_path, parcels_file, parcels_workbook)
    # check if the sub parcels have a corresponding value in the product array. If not we raise an ValueError
    for parcel in parcels:
        if parcel not in products:
            raise ValueError(f'{parcel} has no values in source file')


# get all parcel sku from the file
def get_parcels_sku(project_path, parcels_file, parcels_workbook):
    os.chdir(project_path)
    sku_workbook = openpyxl.load_workbook(parcels_file)
    sku_sheet = sku_workbook[parcels_workbook]
    parcels_sku = []
    for i in range(3, sku_sheet.max_row + 1):
        for j in range(12, 18):
            # check and filter out unusable characters
            if sku_sheet.cell(row=i, column=j).value is not None and sku_sheet.cell(row=i, column=j).value != '-':
                # add sku to array and check for duplicates
                if sku_sheet.cell(row=i, column=j).value not in parcels_sku:
                    parcels_sku.append(sku_sheet.cell(row=i, column=j).value)
    return parcels_sku


# Read in all products into objects from the source file and create a products array with all product objects.
def read_in_all_products(project_path, parcels_file, parcels_workbook):
    os.chdir(project_path)
    sku_workbook = openpyxl.load_workbook(parcels_file)
    sku_sheet = sku_workbook[parcels_workbook]
    products = []
    parcels_sku = get_parcels_sku(project_path, parcels_file, parcels_workbook)
    # creates the products array with Products objects
    for i in range(3, sku_sheet.max_row + 1):
        # filter out sub parcel sku
        if sku_sheet.cell(row=i, column=1).value not in parcels_sku:
            products.append(Product(sku_sheet.cell(row=i, column=1).value, sku_sheet.cell(row=i, column=2).value))
    return products


# Read in all parcels to the parcel objects and create a parcels array with all parcels
def read_in_all_parcels(project_path, parcels_file, parcels_workbook):
    os.chdir(project_path)
    sku_workbook = openpyxl.load_workbook(parcels_file)
    sku_sheet = sku_workbook[parcels_workbook]
    # get all parcel sku from the file
    parcels_sku = get_parcels_sku(project_path, parcels_file, parcels_workbook)
    parcels = []
    # Iterate through the file and if a sub parcel sku matches with the value in the parcels_sku array we create an
    # instance of the Parcel object.
    for i in range(3, sku_sheet.max_row + 1):
        if sku_sheet.cell(row=i, column=1).value in parcels_sku:
            parcels.append(Parcel(sku_sheet.cell(row=i, column=1).value, sku_sheet.cell(row=i, column=2).value))
    return parcels
