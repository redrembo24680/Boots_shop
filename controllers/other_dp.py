from aiogram import types
from bot import dp, bot
from db import Product, session
from .keyboard_show import *


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви потрапили до телеграм бота '
                                'магазину "..." виберіть тип взуття',
                           reply_markup=kb1)


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_id(message: Message):
    await message.reply(message.photo[-1].file_id)


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
    for instans in session.query(Product).filter_by(name=call.data):
        await bot.send_photo(chat_id=call.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n")


@dp.message_handler(commands=['Жіноче'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали жіноче взуття! Виберіть тип',
                           reply_markup=ikb2)
    await message.delete()


@dp.callback_query_handler(text_contains='жін')
async def boot(call: types.CallbackQuery):
    for instans in session.query(Product).filter_by(name=call.data):
        await bot.send_photo(chat_id=call.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n")


# @dp.message_handler(commands=['Кросівки_жін'])
# async def start(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Ви вибрали жіночі кросівки!')
#     await message.delete()
#
#     for instans in session.query(Product).filter_by(name='Кросівки_жін'):
#         await bot.send_photo(chat_id=message.from_user.id,
#                              photo=f'{instans.photo}')
#         await bot.send_message(chat_id=message.from_user.id,
#                                text=f"Ім'я: {instans.name}\n"
#                                     f"id: {instans.id}\n"
#                                     f"ціна: {instans.price}\n"
#                                     f"розмір: {instans.size}\n")
#
#
# @dp.message_handler(commands=['Кеди_жін'])
# async def start(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Ви вибрали жіночі кеди!')
#     await message.delete()
#     for instans in session.query(Product).filter_by(name='Кеди_жін'):
#         await bot.send_photo(chat_id=message.from_user.id,
#                              photo=f'{instans.photo}')
#         await bot.send_message(chat_id=message.from_user.id,
#                                text=f"Ім'я: {instans.name}\n"
#                                     f"id: {instans.id}\n"
#                                     f"ціна: {instans.price}\n"
#                                     f"розмір: {instans.size}\n")
#
#
# @dp.message_handler(commands=['Сандалі_жін'])
# async def start(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Ви вибрали жіночі сандалі!')
#     await message.delete()
#     for instans in session.query(Product).filter_by(name='Сандалі_жін'):
#         await bot.send_photo(chat_id=message.from_user.id,
#                              photo=f'{instans.photo}')
#         await bot.send_message(chat_id=message.from_user.id,
#                                text=f"Ім'я: {instans.name}\n"
#                                     f"id: {instans.id}\n"
#                                     f"ціна: {instans.price}\n"
#                                     f"розмір: {instans.size}\n")
#
#
# @dp.message_handler(commands=['Туфлі_на_підборах'])
# async def start(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Ви вибрали туфлі на підборах!')
#     await message.delete()
#     for instans in session.query(Product).filter_by(name='Туфлі_на_підборах'):
#         await bot.send_photo(chat_id=message.from_user.id,
#                              photo=f'{instans.photo}')
#         await bot.send_message(chat_id=message.from_user.id,
#                                text=f"Ім'я: {instans.name}\n"
#                                     f"id: {instans.id}\n"
#                                     f"ціна: {instans.price}\n"
#                                     f"розмір: {instans.size}\n")
#
#
# @dp.message_handler(commands=['Чоботи_жін'])
# async def start(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Ви вибрали жіночі чоботи!')
#     await message.delete()
#     for instans in session.query(Product).filter_by(name='Чоботи_жін'):
#         await bot.send_photo(chat_id=message.from_user.id,
#                              photo=f'{instans.photo}')
#         await bot.send_message(chat_id=message.from_user.id,
#                                text=f"Ім'я: {instans.name}\n"
#                                     f"id: {instans.id}\n"
#                                     f"ціна: {instans.price}\n"
#                                     f"розмір: {instans.size}\n")
#
#
# @dp.message_handler(commands=['Балетки'])
# async def start(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Ви вибрали жіночі балетки!')
#     await message.delete()
#     for instans in session.query(Product).filter_by(name='Балетки'):
#         await bot.send_photo(chat_id=message.from_user.id,
#                              photo=f'{instans.photo}')
#         await bot.send_message(chat_id=message.from_user.id,
#                                text=f"Ім'я: {instans.name}\n"
#                                     f"id: {instans.id}\n"
#                                     f"ціна: {instans.price}\n"
#                                     f"розмір: {instans.size}\n"
#                                )


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
                           reply_markup=kb6)
    await message.delete()


@dp.message_handler(commands=['Кросівки_дитячі_хлопчачі'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитячі кросівки!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Кросівки_дитячі_хлопчачі'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['Гумове_взуття_дитяче_хлопчаче'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитяче гумове взуття!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Гумове_взуття_дитяче_хлопчаче'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['Черевики_дитячі_хлопчачі'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитячі черевики!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Черевики_дитячі_хлопчачі'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['Мокасини_дитячі_хлопчачі'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитячі мокисини!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Мокасини_дитячі_хлопчачі'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['Мешти_дитячі_хлопчачі'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитячі мешти!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Мешти_дитячі_хлопчачі'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['Босоніжки_і_сандалі_дитячі_хлопчачі'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитячі Босоніжки_і_сандалі!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Босоніжки_і_сандалі_дитячі_хлопчачі'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['На_дівчинку'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали взуття для хлопчиків! Виберіть тип',
                           reply_markup=kb7)
    await message.delete()


@dp.message_handler(commands=['Кросівки_дитячі_дівчачі'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитячі кросівки!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Кросівки_дитячі_дівчачі'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['Гумове_взуття_дитяче_дівчаче'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитяче гумове взуття!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Гумове_взуття_дитяче_дівчаче'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['Черевики_дитячі_дівчачі'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитячі черевики!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Черевики_дитячі_дівчачі'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['Мокасини_дитячі_дівчачі'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитячі мокисини!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Мокасини_дитячі_дівчачі'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['Мешти_дитячі_дівчачі'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитячі мешти!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Мешти_дитячі_дівчачі'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['Босоніжки_і_сандалі_дитячі_дівчачі'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали дитячі Босоніжки_і_сандалі!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Босоніжки_і_сандалі_дитячі_дівчачі'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                               )


@dp.message_handler(commands=['show_all'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали подивитись усі товари')
    await message.delete()

    for instans in session.query(Product).filter_by():
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n")


