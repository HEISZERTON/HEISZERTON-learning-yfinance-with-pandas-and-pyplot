import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn-v0_8')

import yfinance as yf

def main():
	msft = yf.Ticker('msft')

	# stockinfo = msft.info

	# for key,value in stockinfo.items():
	# 	print(key, ":", value)

	# numshares = msft.info['sharesOutstanding']
	# print(numshares)

	df = msft.dividends
	data = df.resample('Y').sum()
	data = data.reset_index()
	data['Year'] = data['Date'].dt.year

	plt.figure()
	plt.bar(data['Year'],data['Dividends'])
	plt.ylabel('Dividend yeild ($)')
	plt.xlabel('Year')
	plt.title('Microsoft Dividend History')
	plt.xlim(2002,2023)
	plt.show()

main()