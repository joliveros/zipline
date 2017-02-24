from unittest import TestCase
import pandas as pd

from .test_trading_calendar import ExchangeCalendarTestBase
from zipline.utils.calendars.exchange_calendar_cryptocurrency import CryptocurrencyCalendar


class cryptocurrencyCalendarTestCase(ExchangeCalendarTestBase, TestCase):

    answer_key_filename = 'cryptocurrency'
    calendar_class = CryptocurrencyCalendar

    MAX_SESSION_HOURS = 24

    def test_2016_no_holidays(self):
        # good friday: 2016-03-25
        # christmas (observed)_: 2016-12-26
        # new years (observed): 2016-01-02
        for date in ["2016-03-25", "2016-12-26", "2016-01-02"]:
            self.assertFalse(
                self.calendar.is_session(pd.Timestamp(date, tz='UTC'))
            )
