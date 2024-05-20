import os
from telegram import Bot
from telegram import Update
import asyncio
from prepare_sink import prepare_sink
from filter import filter


api_token = "6759412477:AAEvNRKvWDvPMVJY-uM2V-z4hZEPjCoOUsA"

bot = Bot(token=api_token)
chat_id = -1002055037831 

def send_message(message_text):
    asyncio.run(bot.send_message(chat_id=chat_id, text=message_text))
    # bot.send_photo(chat_id=505150629, photo=open('output.png', 'rb'))



prepare_sink(10)
article_dict = filter()
message = ""
send_message("Here are the top articles personaly for today, darling ;)\n" )
for title, url in article_dict.items():
    message += f"- [{title}]({url})\n"
send_message(message)




    
