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
│── bot/
│ │── basic_bot.py
│ │── client_factory.py
│ │── logger.py
│ │── cli.py
│ └── config.py
│
│── logs/ ← Contains trade logs
│── main.py ← CLI entry point
│── requirements.txt
└── README.md


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

Screenshots
<img width="1919" height="949" alt="image" src="https://github.com/user-attachments/assets/a6a4d435-d15d-4125-8be2-e7448ed7a46d" />
<img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/675ccd33-ed14-4a82-8dd9-d023141618ae" />
<img width="1919" height="1028" alt="image" src="https://github.com/user-attachments/assets/684c52fe-87b4-4dbb-8b30-a00fe00e9d4a" />
