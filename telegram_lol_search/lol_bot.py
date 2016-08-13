#-*- coding: utf-8 -*-

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

import sys

sys.path.insert(0, "/home/loverkei/workspace/lol_search/lol_search/lol_test")
import findUserInfo


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO)

print("한글 테스트 ")

TOKEN = "input your TOKEN"
updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

# Telegram Start command #
def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="LoL 검색 봇 시작!!!")

# Lol User find command #
def lol_findUser(bot, update, args):
	u_name = args[0]
	user_name = u_name.lower()
	user_name = user_name.replace(" ", "")
	response = findUserInfo.findUserInfo(user_name)

	if (response.status_code == 200):
		res_str = response.json()[user_name]
	elif(response.status_code == 404):
		res_str = "Can not find User " + user_name
	else :
		res_str = "Error : status_code - " + response.status_code
	
	print(res_str)
	bot.sendMessage(chat_id=update.message.chat_id, text=res_str)


start_handler = CommandHandler('start', start)
lol_findUser_handler = CommandHandler('lol', lol_findUser, pass_args=True)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(lol_findUser_handler)
updater.start_polling()


