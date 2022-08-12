from aiogram import types
from aiogram.utils import executor
from config import bot, dp




@dp.message_handler(commands=['start'])
async def send(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello {message.from_user.full_name}")

@dp.message_handler(commands=['quiz'])
async def quiz_1(massage: types.Message):

    question = "Кто выйграет войну?"
    answers = [
            "Россия",
            "Украина"
        ]

    await bot.send_poll(
            chat_id=massage.chat.id,
            question=question,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=0,
            open_period=10
        )


@dp.message_handler(commands='mem')
async def mem(message):
    photo = open('media/memchik.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
