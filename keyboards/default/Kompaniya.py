from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kompaniya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Tecno'),
            KeyboardButton(text='LG')
        ],
        [
            KeyboardButton(text='Microsoft'),
            KeyboardButton(text='Nokia')
        ],
        [
            KeyboardButton(text='NOVEY'),
            KeyboardButton(text='VIVO')
        ],
        [
            KeyboardButton(text='POCO'),
            KeyboardButton(text='Xonor')
        ],
        [
            KeyboardButton(text='Orqaga')
        ]
    ],
    resize_keyboard=True
)