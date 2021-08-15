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
