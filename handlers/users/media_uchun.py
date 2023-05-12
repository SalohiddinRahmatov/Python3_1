from aiogram import types
from aiogram.types import ContentTypes

from loader import dp


# Echo bot
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    await message.answer(text='Rasm qabul qilindi! rasm uchun raxmat!')
