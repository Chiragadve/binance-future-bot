from bot.client_factory import create_futures_client
from bot.basic_bot import BasicBot
from bot.cli import run_cli

def main():
    client = create_futures_client()
    bot = BasicBot(client)
    run_cli(bot)

if __name__ == '__main__':
    main()