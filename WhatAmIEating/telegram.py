import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("905297180:AAFIGPAg0PJm60b7M-NsX2Ka6fNwlvjjeWA")
bot = Chatbot("Nexus")
def recebendomensagem(msg):
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, resp)



telegram.message_loop(recebendomensagem)


while True:
    pass
