import time

from aiogram import Bot
from telethon.sync import TelegramClient, events

dtn_en_chat_id = -1001612340810
dtn_ru_chat_id = -1001631464919

# test_chat_id1 = -1001809615307
# test_chat_id2 = -1001851643557

api_id = 25432102
api_hash = 'c023c1fff1ab1a62604459ca5ca81b25'
sheba_en_chat_id = -1001637720408
sheba_ru_chat_id = -1001598134609

bot = Bot(token='5924185748:AAFHD9tl5pluK1mPTu-Uey9LWnSkHteOVaU')

with TelegramClient('forward_dtn_yanevforme', api_id, api_hash) as client:
    print("Starting telethon")

    @client.on(events.NewMessage(chats=[dtn_en_chat_id]))
    async def handler(event):
        # our_dtn = await client.get_entity(sheba_en_chat_id)
        print(event.message)
        await bot.send_message(sheba_en_chat_id, text=event.message.message)
        # client.send_message(entity=our_dtn, message=event.message)


    @client.on(events.NewMessage(chats=[dtn_ru_chat_id]))
    async def handler(event):
        # our_dtn = await client.get_entity(sheba_ru_chat_id)
        print(event.message)
        time.sleep(1)
        await bot.send_message(sheba_ru_chat_id, text=event.message.message)
        # await client.send_message(entity=our_dtn, message=event.message)


    client.run_until_disconnected()
    print("Stop telethon")
