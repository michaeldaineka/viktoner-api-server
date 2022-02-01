from aiogram import Dispatcher, Bot, types

TOKEN = "5290864582:AAFT1szcdsITKnxH6I7i3Nr5FL9viMl3ILw"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Hello Michael")