import asyncio
import json
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from main import main_collector
from keyboards import main_keyboard, city_keyboard
from attribute import TOKEN

TOKEN = TOKEN
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет! 👋 Я бот, который показывает текущие курсы валют по разным городам Украины. "
                         f"Выбери интересующий тебя город, чтобы увидеть актуальные курсы валют. "
                         f"Просто нажми кнопку 'Выбрать город🏙️', чтобы начать!", reply_markup=main_keyboard())


@dp.message()
async def process_script(message: Message):
    msg = message.text.lower()

    city_mappings = {
        "днепр": "dnepropetrovsk",
        "львов": "lvov",
        "запорожье": "zaporozhye",
        "киев": "kiev",
        "харьков": "kharkov"
    }

    if msg == "выбрать город🏙️":
        await message.answer('Выбирай', reply_markup=city_keyboard())
    elif msg in city_mappings:
        city_name = city_mappings[msg]
        parsed_data = main_collector(city=city_name)
        if parsed_data:
            response_text = "\n".join([
                f"Currency: {item['currency']}\n"
                f"Buy Price: {item['buy_price']}\n"
                f"Sell Price: {item['sell_price']}\n"
                for item in parsed_data
            ])
            await message.answer(response_text)
        else:
            await message.answer("Ошибка при получении данных.")
    elif msg == "назад":
        await message.answer('Назад', reply_markup=main_keyboard())


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())