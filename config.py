from aiogram import Bot, Dispatcher
from decouple import config


TOKEN = config("TOKEN", default="ERROR")
print(TOKEN)
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)