from aiogram import executor
from bot import dp

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)