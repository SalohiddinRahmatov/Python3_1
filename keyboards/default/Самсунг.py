from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

самсунг = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Самсунг A7'),
            KeyboardButton(text='Самсунг A10 s')
        ],
        [
            KeyboardButton(text='Самсунг SX10'),
            KeyboardButton(text='Самсунг A32 s')
        ],
        [
            KeyboardButton(text='Самсунг A33'),
            KeyboardButton(text='Самсунг A50')
        ],
        [
            KeyboardButton(text='Самсунг A51'),
            KeyboardButton(text='Самсунг A52')
        ],
        [
            KeyboardButton(text='Самсунг S 9'),
            KeyboardButton(text='Самсунг 22')
        ],
        [
            KeyboardButton(text='Самсунг S22s'),
            KeyboardButton(text='Самсунг S 23 Ultra')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)