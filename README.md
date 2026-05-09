# Binance Futures Testnet Trading Bot

## 📌 Project Overview
A Python-based CLI trading bot for Binance Futures Testnet that supports MARKET and LIMIT order placement with input validation, structured logging, and exception handling.

---

## 🚀 Features
- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- CLI-based user input
- Validation and error handling
- Logging to file
- Structured modular architecture

---

## 🛠 Technologies Used
- Python 3
- argparse
- logging
- dotenv

---

## 📂 Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .gitignore

---

## ▶️ Run Examples

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65000
```

---

## ✅ Validation Example

```bash
Error: Price is required for LIMIT orders
```

---

## 📄 Assumptions
- Binance Futures Testnet is used
- Logging is stored in logs/trading_bot.log
- Modular architecture is used for scalability