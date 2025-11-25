# Binance Futures Trading Bot (Testnet)

## 🚀 Overview  
A modular and production-ready crypto trading bot built for Binance Futures **Testnet** using Python.  
It supports **Market, Limit, and Stop-Limit orders**, full logging, user input validation, and real API execution.

## ⚙️ Features Implemented
- ✔ Market & Limit Orders
- ✔ Buy / Sell Support
- ✔ Stop-Limit Order (Bonus Requirement)
- ✔ Logging of Requests, Responses & Errors
- ✔ Structured CLI with Validation
- ✔ Modular, Reusable Codebase
- ✔ Error Handling (Margin, Invalid Symbol, Timestamp, Pricing Errors)

## 🏗 Architecture

binance-futures-bot/
│
├── bot/
│   ├── __init__.py
│   ├── basic_bot.py          # Core trading logic (Market, Limit, Stop-Limit)
│   ├── client_factory.py     # Creates Binance Futures client (Testnet)
│   ├── cli.py                # Handles user input & command-line workflow
│   ├── config.py             # Environment variable loader
│   └── logger.py             # Logging helper (API requests, responses, errors)
│
├── logs/
│   ├── bot.log               # Real trade logs (API errors + success)
│   └── bot_copy.txt          # Backup log file
│
├── main.py                   # Entry file – run the trading bot (CLI)
├── requirements.txt          # Minimal dependencies for assignment
├── .env.example              # Example (Do NOT upload real keys)
└── README.md                 # Project documentation



## 📦 Setup & Installation

```bash
git clone https://github.com/Chiragadve/binance-future-bot
cd binance-future-bot
python -m venv venv
venv\Scripts\activate       # on Windows
pip install -r requirements.txt


BINANCE_API_KEY=your_key_here
BINANCE_API_SECRET=your_secret_here
USE_TESTNET=True

python main.py

## 📸 Screenshots

### 1. User Interface – Order Input  
Shows trading pair, side, quantity, and order type selection.  
![Screenshot 1](screenshots/screenshot1.png)

### 2. Order Successfully Executed  
Successful Market / Limit order executed on Binance Testnet.  
![Screenshot 2](screenshots/screenshot2.png)

### 3. Error Handling & Logging  
Timestamp error / insufficient margin / invalid price handling.  
This proves logging and API error management.
![Screenshot 3](screenshots/screenshot3.png)
