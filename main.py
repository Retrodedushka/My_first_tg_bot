import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import F

session = AiohttpSession()
bot = Bot(token='8717686709:AAFTVHUwdqG1FCSwxermCpVY_Fv6np-bQWM', session=session)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    buttons = [
        [KeyboardButton(text="Лукойл"), KeyboardButton(text="Сбер")],
        [KeyboardButton(text="Яндекс"), KeyboardButton(text="Озон")]
    ]
    kb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer("Привет! Выбери компанию:", reply_markup=kb)

@dp.message(F.text == "Лукойл")
async def lukoil_handler(message: Message):
    await message.answer("Ближайшие дивиденды Лукойл: 15 мая 2025 года.")

@dp.message(F.text == "Сбер")
async def sber_handler(message: Message):
    await message.answer("Ближайшие дивиденды Сбер: июль 2025 (рекомендованны).")

@dp.message(F.text == "Озон")
async def ozon_handler(message: Message):
    await message.answer("Ближайшие дивиденды Озон: май 2025 (рекомендованны).")

@dp.message(F.text == "Яндекс")
async def yandex_handler(message: Message):
    await message.answer("Ближайшие дивиденды Яндекс: апрель 2025 (рекомендованны).")

async def main():
    print("Ожидаю сообщения...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
