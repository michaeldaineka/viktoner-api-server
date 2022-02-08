from aiogram import Dispatcher, Bot, types
from app import crud

TOKEN = "5290864582:AAFT1szcdsITKnxH6I7i3Nr5FL9viMl3ILw"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["Мой профиль", "Баланс", "Викторина", "Краш", "Обратная связь"]
keyboard.add(*buttons)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    if not crud.user.get_by_id(user_id=message.from_user.id):
        crud.user.create(obj_in=message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=keyboard)


