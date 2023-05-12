from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

rusumi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Iphone 7+'),
            KeyboardButton(text='Iphone se ')
        ],
        [
            KeyboardButton(text='Iphone 8'),
            KeyboardButton(text='Iphone 8 +')
        ],
        [
            KeyboardButton(text='Iphone X s'),
            KeyboardButton(text='Iphone X s max')
        ],
        [
            KeyboardButton(text='Iphone X'),
            KeyboardButton(text='Iphone 11')
        ],
        [
            KeyboardButton(text='Iphone 12 pro max'),
            KeyboardButton(text='Iphone 13')
        ],
        [
            KeyboardButton(text='Iphone 13 pro'),
            KeyboardButton(text='Iphone 14 pro max')
        ],
        [
            KeyboardButton(text='Orqaga')
        ]
    ],
    resize_keyboard=True
)

samsung = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Samsung A7'),
            KeyboardButton(text='Samsung A10 s')
        ],
        [
            KeyboardButton(text='Samsung S10+'),
            KeyboardButton(text='Samsung A32 s')
        ],
        [
            KeyboardButton(text='Samsung A33'),
            KeyboardButton(text='Samsung A50')
        ],
        [
            KeyboardButton(text='Samsung A51'),
            KeyboardButton(text='Samsung A52')
        ],
        [
            KeyboardButton(text='Samsung S 9'),
            KeyboardButton(text='Samsung S20')
        ],
        [
            KeyboardButton(text='Samsung S22'),
            KeyboardButton(text='Samsung S 23 Ultra')
        ],
        [
            KeyboardButton(text='Orqaga')
        ]
    ],
    resize_keyboard=True
)