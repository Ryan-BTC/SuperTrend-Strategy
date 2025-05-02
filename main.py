import backtrader as bt
import pandas as pd
import config
from backtests.SuperTrend.supertrend import SuperTrend, PandasDataFeed


if __name__ == '__main__':
    timeframe = '4h'

    cerebro = bt.Cerebro()

    # Setting the Portfolio to 1000000
    cerebro.broker.setcash(1000000)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Position size of 95%
    cerebro.addsizer(bt.sizers.PercentSizer, percents=95)

    if timeframe == "15m":
        dataframe = pd.read_csv(
            config.btc_15m_supertrend,
            usecols=['datetime', 'open', 'high', 'low', 'close', 'volume', 'in_uptrend'],
            index_col='datetime',
            parse_dates=['datetime'],
            date_format='%d/%m/%Y %H:%M')
    elif timeframe == '1h':
        dataframe = pd.read_csv(
            config.btc_1h_supertrend,
            usecols=['datetime', 'open', 'high', 'low', 'close', 'volume', 'in_uptrend'],
            index_col='datetime',
            parse_dates=['datetime'],
            date_format='%d/%m/%Y %H:%M')
    elif timeframe == '4h':
        dataframe = pd.read_csv(
            config.btc_4h_supertrend,
            usecols=['datetime', 'open', 'high', 'low', 'close', 'volume', 'in_uptrend'],
            index_col='datetime',
            parse_dates=['datetime'],
            date_format='%d/%m/%Y %H:%M')
    elif timeframe == '1d':
        dataframe = pd.read_csv(
            config.btc_1d_supertrend,
            usecols=['datetime', 'open', 'high', 'low', 'close', 'volume', 'in_uptrend'],
            index_col='datetime',
            parse_dates=['datetime'],
            date_format='%d/%m/%Y')

    # Converting the datetime field to datetime
    dataframe.index = pd.to_datetime(dataframe.index)

    # Converting uptrend result from SuperTrend strategy into an integer values 1/0
    dataframe['in_uptrend'] = dataframe['in_uptrend'].astype(int)

    data = PandasDataFeed(dataname=dataframe)

    # Injecting the data to Cerebro for backtesting it
    cerebro.adddata(data)

    # Adding the strategy to Cerebro
    cerebro.addstrategy(SuperTrend)

    # Run backtrader
    cerebro.run()

    # Plot Chart with the positions executed and portfolio visualizations
    cerebro.plot()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())