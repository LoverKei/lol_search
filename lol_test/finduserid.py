import requests
import summoner

base_url = "https://kr.api.pvp.net/"
api_url = "api/lol/"
region_KR = "kr/"
api_ver = "v1.4/"
api_type = "summoner/"
api_key = input your api_key

end_str = "?api_key="
api_find_type = "by-name/"

user_name = "벵기"
user_name = user_name.lower()
user_name = user_name.replace(" ", "")
print(user_name)


#####################
# User infomation 
# Name, ID, level

full_url = base_url + api_url + region_KR + api_ver + api_type + api_find_type + user_name + end_str + api_key

# full_url exmple #
# https://kr.api.pvp.net/api/lol/kr/v1.4/summoner/by-name/dk?api_key= input your api_key #
#print(full_url)

req = requests.get(full_url)
#print(req)

print(req.status_code)
print(req.json())
if req.status_code == 200:
	decoded = req.json()[user_name]

	user1 = summoner.Summoner(user_name)
	user1.setSMname(decoded["name"])
	user1.setSMid(decoded["id"])
	user1.setSMlv(decoded["summonerLevel"])
	print("Name : %s\nID : %s\nLevel : %s" %(user1.SMname, user1.SMid, user1.SMlv))


elif req.status_code == 404:
	print("Can not find %s." % user_name)
	print(req.text)

else :
	print(req.status_code)
	print(req.text)
