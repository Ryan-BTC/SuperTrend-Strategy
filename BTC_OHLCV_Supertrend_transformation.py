import pandas as pd
import config
from Strategy.SuperTrend import super_trend


def main():
    df = pd.read_csv(config.btc_1d_csv,
                     usecols=['datetime', 'open', 'high', 'low', 'close', 'volume'],
                     parse_dates=['datetime'],
                     date_format='%d/%m/%Y %H:%M')

    super_trend_data = super_trend(df)
    super_trend_data.to_csv(config.btc_1d_supertrend, index=False)


if __name__ == "__main__":
    main()