import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(commands=["start"])
async def start(message: Message):
    await message.answer(
        "Привет! 🤖 Я твой AI-бот. Бот запущен!"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())