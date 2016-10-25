# currentgame.py

# platformId 		- input
# summonerId		- input
# api key  			- input
#
base_url_pre = "https://"
base_url_post = ".api.pvp.net/"
api_url = "observer-mode/rest/consumer/getSpectatorGameInfo/"
end_str = "?api_key="
#

def request_lol(full_url):
	req = requests.get(full_url)

#	print(req.status_code)
#	print(req.json())
	if req.status_code == 200:
		return req

	else :
		print("response status code Not 200 : %d" % (req.status_code))
		print(req.text)
		return 0

def getCunnrentGame(platformId, summonerId, api_key):
	full_url = base_url_pre + platformId.lower() + base_url_post + api_url + platformId.upper() + "/" + str(summonerId) + end_str + api_key
	response = request_lol(full_url)

	return response

if __name__ == "__main__":
	import requests
	platformId = "KR"
	summonerId = "1253868"
	region = "kr"
	api_key = input your api_key

	response = getCunnrentGame(platformId, summonerId, api_key)

	if response :
		print(response.json())

