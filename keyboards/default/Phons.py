from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

phon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Samsung'),
            KeyboardButton(text='Xiaomi')
        ],
        [
            KeyboardButton(text='Iphone'),
            KeyboardButton(text='Cases')
        ],
        [
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True
)