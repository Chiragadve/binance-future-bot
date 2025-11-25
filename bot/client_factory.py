from binance import Client
from .config import BINANCE_API_KEY, BINANCE_API_SECRET, USE_TESTNET, FUTURES_TESTNET_URL

def create_futures_client():
    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=USE_TESTNET)
    client.FUTURES_URL = FUTURES_TESTNET_URL
    return client