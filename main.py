import telebot
from telebot import types
import json


with open("tbinit.conf") as f:
    conf = json.load(f)
bot = telebot.TeleBot(conf["tb_k"])


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Очно")
    item2 = types.KeyboardButton("Онлайн")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Вид расстановок', reply_markup=markup)


@bot.message_handler(commands=["Очно"])
def offline(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Очно: Группа")
    item2 = types.KeyboardButton("Очно: Клиент")
    item3 = types.KeyboardButton("Очно: Заместитель")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, 'Как будете участвовать?', reply_markup=markup)

@bot.message_handler(commands=["Очно: Группа"])
def offline(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(text="Записаться", data="Пример 1")
    item2 = types.KeyboardButton("Как добраться")
    item3 = types.KeyboardButton("Внести предоплату")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, 'Как будете участвовать?', reply_markup=markup)

@bot.message_handler(commands=["Онлайн"])
def online(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Онлайн: Группа")
    item2 = types.KeyboardButton("Онлайн: Клиент")
    item3 = types.KeyboardButton("Онлайн: Заместитель")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, 'Как будете участвовать?', reply_markup=markup)


#@bot.message_handler(content_types=["text"])
#def handle_text(message):
#    if message.text == "Очно":
#    if message.text == "Онлайн":
#        pass

    #bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


bot.polling(none_stop=True, interval=0)
