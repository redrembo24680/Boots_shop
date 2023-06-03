from bot import dp
from db import Product
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
'''id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=False
    )
    name = Column(
        Unicode(225),
        unique=True,
        nullable=False
    )
    size = Column(
        Float(2),
        nullable=False
    )
    prize = Column(
        Float(2),
        nullable=False
    )'''
class ProductForm(StatesGroup):
    name = State()
    size = State()
    prize = State()



@dp.message_handler(commands=["add_product"], state="*")
async def add_country(message: types.Message):
    await ProductForm.name.set()
    await message.reply(f"What country title to add for?\n")


@dp.message_handler(state=ProductForm.name)
async def insert_country(message: types.Message, state: FSMContext, session: AsyncSession):
    async with state.proxy() as data:
        data['title'] = message.text
    await state.finish()
    try:
        sql = insert(Product).values(title=data['title'])
        await session.execute(sql)
        await message.reply(f"{data['title']} was add to db")
    except Exception as e:
        await session.rollback()
        await message.reply(f"{data['title']} wasn't add to db. Error{e}")

    await ProductForm.next()
    await message.reply(f"What country title to add for?\n")