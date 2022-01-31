import requests
from datetime import datetime
import telebot
from config import token


def get_data():
	req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
	response = req.json()
	sell_price = response["btc_usd"]["sell"]
	print(response)
	print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price {sell_price} ")



def telegram_bot(token):
	bot = telebot.TeleBot(token)

	@bot.message_handler(commands=["start"])
	def start_message(message):
		bot.send_message(message.chat.id,'Hello friend Write the <price> to find out the cost of BTC !! ')

	@bot.message_handler(content_types = ["text"])
	def send_text(message):
		if message.text.lower() == 'price':
			try:
				req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
				response = req.json()
				sell_price = response["btc_usd"]["sell"]
				bot.send_message(
					message.chat.id,
					f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price {sell_price} "
				)
			except Exception as ex:
				print(ex)
				bot.send_message(message.chat.id,'Damn something was WRONG!)')

		else:
			bot.send_message(message.chat.id,'Whaaat??? check the comand dude please)')



	bot.polling()



if __name__ == '__main__':
	telegram_bot(token)
	get_data()