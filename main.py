import asyncio
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import Message

bot = Bot(token='8717686709:AAFTVHUwdqG1FCSwxermCpVY_Fv6np-bQWM')
dp = Dispatcher()

@dp.message()
async def start_handler(message: Message): 
    await message.answer("Привет! Я готов показать дивиденды.")

async def main():
    print("Ожидаю сообщения...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

