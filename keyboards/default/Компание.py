from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

компание = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Техно'),
            KeyboardButton(text='ЛЖ')
        ],
        [
            KeyboardButton(text='Микрософт'),
            KeyboardButton(text='Нокиа')
        ],
        [
            KeyboardButton(text='НОВЕЙ'),
            KeyboardButton(text='Виво')
        ],
        [
            KeyboardButton(text='ПОКО'),
            KeyboardButton(text='Хонор')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)