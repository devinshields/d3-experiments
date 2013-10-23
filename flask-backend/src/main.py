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


TickerPriceTime = collections.namedtuple('TickerPriceTime', ['ticker', 'date', 'closing_price'])
PriceTime       = collections.namedtuple('PriceTime',       ['date', 'closing_price'])


def closing_price_table(prices, ticker=''):
  if ticker:
    return sorted(TickerPriceTime(ticker, key_date, prices[key_date]['Adj Close']) for key_date in prices)
  return sorted(PriceTime(key_date, prices[key_date]['Adj Close']) for key_date in prices)
  

@app.route('/closing-price/<ticker>')
def historic_closing_prices(ticker):
  ''' pulls historic closing price data from the Yahoo finance API  '''
  start = (datetime.datetime.now() + datetime.timedelta(days=-365)).strftime('%Y-%m-%d')
  end   = datetime.datetime.now().strftime('%Y-%m-%d')
  prices = ystockquote.get_historical_prices(ticker, start, end)
  return  str(closing_price_table(prices))


if __name__ == "__main__":
  app.run()
  
  