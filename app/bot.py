from aiogram import Dispatcher, Bot, types
from app.crud import user
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api import deps


TOKEN = "5290864582:AAFT1szcdsITKnxH6I7i3Nr5FL9viMl3ILw"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    print(user.get_by_id(user_id=message.from_user.id))
    await message.answer(message.from_user.id)