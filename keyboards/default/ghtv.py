from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

прем = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Айфон 7+'),
            KeyboardButton(text='Айфон se ')
        ],
        [
            KeyboardButton(text='Айфон 8'),
            KeyboardButton(text='Айфон 8 +')
        ],
        [
            KeyboardButton(text='Айфон X s'),
            KeyboardButton(text='Айфон X s max')
        ],
        [
            KeyboardButton(text='Айфон X'),
            KeyboardButton(text='Айфон 11')
        ],
        [
            KeyboardButton(text='Айфон 12 pro max'),
            KeyboardButton(text='Айфон 13')
        ],
        [
            KeyboardButton(text='Айфон 13 pro'),
            KeyboardButton(text='Айфон 14 pro max')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
