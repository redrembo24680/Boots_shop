from bot import dp
from db import Country, session
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types


class CountryForm(StatesGroup):
    tittle = State()


@dp.message_handler(commands=["add_country"], state="*")
async def add_country(message: types.Message):
    await CountryForm.tittle.set()
    await message.reply(f"What country title to add for?\n")


@dp.message_handler(state=CountryForm.tittle)
async def insert_country(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tittle'] = message.text
    await state.finish()
    session.add(Country(tittle=data.get('tittle')))
    try:
        session.commit()
        await message.reply(f"{data['tittle']} was add to db")
    except Exception as e:
        session.rollback()
        await message.reply(f"{data['tittle']} wasn't add to db. Error: {e}")

