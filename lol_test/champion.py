# champion.py #

#
api_ver = "/v1.2/"
api_type = "champion"
#

# region 		- input
# api key  		- input
#
base_url_pre = "https://"
base_url_post = ".api.pvp.net/"
api_url = "api/lol/"
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


#####################
# champion
def getChampions(region , api_key):
	full_url = base_url_pre + region + base_url_post + api_url + region + api_ver + api_type + end_str + api_key
	response = request_lol(full_url)

	return response


def getChampionInfo(region, champID, api_key):
	full_url = base_url_pre + region + base_url_post + api_url + region + api_ver + api_type + "/" + str(champID) + end_str + api_key
	response = request_lol(full_url)

	return response


if __name__ == "__main__" :
	import requests
	region = "kr"
	api_key = input your api_key

	response = getChampions(region, api_key)
	if response :
		print(response.json())

	response = getChampionInfo(region, 266, api_key)
	if response :
		print(response.json())

	
