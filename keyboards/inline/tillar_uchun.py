from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

tillar_bot=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tilda davom etirish",callback_data='til1'),
            InlineKeyboardButton(text="Rus tilda davom etirish",callback_data='til2')
        ],
        [
            InlineKeyboardButton(text="Ulashing" , switch_inline_query='https://rtm.uzedu.uz/uz'),
            InlineKeyboardButton(text="Hamkorlarmiz" , url='https://t.me/yusufxon_king')
        ],

        [
            InlineKeyboardButton(text="Eng tilda davom etirish",callback_data='til3')
        ]
    ]
)