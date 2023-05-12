from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

lk = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Yes'),
            KeyboardButton(text="Now")
        ]
    ],
    resize_keyboard=True
)