from aiogram import types
from aiogram.types import InputFile
from BOT.bot import dp, bot
from BOT.db import Products, session
from .keyboard_show import *


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви потрапили до телеграм бота '
                                'магазину "Free Style" виберіть тип взуття',
                           reply_markup=kb1)


@dp.message_handler(commands=['КУПИТИ'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Для замовлення напишіть за цим номером "0688040150" '
                                'і вкажіть id товару який ви хочете замовити',
                           reply_markup=kb1)


@dp.message_handler(commands=['Доросле'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали доросле взуття! Виберіть стать',
                           reply_markup=kb2)
    await message.delete()


@dp.message_handler(commands=['Чоловіче'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали чоловіче взуття! Виберіть тип',
                           reply_markup=ikb1)

    await message.delete()


@dp.callback_query_handler(text_contains='чол')
async def boot(call: types.CallbackQuery):
    for instans in session.query(Products).filter_by(name=call.data):
        photo = InputFile(f'/db/static/photos/{instans.photo}')
        await bot.send_photo(chat_id=call.from_user.id,
                             photo=photo)
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n",
                               reply_markup=kb4)


@dp.message_handler(commands=['Жіноче'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали жіноче взуття! Виберіть тип',
                           reply_markup=ikb2)
    await message.delete()


@dp.callback_query_handler(text_contains='жін')
async def boot(call: types.CallbackQuery):
    for instans in session.query(Products).filter_by(name=call.data):
        photo = InputFile(f'db/static/photos/{instans.photo}')
        await bot.send_photo(chat_id=call.from_user.id,
                             photo=photo)
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n",
                               reply_markup=kb4)


@dp.message_handler(commands=['Дитяче'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитяче взуття! Виберіть стать',
                           reply_markup=kb3)
    await message.delete()


@dp.message_handler(commands=['На_хлопчика'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали взуття для хлопчиків! Виберіть тип',
                           reply_markup=ikb3)
    await message.delete()


@dp.callback_query_handler(text_contains='хлопчаче')
@dp.callback_query_handler(text_contains='хлопчачі')
async def boot(call: types.CallbackQuery):
    for instans in session.query(Products).filter_by(name=call.data):
        await bot.send_photo(chat_id=call.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n",
                               reply_markup=kb4)


@dp.message_handler(commands=['На_дівчинку'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали взуття для хлопчиків! Виберіть тип',
                           reply_markup=ikb4)
    await message.delete()


@dp.callback_query_handler(text_contains='дівчаче')
@dp.callback_query_handler(text_contains='дівчачі')
async def boot(call: types.CallbackQuery):
    for instans in session.query(Products).filter_by(name=call.data):
        await bot.send_photo(chat_id=call.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n",
                               reply_markup=kb4)
        my_id = 1142980771
        await bot.sendMessage(chat_id=my_id,
                              text=f'{instans}')


@dp.message_handler(commands=['show_all'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали подивитись усі товари')
    await message.delete()

    for instans in session.query(Products).filter_by():
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n",
                               reply_markup=kb4)
