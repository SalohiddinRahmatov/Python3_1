from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

продукты = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📱Телефоны'),
            KeyboardButton(text='🖥Компиютеры')
        ]
    ],
    resize_keyboard=True
)