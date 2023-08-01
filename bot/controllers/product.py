from BOT.bot import dp, bot
from BOT.db import Products, session
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from .keyboard_add import *


class ProductForm(StatesGroup):
    name = State()
    age_category = State()
    gender = State()
    size = State()
    price = State()
    photo = State()


class DeleteProductForm(StatesGroup):
    id = State()


@dp.message_handler(commands=["add_product"], state="*")
async def add_product(message: types.Message):
    await ProductForm.next()
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"What product name to add for?\n",
                           reply_markup=kb1)


@dp.message_handler(state=ProductForm.name)
async def insert_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await ProductForm.next()
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"What age category of product  to add for?\n",
                           reply_markup=kb3)


@dp.message_handler(state=ProductForm.age_category)
async def insert_product_age_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age_category'] = message.text

    await ProductForm.next()
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"What product gender to add for?\n",
                           reply_markup=kb4)


@dp.message_handler(state=ProductForm.gender)
async def insert_product_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    await ProductForm.next()
    await message.reply(f"What product size to add for?\n",
                        reply_markup=kb2)


@dp.message_handler(state=ProductForm.size)
async def insert_product_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await ProductForm.next()
    await message.reply(f"What product price to add for?\n",
                        reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=ProductForm.price)
async def insert_product_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await ProductForm.next()
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"What product photo to add for?\n")


@dp.message_handler(state=ProductForm.photo, content_types=types.ContentTypes.PHOTO)
async def insert_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        photos = message.photo[-1]
        file = await photos.get_file()
        file_name = file.file_path.split('/')[-1]

        photo = message.photo[-1]
        photo_id = photo.file_id
        files = await bot.get_file(photo_id)
        file_paths = files.file_path
        await bot.download_file(file_paths, f'..boots_shop/{file_name}')
        data['photo'] = file_name

    try:

        session.add(
            Products(name=data.get('name'), age_category=data.get('age_category'), gender=data.get('gender'), size=data.get('size'), price=data.get('price'),
                    photo=data.get('photo')))
        session.commit()
        await message.reply(f"{data['name']} was add to db")
    except Exception as e:
        session.rollback()
        await message.reply(f"{data['name']} wasn't add to db. Error{e}")

    await state.finish()


@dp.message_handler(commands=["delete_product"], state="*")
async def delete_product(message: types.Message):
    await DeleteProductForm.id.set()
    await message.reply(f"What product id to delete for?\n")


@dp.message_handler(state=DeleteProductForm.id)
async def insert_product_country(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text

    try:
        for delete_product in session.query(Products).filter_by(id=data.get('id')):
            session.delete(delete_product)
            session.commit()
            await message.reply(f"Product with id: {message.text} was deleted from db")
    except Exception as e:
        session.rollback()
        await message.reply(f"Product with it's id: {message.text} wasn't deleted to db. Error{e}")
    await state.finish()

