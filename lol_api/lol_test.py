
import requests
import json
import sys
import summoner

#sys.path.append("D:\work\temp\python\lol_test")
#print(sys.path)

base_url = "https://kr.api.pvp.net/"
api_url = "api/lol/"
region_KR = "kr/"
api_ver = "v1.4/"
api_type = "summoner/"

api_key = "input your api_key"

end_str = "?api_key="
api_find_type = "by-name/"

user_name = "각성클라우드9"
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


"""
#########################
# matchlist

api_ver = "v2.2/"
api_type = "matchlist/"
api_find_type = "by-summoner/"

full_url = base_url + api_url + region_KR + api_ver + api_type + api_find_type + str(user1.SMid) + end_str + api_key

req = requests.get(full_url)
print(req.json())
"""

"""
########################
# match - test
api_ver = "v2.2/"
api_type = "match/"

full_url = base_url + api_url + region_KR + api_ver + api_type + "2454875350" + end_str + api_key

req = requests.get(full_url)
print(req.json())
"""


"""
#####################################3
# league - entry

# response example #
# {'dk': {'id': 1401389, 'revisionDate': 1464962927000, 'profileIconId': 508, 'name': 'D   K', 'summonerLevel': 30}} #

decoded = req.json()
print(decoded)

user_id = str(decoded[user_name]['id'])
print("user_name : " + user_name + "   user_id : " + user_id)

print("\n\n\n")

#dk_id = "1401389"
api_ver = "v2.5/"
api_type = "league/"
api_find_type = "by-summoner/"
api_type_post = "/entry"

full_url = base_url + api_url + region_KR + api_ver + api_type + api_find_type + user_id + api_type_post + end_str + api_key

print(full_url)
req = requests.get(full_url)
decoded = req.json()
summoner_data = decoded[user_id]
print(decoded)
print("\n\n")
print(summoner_data)

"""

"""
################################
# league
api_ver = "v2.5/"
api_type = "league/"
api_find_type = "by-summoner/"

full_url = base_url + api_url + region_KR + api_ver + api_type + api_find_type + str(user1.SMid) + end_str + api_key

print(full_url)

req = requests.get(full_url)

decoded = req.json()

print(decoded)
"""
