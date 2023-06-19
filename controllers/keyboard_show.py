from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentType, Message, InlineKeyboardMarkup, \
    InlineKeyboardButton

ikb = InlineKeyboardMarkup(row_width=2)

ib1 = InlineKeyboardButton(text='Шльпанці', callback_data='Шльопанці_чол')
ib2 = InlineKeyboardButton(text='Кросівки', callback_data='Кросівки_чол')
ib3 = InlineKeyboardButton(text='Кеди', callback_data='Кеди_чол')
ib4 = InlineKeyboardButton(text='Чоботи', callback_data='Чоботи_чол')
ib5 = InlineKeyboardButton(text='Туфлі', callback_data='Туфлі_чол')
ib6 = InlineKeyboardButton(text='Сандалі', callback_data='Сандалі_чол')

ikb.add(ib1).insert(ib2).add(ib3).insert(ib4).add(ib5).insert(ib6)


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