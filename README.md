# Crypto Trading Backtest: SMA Crossover Strategy

## Overview 📈
This repository provides a robust backtesting framework for a simple but effective **Simple Moving Average (SMA) Crossover Trading Strategy** on cryptocurrency markets. The strategy dynamically allocates capital based on trend signals and includes transaction cost considerations for a realistic performance evaluation.

## Features 🔥
- **Fetch Historical Data** 📡: Retrieves OHLCV data from the **Coinbase API**.
- **Technical Indicators** 📊: Implements **Simple Moving Averages (SMA)**, Weighted Moving Averages (WMA), and **Highpass/Lowpass filters**.
- **Signal Generation** 🚦: Identifies **Golden Cross (Buy)** and **Death Cross (Sell)** signals.
- **Dynamic Backtesting** 🏦: Simulates trading with dynamic capital allocation and transaction costs.
- **Performance Visualization** 📉: Generates **candlestick charts**, SMA overlays, and **equity performance plots**.

## How It Works ⚙️
### 1️⃣ Fetch Historical Data
```python
fetch_historical_data(base_curr="BTC", quote_curr="USDT", start_time="2021-01-01", end_time="2025-03-15")
```
- Retrieves daily OHLCV (Open, High, Low, Close, Volume) data from **Coinbase**.
- Data is stored in a Pandas DataFrame for easy analysis.

### 2️⃣ Compute SMA Crossover Signals
```python
df = sma_crossing_signals(df, short_window=20, long_window=60)
```
- Calculates **20-day SMA** and **60-day SMA**.
- Generates crossover signals for entry (buy) and exit (sell) points.

### 3️⃣ Backtest Trading Strategy
```python
df = backtest_trading_strategy(df, cash_to_invest=10000, transaction_cash_ratio=0.5, transaction_cost=0.001)
```
- **Initial Capital**: $10,000
- **Allocation**: 50% of cash on buy signals.
- **Sell**: Exit all holdings on a sell signal.
- **Transaction Cost**: 0.1% per trade.

### 4️⃣ Visualize Performance
```python
plot_chart(df)
```
- **Candlestick Chart** with SMA overlays.
- **Total Equity & Cash Balance** over time.
- **Buy & Sell Markers** on price movements.

## Example Results 🚀
```
The final equity is: 15149.23 USD
The total return is: 51.49%
```
The backtest demonstrates a **+51.49% return** using historical BTC/USDT data. 📈

## Installation & Dependencies 🛠️
```bash
pip install numpy pandas scipy matplotlib mplfinance requests
```

## Future Enhancements 🚀
- Add **Exponential Moving Averages (EMA)**.
- Implement **Risk Management** and Stop-loss mechanisms.
- Extend support for additional cryptocurrency exchanges.

## Contributing 🤝
Got ideas? Found a bug? Open an **issue** or submit a **pull request**!

## License 📜
MIT License - Free to use and modify!
