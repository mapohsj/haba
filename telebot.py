import telegram

token = "1639211097:AAE3FSBm3czPCEK1BvdZrDY13AVjjnPF4O4"
bot = telegram.Bot(token)
updates = bot.getUpdates()
print(updates[0].message.chat_id)
bot.sendMessage(chat_id=1688894930, text="안녕하세요. 저는 봇입니다.")
