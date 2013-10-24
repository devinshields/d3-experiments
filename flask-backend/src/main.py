#!/usr/bin/python
'''
'''

import collections
import datetime
import json
import ystockquote

from flask import request
from flask import Flask


app = Flask(__name__, static_folder='static', static_url_path='') # note: is tweaky about '/'s


TickerPriceTime = collections.namedtuple('TickerPriceTime', ['ticker', 'date', 'closing_price'])
PriceTime       = collections.namedtuple('PriceTime',       ['date', 'closing_price'])


@app.route('/api')
def hello_flask():
  return '''
<!DOCTYPE html>
<html>
    <body>
        <form action="./closing-price" method="get">
            Stock Symbol: <input type="text" name="ticker"><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>'''


def closing_price_table(prices, ticker=''):
  if ticker:
    return sorted(TickerPriceTime(ticker, key_date, prices[key_date]['Adj Close']) for key_date in prices)
  return sorted(PriceTime(key_date, prices[key_date]['Adj Close']) for key_date in prices)


def callback_wrapper(o):
  return 'api_callback({0})'.format(o)


@app.route('/closing-price')
def historic_closing_prices():
  ''' pulls historic closing price data from the Yahoo finance API  '''
  ticker = request.args.get('ticker')
  start  = (datetime.datetime.now() + datetime.timedelta(days=-365)).strftime('%Y-%m-%d')
  end    = datetime.datetime.now().strftime('%Y-%m-%d')
  prices = ystockquote.get_historical_prices(ticker, start, end)
  table  = closing_price_table(prices)
  return callback_wrapper(json.dumps(table))


if __name__ == "__main__":
  app.run(debug=True)
  
  
