#!/usr/bin/python
'''
'''


import collections
import datetime
import ystockquote


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_flask():
  return 'hello, flask!'


TickerPriceTime = collections.namedtuple('TickerPriceTime',['ticker', 'date', 'closing_price'])


def closing_price_table(ticker, prices):
  return sorted(TickerPriceTime(ticker, key_date, prices[key_date]['Adj Close']) for key_date in prices)


@app.route('/stock/<ticker>')
def historic_closing_prices(ticker):
  ''' pulls historic closing price data from the Yahoo finance API  '''
  start = (datetime.datetime.now() + datetime.timedelta(days=-365)).strftime('%Y-%m-%d')
  end   = datetime.datetime.now().strftime('%Y-%m-%d')
  prices = ystockquote.get_historical_prices(ticker, start, end)
  price_table = closing_price_table(ticker, prices)
  return 'request for symbol: \n%s\n' % '\n'.join(map(str, price_table))


if __name__ == "__main__":
  app.run()