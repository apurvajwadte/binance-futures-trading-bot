def validate_side(side):
    valid_sides = ["BUY", "SELL"]

    if side.upper() not in valid_sides:
        raise ValueError("Side must be BUY or SELL")

    return side.upper()


def validate_order_type(order_type):
    valid_types = ["MARKET", "LIMIT"]

    if order_type.upper() not in valid_types:
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type.upper()


def validate_quantity(quantity):
    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity