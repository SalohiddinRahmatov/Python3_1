from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

chexol = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Samsunga'),
            KeyboardButton(text='Xiaomiga')
        ],
        [
            KeyboardButton(text='Iphonga'),
            KeyboardButton(text='Orqaga')
        ]
    ],
    resize_keyboard=True
)