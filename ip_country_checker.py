#Coded by Saputra
import requests
import json

def ip():
	url = "http://ip-api.com/json/"
	req = requests.get(url).text
	load = json.loads(req)
	get_country = load['country']
	get_country_code = load['countryCode']
	regionName = load['regionName']
	get_city = load['city']
	print("Country : {}" .format(get_country))
	print("Country code : {}" .format(get_country_code))
	print("Region : {}" .format(regionName))
	print("Get city : {}" .format(get_city))


ip()