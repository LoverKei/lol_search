#_*_ coding:utf-8 *_*

import requests
import summoner
import apikey

base_url = "https://kr.api.pvp.net/"
api_url = "api/lol/"
region_KR = "kr/"
api_ver = "v1.4/"
api_type = "summoner/"

end_str = "?api_key="
api_find_type = "by-name/"


def request_lol(full_url):
	req = requests.get(full_url)
	return req

def findUserInfo(user_name):
	user_name = user_name.lower()
	user_name = user_name.replace(" ", "")

	api_key = apikey.getKey()

	full_url = base_url + api_url + region_KR + api_ver + api_type + api_find_type + user_name + end_str + api_key
	response = request_lol(full_url)

	return response


if __name__ == "__main__":
	import requests

	response = findUserInfo("dk")

	if response :
		print(response.json())
