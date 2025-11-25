from binance.exceptions import BinanceAPIException, BinanceOrderException
from .logger import get_logger

logger = get_logger(__name__)


class BasicBot:
    """
    Basic trading bot for Binance USDT-M Futures Testnet.
    Supports market, limit and stop-limit orders on both buy and sell sides.
    """

    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol: str, side: str, quantity: float):
        params = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
        }
        logger.info("Market order request: %s", params)
        try:
            response = self.client.futures_create_order(**params)
            logger.info("Market order response: %s", response)
            return response
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error("Market order failed", exc_info=True)
            raise

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        params = {
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": quantity,
            "price": price,
        }
        logger.info("Limit order request: %s", params)
        try:
            response = self.client.futures_create_order(**params)
            logger.info("Limit order response: %s", response)
            return response
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error("Limit order failed", exc_info=True)
            raise

    def place_stop_limit_order(self, symbol: str, side: str, quantity: float, price: float, stop_price: float):
        """
        Stop-limit order on futures:
        Triggers when stop_price is reached, then submits a limit order at price.
        """
        params = {
            "symbol": symbol,
            "side": side,
            "type": "STOP",
            "timeInForce": "GTC",
            "quantity": quantity,
            "price": price,
            "stopPrice": stop_price,
        }
        logger.info("Stop-limit order request: %s", params)
        try:
            response = self.client.futures_create_order(**params)
            logger.info("Stop-limit order response: %s", response)
            return response
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error("Stop-limit order failed", exc_info=True)
            raise
