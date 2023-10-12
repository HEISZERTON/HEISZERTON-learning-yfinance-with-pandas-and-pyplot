# Folwing youtube tutorial 
# https://www.youtube.com/watch?v=9nB__kJio-M

import pandas
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn-v0_8')

import yfinance as yf

def main():
	msft = yf.Ticker('msft')

	stockinfo = msft.info

	for key,value in stockinfo.items():
		print(key, ":", value)

	numshares = msft.info['sharesOutstanding']
	print(numshares)
	print(msft.balancesheet)

def plot_chart(stock_ticker):
	security = yf.Ticker(stock_ticker)

	today = datetime.now().date().strftime("%Y-%m-%d")
	df = security.history(start = '2020-01-01', end = today)
	plt.figure()
	plt.plot(df['Close'])
	plt.title(security.info['shortName'] + ' Price History')
	plt.ylabel('Price ($)')
	plt.xlabel('Year')
	plt.show()

def plot_dividend(stock_ticker):
	security = yf.Ticker(stock_ticker)

	df = security.dividends
	data = df.resample('Y').sum()
	data = data.reset_index()
	data['Year'] = data['Date'].dt.year

	plt.figure()
	plt.bar(data['Year'],data['Dividends'])
	plt.ylabel('Dividend yeild ($)')
	plt.xlabel('Year')
	plt.title(security.info['shortName'] + ' Dividend History')
	plt.xlim(2002,2020)
	plt.show()

def chart_list(ticker_list):

	df = pandas.DataFrame()
	today = datetime.now().date().strftime("%Y-%m-%d")

	for security in ticker_list:	
		df[security] = yf.Ticker(security).history(start = '2020-01-01', end = today).Close

	plt.figure()
	plt.plot(df)
	plt.legend(ticker_list)
	plt.title('Security Price History')
	plt.ylabel('Price ($)')
	plt.xlabel('Year')
	plt.show()

#plot_dividend('msft')
#plot_chart('msft')
chart_list(['voo','msft','aapl','nvda','jnj','axp','dis'])
#main()