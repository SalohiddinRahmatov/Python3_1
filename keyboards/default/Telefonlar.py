from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

telefonlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Samsunglar'),
            KeyboardButton(text='Xiaomilar')
        ],
        [
            KeyboardButton(text='Iphonelar'),
            KeyboardButton(text='Chexolar')
        ],
        [
            KeyboardButton(text='Kolgan kompaniyalar'),
            KeyboardButton(text='Orqaga'),
        ]
    ],
    resize_keyboard=True
)