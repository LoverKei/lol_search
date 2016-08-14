# league.py

import requests
import apikey

base_url_pre = "https://"
base_url_post = ".api.pvp.net/"
api_url = "api/lol/"
end_str = "?api_key="
api_ver = "/v2.5/"
api_type = "league/by-summoner/"


def request_lol(full_url):
	req = requests.get(full_url)
	return req

def getLeague_entry(summonerId, platformId = "kr"):
	api_key = apikey.getKey()
	full_url = base_url_pre + platformId + base_url_post + api_url + platformId + api_ver + api_type + str(summonerId) + "/entry" + end_str + api_key

	response = request_lol(full_url)

	return response

if __name__ == "__main__":
	import requests
	summonerId = "1401389"

	response = getLeague_entry(summonerId)

	if response :
		print(response.json())

