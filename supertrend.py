import backtrader

class PandasDataFeed(backtrader.feeds.PandasData):
    lines = 'in_uptrend',
    params = (
        ('datetime', None),
        ('open', 'open'),
        ('high', 'high'),
        ('low', 'low'),
        ('close', 'close'),
        # Custom fields
        ('in_uptrend', 'in_uptrend'),
    )


class SuperTrend(backtrader.Strategy):
    # parms = dict(
    #     num_opening_bars=15
    # )

    def __init__(self):
        self.in_position = False
        self.order = None
        self.portfolio_values =[]

    def log(self, txt, dt=None):
        if dt is None:
            dt = self.datas[0].datetime.datetime()

        print('%s, %s' % (dt, txt))


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        if order.status in [order.Completed]:
            order_details = f"{order.executed.price}, Cost: {order.executed.value}, Comm {order.executed.comm}"

            if order.isbuy():
                self.log(f"BUY EXECUTED, Price: {order_details}")
            else:  # Sell
                self.log(f"SELL EXECUTED, Price: {order_details}")

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None


    def next(self):
        last_row_index = 0
        previous_row_index = -1
        self.portfolio_values.append(self.broker.getvalue())

        if not self.data.in_uptrend[previous_row_index] and self.data.in_uptrend[last_row_index]:
            print("Changed to uptrend, buy")

            if not self.getposition():
                order = self.buy()
            else:
                print("Already in position, nothing, to do")

        if self.data.in_uptrend[previous_row_index] and not self.data.in_uptrend[last_row_index]:
            print("Changed to downtrend, sell")

            if self.getposition():
                order = self.sell()
            else:
                print("You aren't in position nothing to Sell")


    def stop(self):
        self.log('(Ending Value %.2f' %
                 (self.broker.getvalue()))

        if self.broker.getvalue() > 130000:
            self.log("*** BIG WINNER ***")

        if self.broker.getvalue() < 70000:
            self.log("*** MAJOR LOSER ***")



