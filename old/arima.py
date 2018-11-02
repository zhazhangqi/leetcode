from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot

knownTimestamps = [
'2013-01-01 00:00',
'2013-01-01 01:00',
'2013-01-01 02:00',
'2013-01-01 03:00',
'2013-01-01 04:00',
'2013-01-01 05:00',
'2013-01-01 06:00',
'2013-01-01 08:00',
'2013-01-01 10:00',
'2013-01-01 11:00',
'2013-01-01 12:00',
'2013-01-01 13:00',
'2013-01-01 16:00',
'2013-01-01 17:00',
'2013-01-01 18:00',
'2013-01-01 19:00',
'2013-01-01 20:00',
'2013-01-01 21:00',
'2013-01-01 23:00']
humidity = [0.62,0.64,0.62,0.63,0.63,0.64,0.63,0.64,0.48,0.46,0.45,0.44,0.46,0.47,0.48,0.49,0.51,0.52,0.52]
timestamps = [
'2013-01-01 07:00',
'2013-01-01 09:00',
'2013-01-01 14:00',
'2013-01-01 15:00',
'2013-01-01 22:00']
startDate = '2013-01-01'
endDate = '2013-01-01'
pyplot.plot(humidity)
# def predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps):
# 	for x in knownTimestamps:
# 		time = datetime.strptime(x, "%Y-%m-%d %H:%M").seconds
# 		print time
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

def predictMissingHumidity(startDate='1/1/2012', endDate="1/2/2012",
	                       knownTimestamps=None,
	                           humidity=None, timestamps=None):

	train_pd = pd.DataFrame()
	train_pd['index'] = knownTimestamps
	train_pd['humidity'] = humidity
	test_pd = pd.DataFrame()
	test_pd["indx"] = timestamps


	# rng = pd.date_range(start=startDate, end=endDate, freq='H')
	# train = pd.Series(np.random.randn(len(rng)), index=rng)
	# print train
	# X = train.values
	# size = int(len(X) * 0.66)
	# train, test = X[0:size], X[size:len(X)]
	train = train_pd["humidity"].values
	test = test_pd.values
	history = [x for x in train]
	predictions = list()
	for t in range(len(test)):
		model = ARIMA(history, order=(5, 1, 0))
		model_fit = model.fit(disp=0)
		print(model_fit.summary())
		output = model_fit.forecast()
		yhat = output[0]
		predictions.append(yhat)
		obs = test[t]
		history.append(obs)
		# print('predicted=%f, expected=%f' % (yhat, obs))
	error = mean_squared_error(test, predictions)
	print('Test MSE: %.3f' % error)
	print predictions
predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps)
