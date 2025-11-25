from bot.client_factory import create_futures_client

client = create_futures_client()
print(client.futures_ping())
