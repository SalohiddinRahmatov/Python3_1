from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

телефоны = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Самсунг'),
            KeyboardButton(text='Хиаоми')
        ],
        [
            KeyboardButton(text='Айфон'),
            KeyboardButton(text='Чехлы')
        ],
        [
            KeyboardButton(text='Другие похожие компание'),
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)