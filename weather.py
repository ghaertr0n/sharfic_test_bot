import requests


appid = '3834e9a6a69b1d7e2d845171986a7f6a'


def get_weather():
	url = 'http://api.openweathermap.org/data/2.5/weather?q=astana&APPID=' + appid
	response = requests.get(url).json()
	price = response['main']['temp']
	temp = (str((round(price-273)))+ ' °C')
	return temp


get_weather()