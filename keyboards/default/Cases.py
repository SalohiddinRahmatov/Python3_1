from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

case = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='to Samsun'),
            KeyboardButton(text='to Xiaomi')
        ],
        [
            KeyboardButton(text='to Iphon'),
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True
)