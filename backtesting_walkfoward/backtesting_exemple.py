from backtesting_walkfoward.backtesting import Backtesting
import numpy as np
import pandas as pd


def moving_avarange(data_class, x, y):
    df = data_class.dataframe.copy()
    ma_fast = np.array(df.close.rolling(x).mean())
    ma_slow = np.array(df.close.rolling(y).mean())

    return {'ma_fast': ma_fast, 'ma_slow': ma_slow}


def buy_enter_ma(data_class):
    mf = data_class.indicators['ma_fast']
    ms = data_class.indicators['ma_slow']
    op = data_class.open
    be = np.zeros(len(mf))

    for i in range(len(be)):
        if i < 2 or not mf[i] or not ms[i]:
            continue
        if mf[i - 2] <= ms[i - 2] and mf[i - 1] > ms[i - 1]:
            be[i] = op[i]

    return be


def sell_enter_ma(data_class):
    mf = data_class.indicators['ma_fast']
    ms = data_class.indicators['ma_slow']
    op = data_class.open
    se = np.zeros(len(mf))

    for i in range(len(se)):
        if i < 2 or not mf[i] or not ms[i]:
            continue
        if mf[i - 2] >= ms[i - 2] and mf[i - 1] < ms[i - 1]:
            se[i] = op[i]

    return se


if __name__ == '__main__':
    path = 'MSFT.csv'
    df_msft = pd.read_csv(path)

    backtesting = Backtesting(df_msft)
    backtesting.indicator(moving_avarange, 12, 200)
    backtesting.buy_enter(buy_enter_ma)
    backtesting.sell_enter(sell_enter_ma)
    backtesting.backtesting(revert=True)

    metrics_results = backtesting.results()

    backtesting.data_class.plot_bokeh_indicators(
        line_indicators={'ma_fast': 'blue', 'ma_slow': 'yellow'},
        circle_indicators={'buy_enter_price': 'green', 'sell_enter_price': 'red'}
    )
