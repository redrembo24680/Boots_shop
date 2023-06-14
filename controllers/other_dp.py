from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ContentType, Message
from bot import dp, bot
from db import Product, session
from sqlalchemy import select, insert, update, delete

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/Доросле')
b2 = KeyboardButton('/Дитяче')
kb1.add(b1).insert(b2)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/Чоловіче')
b2 = KeyboardButton('/Жіноче')
kb2.add(b1).insert(b2)

kb3 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/На_хлопчика')
b2 = KeyboardButton('/На_дівчинку')
kb3.add(b1).insert(b2)

kb4 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/Кросівки_жін')
b2 = KeyboardButton('/Кеди_жін')
b3 = KeyboardButton('/Сандалі_жін')
b4 = KeyboardButton('/Туфлі_на_підборах')
b5 = KeyboardButton('/Чоботи_жін')
b6 = KeyboardButton('/Балетки')
kb4.add(b1).insert(b2).insert(b3).add(b4).insert(b5).insert(b6)

kb5 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/Кросівки_чол')
b2 = KeyboardButton('/Кеди_чол')
b3 = KeyboardButton('/Сандалі_чол')
b4 = KeyboardButton('/Шльопанці')
b5 = KeyboardButton('/Чоботи_чол')
b6 = KeyboardButton('/Туфлі_чол')
kb5.add(b1).insert(b2).insert(b3).add(b4).insert(b5).insert(b6)


kb6 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/Кросівки_дитячі_хлопчачі')
b2 = KeyboardButton('/Гумове_взуття_дитяче_хлопчаче')
b3 = KeyboardButton('/Черевики_дитячі_хлопчачі')
b4 = KeyboardButton('/Мокасини_дитячі_хлопчачі')
b5 = KeyboardButton('/Мешти_дитячі_хлопчачі')
b6 = KeyboardButton('/Босоніжки_і_сандалі_дитячі_хлопчачі')
kb6.add(b1).insert(b2).insert(b3).add(b4).insert(b5).insert(b6)

kb7 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/Кросівки_дитячі_дівчачі')
b2 = KeyboardButton('/Гумове_взуття_дитяче_дівчаче')
b3 = KeyboardButton('/Черевики_дитячі_дівчачі')
b4 = KeyboardButton('/Мокасини_дитячі_дівчачі')
b5 = KeyboardButton('/Мешти_дитячі_дівчачі')
b6 = KeyboardButton('/Босоніжки_і_сандалі_дитячі_дівчачі')
kb7.add(b1).insert(b2).insert(b3).add(b4).insert(b5).insert(b6)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви потрапили до телеграм бота '
                                'магазину "..." виберіть тип взуття',
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
                           reply_markup=kb5)
    await message.delete()


@dp.message_handler(commands=['Кросівки_чол'])
async def start(message: types.Message):

    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали чоловічі кросівки!')

    await message.delete()
    for instans in session.query(Product).filter_by(name='кросівки_чол'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(commands=['Киди_чол'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали чоловічі кеди!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Киди_чол'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


@dp.message_handler(commands=['Сандалі_чол'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали чоловічі сандалі!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Сандалі_чол'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")



@dp.message_handler(commands=['Шльопанці'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали чоловічі шльпанці!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Шльопанці'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


@dp.message_handler(commands=['Чоботи_чол'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали чоловічі чоботи!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Чоботи_чол'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


@dp.message_handler(commands=['Туфлі_чол'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали чоловічі туфлі!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Туфлі_чол'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")

@dp.message_handler(commands=['Жіноче'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали жіноче взуття! Виберіть тип',
                           reply_markup=kb4)
    await message.delete()


@dp.message_handler(commands=['Кросівки_жін'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали жіночі кросівки!',
                           )
    await message.delete()

    for instans in session.query(Product).filter_by(name='Кросівки_жін'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


@dp.message_handler(commands=['Кеди_жін'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали жіночі кеди!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Кеди_жін'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


@dp.message_handler(commands=['Сандалі_жін'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали жіночі сандалі!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Сандалі_жін'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


@dp.message_handler(commands=['Туфлі_на_підборах'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали туфлі на підборах!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Туфлі_на_підборах'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


@dp.message_handler(commands=['Чоботи_жін'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали жіночі чоботи!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Чоботи_жін'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


@dp.message_handler(commands=['Балетки'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ви вибрали жіночі балетки!',
                           )
    await message.delete()
    for instans in session.query(Product).filter_by(name='Балетки'):
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f'{instans.photo}')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ім'я: {instans.name}\n"
                                    f"id: {instans.id}\n"
                                    f"ціна: {instans.price}\n"
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


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
                                    f"розмір: {instans.size}\n"
                                    f"колір: {instans.color}\n"
                                    f"країна виробник: {instans.country}")


