import streamlit as st
from bot.client_factory import create_futures_client
from bot.basic_bot import BasicBot

# Initialize client & bot
try:
    client = create_futures_client()
    bot = BasicBot(client)
except Exception as e:
    st.error(f"Failed to initialize Binance client: {e}")
    st.stop()

st.title("Binance Futures Testnet Trading Bot")

# Symbol & side selection
symbol = st.text_input("Trading Pair (e.g., BTCUSDT)", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
quantity = st.number_input("Quantity", min_value=0.001, value=0.01)

# Order type selection
order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT", "STOP_LIMIT"]
)

# Extra fields for LIMIT / STOP_LIMIT
price = None
stop_price = None

if order_type in ["LIMIT", "STOP_LIMIT"]:
    price = st.number_input("Limit Price", min_value=0.001)

if order_type == "STOP_LIMIT":
    stop_price = st.number_input("Stop Price (Trigger)", min_value=0.001)

# Place order
if st.button("Place Order"):
    try:
        if order_type == "MARKET":
            response = bot.place_market_order(symbol, side, quantity)

        elif order_type == "LIMIT":
            response = bot.place_limit_order(symbol, side, quantity, price)

        elif order_type == "STOP_LIMIT":
            response = bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)

        st.success("Order Sent Successfully!")
        st.subheader("Response:")
        st.json(response)

    except Exception as e:
        st.error(f"Error: {e}")