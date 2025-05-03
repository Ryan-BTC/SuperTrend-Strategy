# SuperTrend strategy using Backtrader

This project is a Python-based project that uses the Backtrader library for backtesting SuperTrend Strategy.

## 🛠️ Dependencies
Install dependencies via pip:

<pre>pip install backtrader pandas matplotlib</pre>


## Features
- Backtesting trading strategies
- Indicators: 
  - Currently, SuperTrend. 
  - More to come...

  
This repository provides a backtesting framework for testing and simulating cryptocurrency trading strategies using historical data.

<b>Note:</b> This project is only for backtesting purposes and does not execute live trades.

<b>Features Backtesting:</b> Simulate SuperTrend trading strategy using historical OHLCV data.

<B>Logging:</B> Comprehensive logging of backtest results for analysis.

# Methodology 

Primarily I executed BTC_OHLCV_Supertrend_transformation.py before running this backtest. This will add the signal from our SuperTrend strategy. 
The csv file containing the SuperTrend signals are saved within the data/SuperTrend directory.

## Configuration File Setup for Backtesting
Before running the backtest, you need to set up the configuration file. This file contains settings such as the path to your historical data.

## Important Notes
This repository does not include sensitive files such as API keys or large historical data. 
You'll need to provide a config.py file with the following structure:

<pre># File paths for each timeframe
btc_15m_supertrend = 'path/to/btc_15m.csv'
btc_1h_supertrend = 'path/to/btc_1h.csv'
btc_4h_supertrend = 'path/to/btc_4h.csv'
btc_1d_supertrend = 'path/to/btc_1d.csv'

# Output files
SuperTrend_vs_BTC_Benchmark_4h_returns = 'outputs/supertrend_vs_btc_4h.csv'
SuperTrend_Visuals_4h = 'outputs/supertrend_4h_chart.png'</pre>

⚠️ Keep config.py excluded from version control using .gitignore, especially if it contains sensitive paths or keys.

<b>API Keys:</b> This project does not require API keys or secrets, as it is focused on backtesting with historical data.
<b>Security:</b> Your API keys or any other sensitive information should never be stored in this repository. Keep them in secure, external configuration files or environment variables (if using live trading).


## Running with Different Timeframes
To run the strategy on a different timeframe, change the timeframe variable in the main script:

<pre>
timeframe = '4h'  # Options: '15m', '1h', '4h', '1d'
</pre>

Make sure the corresponding path is correctly defined in config.py with the format:

<pre>
btc_{timeframe}_supertrend
</pre>

For example, for timeframe = '1h', ensure config.btc_1h_supertrend exists.


# 📊 Results & Outputs
After running the backtest, the script generates:

✅ A CSV file containing:

- The daily returns of the Supertrend strategy
- The BTC benchmark returns over the same period
- Both indexed by date and ready for further analysis


<pre>SuperTrend_vs_BTC_Benchmark_4h_returns = 'outputs/supertrend_vs_btc_4h.csv'</pre>

This CSV is designed to be used in the Portfolio Analytics project, where you can:

Assess performance metrics (e.g., Sharpe, Sortino ratios)

## Plot cumulative returns

Analyze strategy vs benchmark visually

### 📈 A PNG chart showing:

- Trade entries and exits
- Portfolio equity curve over time

<pre>SuperTrend_Visuals_4h = 'outputs/supertrend_4h_chart.png'</pre>


✅ Conclusion
Based on the backtest results:

The initial portfolio value was set at $1,000,000.

Among the tested timeframes, the 4-hour (4h) strategy delivered the strongest performance.

By the end of the test period, the Supertrend strategy on the 4h timeframe grew the portfolio to approximately $19.8 million.

This highlights the potential effectiveness of trend-following strategies like Supertrend on mid-term timeframes when tuned and backtested properly.

Use these results to further evaluate robustness, risk metrics, and integrate with your Portfolio Analytics workflow for deeper insights.