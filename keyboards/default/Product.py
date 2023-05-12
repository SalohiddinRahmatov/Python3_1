from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

product = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📱Phons'),
            KeyboardButton(text='🖥Computers')
        ],
        [
            KeyboardButton(text='Contact the admin')
        ]
    ],
    resize_keyboard=True
)