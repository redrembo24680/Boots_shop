import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from sqlalchemy import select, insert, update, delete
import logging
from aiogram import Bot, Dispatcher, executor, types
from settings import Settings
import asyncio
import sys
from main import DB_Worker


API_TOKEN='6226396360:AAFPDVmZsjJ5c8cfFt2Ya7gBg7KU_dsUJko'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class CountryForm(StatesGroup):
    title = State()


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton("Add country", callback_data="add_country"),
            ],
        ],
    )
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=markup)



@dp.message_handler(commands=["add_country"], state="*")
async def add_country(message: types.Message):
    await CountryForm.title.set()
    await message.reply(f"What country title to add for?\n")


@dp.message_handler(state=CountryForm.title)
async def insert_country(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await state.finish()

    with DB_Worker as db:
        try:
            db.insert('countries', data)
            db.values(message.text)
            await message.reply(f"{data['title']} was added to db")

        except Exception as e:
            await message.reply(f"{data['title']} wasn't added Error {e}'")

    await CountryForm.next()
    await message.reply("How old are you?")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)












