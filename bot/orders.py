from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(symbol, side, order_type, quantity, price=None):

    logger.info(
        f"Order Request -> Symbol: {symbol}, "
        f"Side: {side}, Type: {order_type}, "
        f"Quantity: {quantity}, Price: {price}"
    )

    try:

        order_response = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price,
            "status": "SUCCESS"
        }

        logger.info(f"Order Response -> {order_response}")

        return order_response

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise