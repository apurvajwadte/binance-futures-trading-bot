import argparse

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:

        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        if order_type == "LIMIT" and not args.price:
            raise ValueError("Price is required for LIMIT orders")

        order = place_order(
            symbol=args.symbol.upper(),
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=args.price
        )

        print("\n===== ORDER SUCCESS =====")
        print(f"Symbol      : {order['symbol']}")
        print(f"Side        : {order['side']}")
        print(f"Order Type  : {order['type']}")
        print(f"Quantity    : {order['quantity']}")
        print(f"Price       : {order['price']}")
        print(f"Status      : {order['status']}")

    except Exception as e:
        print(f"\nError: {str(e)}")


if __name__ == "__main__":
    main()