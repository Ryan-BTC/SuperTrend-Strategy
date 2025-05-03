import backtrader as bt
import pandas as pd
import config
import matplotlib.pyplot as plt

from backtests.SuperTrend.supertrend import SuperTrend, PandasDataFeed


if __name__ == '__main__':
    timeframe = '1D'
    date_format = '%d/%m/%Y %H:%M' if timeframe != '1d' else '%d/%m/%Y'

    # Obtaining values from config file
    config_filepath_df      = f'btc_{timeframe}_supertrend'
    config_filepath_returns = f'SuperTrend_vs_BTC_Benchmark_{timeframe}_returns'
    config_filepath_charts  = f'SuperTrend_Visuals_{timeframe}'

    data_path           = getattr(config, config_filepath_df)
    data_path_returns   = getattr(config, config_filepath_returns)
    data_path_charts    = getattr(config, config_filepath_charts)

    cerebro = bt.Cerebro()

    # Setting the Portfolio to 1000000
    cerebro.broker.setcash(1000000)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Position size of 95%
    cerebro.addsizer(bt.sizers.PercentSizer, percents=95)

    dataframe = pd.read_csv(
        data_path,
        usecols=['datetime', 'open', 'high', 'low', 'close', 'volume', 'in_uptrend'],
        index_col='datetime',
        parse_dates=['datetime'],
        date_format=date_format)

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
    strats = cerebro.run()
    strategy_instance = strats[0]

    # Returns from the SuperTrend Strategy on Historical data
    returns = pd.Series(strategy_instance.portfolio_values, index=strategy_instance.dates)

    # Returns from the BTC Benchmark on Historical data 2018-01-01 to 2025-04-30
    btc_returns = dataframe['close'].pct_change().dropna()

    # Convert equity to returns
    strat_returns = returns.pct_change().dropna()

    # Combine both return series into a single DataFrame
    combined_returns = pd.DataFrame({
        'superTrend_return': strat_returns,
        'btc_return': btc_returns
    }, index=returns.index)


    combined_returns.dropna(inplace=True)

    # Reset index to move datetime from index to a column
    combined_returns = combined_returns.reset_index()

    # Rename the index column to something clear (e.g., 'datetime')
    combined_returns.rename(columns={'index': 'datetime'}, inplace=True)

    # Saving SuperTrend and BTC Benchmark returns
    combined_returns.to_csv(data_path_returns)

    # Plot Chart with the positions executed and portfolio visualizations
    figs = cerebro.plot()

    fig = figs[0][0]

    # Saving Chart for Visualization
    fig.savefig(data_path_charts)

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())