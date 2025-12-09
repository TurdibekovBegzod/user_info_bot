from aiogram import Bot, Dispatcher
from asyncio import run
import functions

dp = Dispatcher()
bot = Bot(token = "6620860143:AAGjxFbxbSMSsu0_Xxk52zHEpghKsNkfx_4")
#=========================
async def startup(bot : Bot):
    await bot.send_message(chat_id = 6076315346, text = "Bot ishga tushdi! ✅")

async def shutdown(bot : Bot):
    await bot.send_message(chat_id = 6076315346, text = "Bot ishga tushmadi! ❌")


#=====================================
async def main():
    dp.startup.register(startup)
    dp.message.register(functions.get_user_info)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot)

run(main())