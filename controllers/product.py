from bot import dp, bot
from db import Product, session
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import types
from sqlalchemy import select, insert, update, delete

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Кросівки_жін')
b2 = KeyboardButton('Кеди_жін')
b3 = KeyboardButton('Сандалі_жін')
b4 = KeyboardButton('Туфлі_на_підборах')
b5 = KeyboardButton('Чоботи_жін')
b6 = KeyboardButton('Балетки')
b7 = KeyboardButton('Кросівки_чол')
b8 = KeyboardButton('Кеди_чол')
b9 = KeyboardButton('Сандалі_чол')
b10 = KeyboardButton('Шльопанці')
b11 = KeyboardButton('Чоботи_чол')
b12 = KeyboardButton('Туфлі_чол')
b13 = KeyboardButton('/Кросівки_дитячі_хлопчачі')
b14 = KeyboardButton('/Гумове_взуття_дитяче_хлопчаче')
b15 = KeyboardButton('/Черевики_дитячі_хлопчачі')
b16 = KeyboardButton('/Мокасини_дитячі_хлопчачі')
b17 = KeyboardButton('/Мешти_дитячі_хлопчачі')
b18 = KeyboardButton('/Босоніжки_і_сандалі_дитячі_хлопчачі')
b19 = KeyboardButton('/Кросівки_дитячі_дівчачі')
b20 = KeyboardButton('/Гумове_взуття_дитяче_дівчаче')
b21 = KeyboardButton('/Черевики_дитячі_дівчачі')
b22 = KeyboardButton('/Мокасини_дитячі_дівчачі')
b23 = KeyboardButton('/Мешти_дитячі_дівчачі')
b24 = KeyboardButton('/Босоніжки_і_сандалі_дитячі_дівчачі')
kb1.add(b1).insert(b2).insert(b3).add(b4).insert(b5).insert(b6).add(b7).insert(b8).insert(b9).add(b10).insert(b11).insert(b12).add(b13).insert(b14).insert(b15).add(b16).insert(b17).insert(b18).add(b19).insert(b20).insert(b21).add(b22).insert(b23).insert(b24)


kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('19')
b2 = KeyboardButton('20')
b3 = KeyboardButton('21')
b4 = KeyboardButton('22')
b5 = KeyboardButton('23')
b6 = KeyboardButton('24')
b7 = KeyboardButton('25')
b8 = KeyboardButton('26')
b9 = KeyboardButton('27')
b10 = KeyboardButton('28')
b11 = KeyboardButton('29')
b12 = KeyboardButton('30')
b13 = KeyboardButton('31')
b14 = KeyboardButton('32')
b15 = KeyboardButton('33')
b16 = KeyboardButton('34')
b17 = KeyboardButton('35')
b18 = KeyboardButton('36')
b19 = KeyboardButton('37')
b20 = KeyboardButton('38')
b21 = KeyboardButton('39')
b22 = KeyboardButton('40')
b23 = KeyboardButton('41')
b24 = KeyboardButton('42')
b25 = KeyboardButton('43')
b26 = KeyboardButton('44')
b27 = KeyboardButton('45')
b28 = KeyboardButton('46')
kb2.add(b1).insert(b2).insert(b3).add(b4).insert(b5).insert(b6).add(b7).insert(b8).insert(b9).add(b10).insert(b11).insert(b12).add(b13).insert(b14)\
    .insert(b15).add(b16).insert(b17).insert(b18).add(b19).insert(b20).insert(b21).add(b22).insert(b23).insert(b24).add(b25).insert(b26).insert(b27).add(b28)



class ProductForm(StatesGroup):
    name = State()
    size = State()
    price = State()
    color = State()
    country = State()
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
                           text=f"What product size to add for?\n",
                           reply_markup=kb2)


@dp.message_handler(state=ProductForm.size)
async def insert_product_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await ProductForm.next()
    await message.reply(f"What product price to add for?\n", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=ProductForm.price)
async def insert_product_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await ProductForm.next()
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"What product color to add for?\n")


@dp.message_handler(state=ProductForm.color)
async def insert_product_color(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['color'] = message.text

    await ProductForm.next()
    await message.reply(f"What product country to add for?\n")


@dp.message_handler(state=ProductForm.country)
async def insert_product_country(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['country'] = message.text

    await ProductForm.next()
    await message.reply(f"What product photo id to add for?\n")


@dp.message_handler(state=ProductForm.photo)
async def insert_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.text

    try:
        session.add(
            Product(name=data.get('name'), size=data.get('size'), price=data.get('price'), color=data.get('color'),
                    country=data.get('country'), photo=data.get('photo')))
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
        for delete_product in session.query(Product).filter_by(id=data.get('id')):
            session.delete(delete_product)
            session.commit()
            await message.reply(f"Product with id: {message.text} was deleted from db")
    except Exception as e:
        session.rollback()
        await message.reply(f"Product with it's id: {message.text} wasn't deleted to db. Error{e}")
    await state.finish()

