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
	logger.info("/lol " + args[0])
	user_name = args[0].lower()
	user_name = user_name.replace(" ", "")
	response = findUserInfo.findUserInfo(user_name)

	if (response.status_code == 200):
# default info
		res_str = response.json()[user_name]
		logger.info(res_str)
		u_lv = res_str["summonerLevel"]
		u_name = res_str["name"]
		u_id = res_str["id"]

		res_str = u_name + "(" + str(u_lv) + ") \n"

# Rank info
		response = league.getLeague_entry(u_id)
		if(response.status_code == 200):
			logger.info(response.json())
			response = response.json()[str(u_id)][0]
			u_tier = response["tier"]
			u_leagueName = response["name"]
			u_division = response["entries"][0]["division"]
			u_leaguePoints = response["entries"][0]["leaguePoints"]
			u_wins = response["entries"][0]["wins"]
			u_lossed = response["entries"][0]["losses"]
			u_rate = u_wins * 100 / (u_wins+u_lossed)

			res_str += u_tier + " " + str(u_division) + "(" + str(u_leaguePoints) + "LP)  " + str(u_wins) + "win / " + str(u_lossed) + "loss (" + str(u_rate) + "%) - " + u_leagueName
		else :
			res_str += "UnRanked"

# last game info
# TO DO

# make response msg

	elif(response.status_code == 404):
		res_str = "Can not find User " + user_name
	else :
		res_str = "Error : status_code - " + response.status_code
	
	logger.info(res_str)
	bot.sendMessage(chat_id=update.message.chat_id, text=res_str)


start_handler = CommandHandler('start', start)
lol_findUser_handler = CommandHandler('lol', lol_findUser, pass_args=True)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(lol_findUser_handler)
updater.start_polling()
