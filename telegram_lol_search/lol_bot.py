#-*- coding: utf-8 -*-

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

import sys

# import lol_search API
sys.path.insert(0, "/home/loverkei/workspace/lol_search/lol_search/lol_api")
import findUserInfo
import league
import summoner

# logger
logger = logging.getLogger('lol_telbot_logger')

fileHandler = logging.FileHandler('../lol_telbot.log')
streamHandler = logging.StreamHandler()

logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

logger.setLevel(logging.INFO)

logging.info("--- Start LoL Search Tel Bot ---")

# import TOKEN
import myToken
TOKEN = myToken.getToken()

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher



# Telegram Start command #
def start(bot, update):
	logger.info("/start")
	bot.sendMessage(chat_id=update.message.chat_id, text="LoL 검색 봇 시작!!!\n/lol LOL_ID : LoL 검색")

# Lol User find command #
def lol_findUser(bot, update, args):
	# remake user name. (delete blank, combine args)
	user_name = ""
	for tmp in args:
		tmp = tmp.lower()
		user_name += tmp
	user_name = user_name.replace(" ", "")
	
	logger.info("/lol " + user_name)

	# find user_info
	user = getUserInfoByDB(user_name,summoner.Summoner(user_name))
	if(user.getUstatus() != 0):
		# To DO
		print("TO DO")
	else :
		# get user infomation by RIOT api
		user = getUserInfoByRIOT(user_name, user)

	# make response message.
	res_str = makeResponse(user)
	bot.sendMessage(chat_id=update.message.chat_id, text=res_str)


# TO DO 
def getUserInfoByDB(user_name, user):
	user.setUstatus(0)  # Can not find User in DB
	return user



# make /lol res_str
def getUserInfoByRIOT(user_name, user):
	response = findUserInfo.findUserInfo(user_name)

	if (response.status_code == 200):
# default info
		res_str = response.json()[user_name]
		logger.info(res_str)
		user.setUlv(str(res_str["summonerLevel"]))
		user.setUname(res_str["name"])
		user.setUid(str(res_str["id"]))


# Rank info
		response = league.getLeague_entry(user.getUid())
		if(response.status_code == 200):
			logger.info(response.json())
			response = response.json()[user.getUid()][0]
			user.setUtier(str(response["tier"]))
			user.setUleagueName(str(response["name"]))
			user.setUdivision(str(response["entries"][0]["division"]))
			user.setUleaguePoints(response["entries"][0]["leaguePoints"])
			user.setUwins(response["entries"][0]["wins"])
			user.setUlossed(response["entries"][0]["losses"])
			user.setUstatus(201)
		else :
			user.setUtier("UnRanked")
			user.setUstatus(200)

# last game info
# TO DO

	elif(response.status_code == 404):
		user.setUstatus(response.status_code)
		logger.info("Error : Can not find user - " + user.getUname())
	else :
		user.setUstatus(response.status_code)
		logger.info("Error : status_code - " + str(response.status_code))
	
	return user



# make "/lol" response msg
def makeResponse(user):
	if(user.getUstatus() == 201): # Ranked player
		rsp_str = user.getUname() + "(" + user.getUlv() + ") \n"
		u_rate = user.getUwins() * 100 / (user.getUwins() + user.getUlossed())
		rsp_str += user.getUtier() + " " + user.getUdivision() + "(" + str(user.getUleaguePoints()) + "LP)  " + str(user.getUwins()) + "win / " + str(user.getUlossed()) + "loss (" + str(u_rate) + "%) - " + user.getUleagueName()
	elif(user.getUstatus() == 200): # UnRanked player
		rsp_str = user.getUname() + "(" + user.getUlv() + ") \n"
		rsp_str += "UnRanked."
	else :
		rsp_str = "Can not find user " + user_getUname() + ", " + str(user_getUStatus())

	logger.info("Response : " + rsp_str)
	return rsp_str



# connection of tel_bot
start_handler = CommandHandler('start', start)
lol_findUser_handler = CommandHandler('lol', lol_findUser, pass_args=True)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(lol_findUser_handler)
updater.start_polling()
