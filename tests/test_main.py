import pytest
from unittest.mock import AsyncMock
from aiogram.types import Message
from main import cmd_start, lukoil_handler, sber_handler, ozon_handler, yandex_handler

@pytest.mark.asyncio
async def test_cmd_start():
    message = AsyncMock(spec=Message)
    await cmd_start(message)
    message.answer.assert_called_once()
    args, kwargs = message.answer.call_args
    assert "Привет! Выбери компанию:" in args[0]
    assert "reply_markup" in kwargs

@pytest.mark.asyncio
async def test_lukoil_handler():
    message = AsyncMock(spec=Message)
    await lukoil_handler(message)
    message.answer.assert_called_once_with("Ближайшие дивиденды Лукойл: 15 мая 2025 года.")

@pytest.mark.asyncio
async def test_sber_handler():
    message = AsyncMock(spec=Message)
    await sber_handler(message)
    message.answer.assert_called_once_with("Ближайшие дивиденды Сбер: июль 2025 (рекомендованны).")

@pytest.mark.asyncio
async def test_ozon_handler():
    message = AsyncMock(spec=Message)
    await ozon_handler(message)
    message.answer.assert_called_once_with("Ближайшие дивиденды Озон: май 2025 (рекомендованны).")

@pytest.mark.asyncio
async def test_yandex_handler():
    message = AsyncMock(spec=Message)
    await yandex_handler(message)
    message.answer.assert_called_once_with("Ближайшие дивиденды Яндекс: апрель 2025 (рекомендованны).")