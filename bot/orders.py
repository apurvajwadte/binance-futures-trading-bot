from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger()

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):

    try:

        logger.info(
            f"Order Request -> Symbol: {symbol}, "
            f"Side: {side}, Type: {order_type}, "
            f"Quantity: {quantity}, Price: {price}"
        )

        if order_type == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type == "LIMIT":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Order Response -> {order}")

        return order

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise