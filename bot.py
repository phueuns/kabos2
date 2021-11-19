import telebot
from telebot import types
import sys
import json
bot = telebot.TeleBot('2082150126:AAGj2351pNNWwthRwlKRGvk_0P37CSpyuyQ')#Token
@bot.message_handler(commands=["start"])
def id(message):
 cht = message.chat.id
 frt = message.chat.first_name
 usr = message.from_user.username
 typ = message.chat.type
 dat = message.date
 bot.send_message(message.chat.id, text="""
▮🆔 ¦ 𝙄𝘿 ◍▸ {}
▯🌐 ¦ 𝙐𝙎𝙀𝙍 ◍▸ @{}
▮👤 ¦ 𝙉𝘼𝙈𝙀 ◍▸ {}
▯♉️ ¦ 𝙏𝙔𝙋𝙀 ◍▸ {}
▮♐️ ¦ 𝘿𝘼𝙏𝘼 ◍▸ {}
▯𝗖𝗛 ¦ @nn_konn""".format(cht,usr,frt,typ,dat))
bot.polling(True)