import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import F

session = AiohttpSession()
bot = Bot(token='8717686709:AAFTVHUwdqG1FCSwxermCpVY_Fv6np-bQWM', session=session)
dp = Dispatcher()
companies = {
    "Лукойл": "06 мая 2026 года",
    "Сбер": "15 июля 2025 года",
    "Озон": "28 мая 2025 года",
    "Яндекс": "13 апреля 2025 года"
}

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    buttons = [[KeyboardButton(text=name)] for name in companies.keys()]
    kb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer("Привет! Выбери компанию:", reply_markup=kb)

@dp.message(F.text.in_(companies.keys()))
async def company_info(message: Message):
    name = message.text
    date = companies.get(name)
    await message.answer(f"Дата публикации финансовой отчетности для {name}: {date}")

async def main():
    print("Ожидаю сообщения...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
