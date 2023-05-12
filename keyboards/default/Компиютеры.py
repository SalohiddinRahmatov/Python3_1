from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

компиютеры = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Самсунг ПК'),
            KeyboardButton(text='Асус')
        ],
        [
            KeyboardButton(text='айМак'),
            KeyboardButton(text='эйсер')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)