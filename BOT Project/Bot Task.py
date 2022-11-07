import telebot
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
logging.basicConfig(level=logging.INFO)
# dp = Dispatcher(bot)

bot = Bot(token = "5456204040:AAGNo61KJdwsJejgIBx7K_qtItrf41L6CQY")
dp = Dispatcher(bot)
@dp.message_handler(commands =['start'])
async def cmd_start (message: types.Message):
  # bot.send_message(message.chat.id,"Привет ✌️ ")
  await message.answer ("Hello!")

async def main():
  await dp.start_polling(bot)
# bot.infinity_poling()
if __name__ == "__main__":
  asyncio.run(main())
