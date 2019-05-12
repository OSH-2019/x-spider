import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
class stock:
	price = pd.DataFrame([]);
	name=""
	def __init__(self,stock_name,start,end):
		
		# get stock data, from yahoo finance within the dates specified
		self.price = web.DataReader(stock_name, "yahoo", start, end)
		self.price.head(n=3)
		self.name=stock_name

	def store(self,PATH):
		self.price.to_csv(PATH)
	def printf(self):
		print(self.price)

def main():
	# We will look at stock prices over the past year, starting at January 1, 2016
	start = datetime.datetime(2017,1,1)
	end = datetime.date.today()
	name = "AAPL"
	st=stock(name,start,end)
	st.store("%s.csv"%st.name)
	#print(st.price.index)
	#st.printf()
	'''
	start = datetime.datetime(2016,1,1)
	end = datetime.date.today()

	stock = "AAPL"

# get stock data, from yahoo finance within the dates specified
	stock = web.DataReader(stock, "yahoo", start, end)

	stock.head(n=3)
	print(stock)
	'''

if __name__ =="__main__":
	main()

