import os
from telegram import Bot



def send_message():

    api_token = "6759412477:AAEvNRKvWDvPMVJY-uM2V-z4hZEPjCoOUsA"
    #chat_id = "YOUR_CHAT_ID"
    message_text =   "Good morning, here's your Morning report: \n" 
   
    bot = Bot(token=api_token)
    bot.send_message(chat_id=505850629, text=message_text)
    bot.send_photo(chat_id=505850629, photo=open('output.png', 'rb'))

    


if __name__ == "__main__":
    send_message()