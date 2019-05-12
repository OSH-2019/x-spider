import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller,ARMA
def adf_test(ts): 
	adftest = adfuller(ts,autolag='BIC') 
	adf_res = pd.Series(adftest[0:4], index=['Test Statistic','p-value','Lags Used','Number of Observations Used']) 
	for key, value in adftest[4].items(): 
		adf_res['Critical Value (%s)' % key] = value 
	return adf_res
	
def draw_ma(ts, w): 
	ma = ARMA(ts, order=(0, w)).fit(disp = -1) 
	ts_predict_ma = ma.predict() 
	ar = ARMA(ts, order=(w,0)).fit(disp=-1) 
	ts_predict_ar = ar.predict() 
	plt.clf() 
	plt.plot(ts, color='yellow',label = "ORG") 
	plt.plot(ts_predict_ar, label="AR") 
	plt.plot(ts_predict_ma, label="MA") 
	
	plt.legend(loc="best") 
	plt.title("MA Test %s" % w) 
	plt.savefig( str(w) +".pdf", format='pdf') 
	return ts_predict_ma

def test_ts(ts, w, title): 
	roll_mean = ts.rolling(window = w).mean()

	roll_std = ts.rolling(window = w).std() 
	
	#pd_ewma = pd.ewma(ts, span=w) panda 当前版本没有ewma方法了
	pd_ewma=ts.ewm(span=w).mean()
	plt.clf() 
	plt.figure() 
	plt.grid() 
	plt.plot(ts, color='blue',label='Original') 
	plt.plot(roll_mean, color='red', label='Rolling Mean') 
	plt.plot(roll_std, color='black', label = 'Rolling Std') 
	plt.plot(pd_ewma, color='yellow', label = 'EWMA') 
	plt.legend(loc='best') 
	plt.title('Rolling Mean & Standard Deviation')

	#plt.show() 
	plt.savefig(title+'.pdf', format='pdf')

def main():
	data=pd.read_csv('AAPL.csv', index_col='Date')

	#print(data.head())	
	#print(data.dtypes)
	data.index = pd.to_datetime(data.index)
	#print(data.index)
	ts = data['Close']
	#print(type(ts['2019-01-02':'2019-05-01'].rolling(window = 20).mean()))
	ts = ts.sort_index(ascending=True)
	ts_log = np.log(ts)
	ts_diff = ts_log.diff(1)
	
	ts = ts['2018-01-02':]
	#print(ts['2019-01-04':])
	ts_ret = np.diff(ts,1)
	ts_log = np.log(ts)
	ts_diff = ts_log.diff(1)
	ts_diff.dropna(inplace=True)
	print("--------------日收盘-------------")
	adf_res=adf_test(ts)
	print(adf_res)
	test_ts(ts[:], 100, title='test_org')
	print("--------------简单收益率------------")
	adf_res=adf_test(ts_ret)
	print(adf_res)
	print("--------------对数收益率-------------")
	adf_res=adf_test(ts_diff)
	print(adf_res)
	test_ts(ts_log[:], 100, title='test_log')
	
	print ('---------------------------MA TEST------------------------------') 
	adf_res = adf_test(ts_diff['2018-01-01':]) 
	print ('ADF test results (ema diff):\n', adf_res) 
	ma_predict = draw_ma(ts_diff['2018-01-01':], 9) 
	#rtn_test(ma_predict, "ma predict")


if __name__=="__main__":
	main()

