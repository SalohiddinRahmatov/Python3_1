from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

computer = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Samsung PC'),
            KeyboardButton(text='ASUS')
        ],
        [
            KeyboardButton(text='iMac'),
            KeyboardButton(text='aser')
        ],
        [
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True
)