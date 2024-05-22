import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

API_TOKEN = os.environ.get("TELEGRAM_TOKEN")

bot = telebot.TeleBot(API_TOKEN)
meme_pic = open("./Know Your Meme.jpeg", "rb")


@bot.message_handler(commands=["start"])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(
        message,
        "Dey calm down {}, shey tapping never tire you? try dey rest small, lol!".format(
            message.chat.first_name
        ),
    )
    bot.send_photo(message.chat.id, meme_pic)


@bot.message_handler(func=lambda msg: True)
def ignore_all(message: telebot.types.Message):
    bot.reply_to(message, "Oga, go rest jare")


bot.infinity_polling()
