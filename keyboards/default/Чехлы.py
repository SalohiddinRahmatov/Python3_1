from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

чехол = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Для самсунга'),
            KeyboardButton(text='Для хиаоми')
        ],
        [
            KeyboardButton(text='Для айфона'),
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)