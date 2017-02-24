from datetime import time

from pandas import Timedelta, Timestamp
from pandas.tseries.holiday import GoodFriday
from pytz import timezone

from zipline.utils.calendars import TradingCalendar
from zipline.utils.calendars.trading_calendar import (
    end_default
)

# Number of hours of offset between the open and close times dictated by this
# calendar versus the 6:31am to 5:00pm times over which we want to simulate
# futures algos.
FUTURES_OPEN_TIME_OFFSET = 24
FUTURES_CLOSE_TIME_OFFSET = 0


class CryptocurrencyCalendar(TradingCalendar):
    """Synthetic calendar for trading cryptocurrencies.
    """
    # XXX: Override the default TradingCalendar start and end dates with ones
    # further in the future. This is a stopgap for memory issues caused by
    # upgrading to pandas 18. This calendar is the most severely affected,
    # since it has the most total minutes of any of the zipline calendars.
    def __init__(self,
                 start=Timestamp('2000-01-01', tz='UTC'),
                 end=end_default):
        super(QuantopianUSFuturesCalendar, self).__init__(start=start, end=end)

    @property
    def name(self):
        return "cryptocurrencies"

    @property
    def tz(self):
        return timezone('US/Eastern')

    @property
    def open_time(self):
        return time(18, 1)

    @property
    def close_time(self):
        return time(18)

    @property
    def open_offset(self):
        return 0

    def execution_time_from_open(self, open_dates):
        return open_dates + Timedelta(hours=FUTURES_OPEN_TIME_OFFSET)

    def execution_time_from_close(self, close_dates):
        return close_dates + Timedelta(hours=FUTURES_CLOSE_TIME_OFFSET)
