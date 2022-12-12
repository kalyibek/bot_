from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

TOKEN = '5697638281:AAHaOUdfaMZI2C1u77M0Vjtmjy3oiXFpSDQ'
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
