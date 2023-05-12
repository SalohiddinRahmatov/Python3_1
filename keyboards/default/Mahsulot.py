from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

mahsulotlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📱Telefonlar'),
            KeyboardButton(text='🖥Kompiyuterlar')
        ],
        [
            KeyboardButton(text='Adminga murojat')
        ]
    ],
    resize_keyboard=True
)