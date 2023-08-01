from BOT.bot import executor, dp
import BOT.controllers

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


