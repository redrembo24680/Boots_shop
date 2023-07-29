from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentType, Message, InlineKeyboardMarkup, \
    InlineKeyboardButton, ReplyKeyboardRemove

ikb1 = InlineKeyboardMarkup(row_width=2)

ib1 = InlineKeyboardButton(text='Шльпанці', callback_data='Шльопанці_чол')
ib2 = InlineKeyboardButton(text='Кросівки', callback_data='Кросівки_чол')
ib3 = InlineKeyboardButton(text='Кеди', callback_data='Кеди_чол')
ib4 = InlineKeyboardButton(text='Чоботи', callback_data='Чоботи_чол')
ib5 = InlineKeyboardButton(text='Туфлі', callback_data='Туфлі_чол')
ib6 = InlineKeyboardButton(text='Сандалі', callback_data='Сандалі_чол')

ikb1.add(ib1).insert(ib2).insert(ib3).add(ib4).insert(ib5).insert(ib6)

ikb2 = InlineKeyboardMarkup(row_width=2)

ib1 = InlineKeyboardButton(text='Кросівки', callback_data='Кросівки_жін')
ib2 = InlineKeyboardButton(text='Кеди', callback_data='Кеди_жін')
ib3 = InlineKeyboardButton(text='Сандалі', callback_data='Сандалі_жін')
ib4 = InlineKeyboardButton(text='Туфлі_на_підборах', callback_data='Туфлі_на_підборах_жін')
ib5 = InlineKeyboardButton(text='Чоботи', callback_data='Чоботи_жін')
ib6 = InlineKeyboardButton(text='Балетки', callback_data='Балетки_жін')

ikb2.add(ib1).insert(ib2).add(ib3).insert(ib4).add(ib5).insert(ib6)

ikb3 = InlineKeyboardMarkup(row_width=2)

ib1 = InlineKeyboardButton(text='Кросівки', callback_data='Кросівки_дитячі_хлопчачі')
ib2 = InlineKeyboardButton(text='Гумове_взуття_дитяче', callback_data='Гумове_взуття_дитяче_хлопчаче')
ib3 = InlineKeyboardButton(text='Черевики_дитячі', callback_data='Черевики_дитячі_хлопчачі')
ib4 = InlineKeyboardButton(text='Мокасини_дитячі', callback_data='Мокасини_дитячі_хлопчачі')
ib5 = InlineKeyboardButton(text='Мешти_дитячі', callback_data='Мешти_дитячі_хлопчачі')
ib6 = InlineKeyboardButton(text='Босоніжки_дитячі', callback_data='Босоніжки_дитячі_хлопчачі')

ikb3.add(ib1).insert(ib2).add(ib3).insert(ib4).add(ib5).insert(ib6)


ikb4 = InlineKeyboardMarkup(row_width=2)

ib1 = InlineKeyboardButton(text='Кросівки', callback_data='Кросівки_дитячі_дівчачі')
ib2 = InlineKeyboardButton(text='Кеди', callback_data='Гумове_взуття_дитяче_дівчаче')
ib3 = InlineKeyboardButton(text='Сандалі', callback_data='Черевики_дитячі_дівчачі')
ib4 = InlineKeyboardButton(text='Туфлі_на_підборах', callback_data='Мокасини_дитячі_дівчачі')
ib5 = InlineKeyboardButton(text='Мешти_дитячі', callback_data='Мешти_дитячі_дівчачі')
ib6 = InlineKeyboardButton(text='Босоніжки_дитячі', callback_data='Босоніжки_дитячі_дівчачі')

ikb4.add(ib1).insert(ib2).add(ib3).insert(ib4).add(ib5).insert(ib6)

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
