VALID_SIDES = {"BUY", "SELL"}
ORDER_TYPE_CHOICES = {
    "1": "MARKET",
    "2": "LIMIT",
    "3": "STOP_LIMIT",
}


def read_float(prompt: str) -> float:
    raw = input(prompt).strip()
    try:
        value = float(raw)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        raise ValueError(f"Invalid number: {raw}")


def read_side() -> str:
    side = input("Side [BUY/SELL]: ").strip().upper()
    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")
    return side


def print_order_summary(order: dict) -> None:
    if not isinstance(order, dict):
        print("Unexpected order response.")
        return

    print("\nOrder Summary")
    print("-" * 40)
    print(f"Order ID      : {order.get('orderId')}")
    print(f"Symbol        : {order.get('symbol')}")
    print(f"Side          : {order.get('side')}")
    print(f"Type          : {order.get('type')}")
    print(f"Status        : {order.get('status')}")
    print(f"Original Qty  : {order.get('origQty')}")
    print(f"Executed Qty  : {order.get('executedQty')}")
    print(f"Price         : {order.get('price')}")
    print(f"Average Price : {order.get('avgPrice')}")
    print(f"Update Time   : {order.get('updateTime')}")
    print("-" * 40)


def run_cli(bot):
    print("=== Binance Futures Testnet Trading Bot ===")

    while True:
        print("\nSelect order type:")
        print("  1) Market order")
        print("  2) Limit order")
        print("  3) Stop-limit order (advanced)")
        print("  Q) Quit")

        choice = input("Choice: ").strip().upper()
        if choice in {"Q", "QUIT", "EXIT"}:
            print("Exiting bot.")
            break

        order_type = ORDER_TYPE_CHOICES.get(choice)
        if order_type is None:
            print("Invalid choice. Please select 1, 2, 3 or Q.")
            continue

        try:
            symbol = input("Symbol (e.g. BTCUSDT): ").strip().upper()
            side = read_side()
            quantity = read_float("Quantity: ")

            if order_type == "MARKET":
                order = bot.place_market_order(symbol, side, quantity)

            elif order_type == "LIMIT":
                limit_price = read_float("Limit price: ")
                order = bot.place_limit_order(symbol, side, quantity, limit_price)

            else:  # STOP_LIMIT
                limit_price = read_float("Limit price: ")
                stop_price = read_float("Stop price (trigger): ")
                order = bot.place_stop_limit_order(symbol, side, quantity, limit_price, stop_price)

            print_order_summary(order)

        except Exception as exc:
            print(f"Error: {exc}")
