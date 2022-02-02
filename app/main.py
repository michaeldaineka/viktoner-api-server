from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot
from bot import dp, bot, TOKEN
import uvicorn


app = FastAPI()
WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = "https://05e5-178-124-178-56.ngrok.io" + WEBHOOK_PATH


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    session = await bot.get_session()
    await session.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)