#_*_ coding:utf-8 *_*

import requests

base_url = "https://kr.api.pvp.net/"
api_url = "api/lol/"
region_KR = "kr/"
api_ver = "v1.4/"
api_type = "summoner/"
api_key = "input your api Key"

end_str = "?api_key="
api_find_type = "by-name/"


def request_lol(full_url):
	req = requests.get(full_url)

	print(req.json())
	return req

def findUserInfo(user_name):
	user_name = user_name.lower()
	user_name = user_name.replace(" ", "")
	print(user_name)

	full_url = base_url + api_url + region_KR + api_ver + api_type + api_find_type + user_name + end_str + api_key
	response = request_lol(full_url)

	return response


if __name__ == "__main__":
	import requests

	response = findUserInfo("DK")

	if response :
		print(response.json())
