from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kompiyuterlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Samsung'),
            KeyboardButton(text='ASUS')
        ],
        [
            KeyboardButton(text='iMac'),
            KeyboardButton(text='aser')
        ],
        [
            KeyboardButton(text='Orqaga')
        ]
    ],
    resize_keyboard=True
)