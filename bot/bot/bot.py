import logging
from BOT.settings import Settings
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

logging.basicConfig(level=logging.INFO)

bot = Bot(token=Settings.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

