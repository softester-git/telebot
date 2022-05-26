import telebot
from libs import load_config


class TBot:

    def __init__(self):
        conf = load_config("tbinit.conf")
        self.bot = telebot.TeleBot(conf["tb_k"])
