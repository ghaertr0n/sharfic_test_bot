import requests, misc

appid = misc.appid

def get_weather():
	url = 'http://api.openweathermap.org/data/2.5/weather?q=astana&APPID=' + appid
	response = requests.get(url).json()
	price = response['main']['temp']
	temp = (str((round(price-273)))+ ' °C')
	return temp
