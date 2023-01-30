# import os
import logging

from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN

from preprocessor import clean, tokenize_text, lemmatize_sentence
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from classifier import lrc, tfid
import pandas as pd

logging.basicConfig(level=logging.INFO)
# , filename="mylog.log")

# TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hello, {user_name}! Tell me your thoughts on any movie."

    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)

@dp.message_handler()
async def send_message(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    text = clean(text)
    text = tokenize_text(text)
    text = lemmatize_sentence(text)
    tfidf_represent = tfid.transform(pd.Series(text))
    text = lrc.predict(tfidf_represent)
    text = text[0]
    if text == 1:
        reply = "I'm glad you liked it!"
    else:
        reply = "I'm sorry that you didn't like it!"

    logging.info(f'{user_name=} {user_id=} sent message: {reply}')
    await bot.send_message(user_id, reply)


if __name__ == '__main__':
    executor.start_polling(dp)
