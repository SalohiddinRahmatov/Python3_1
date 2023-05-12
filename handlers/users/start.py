from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.Mahsulot import mahsulotlar
from keyboards.default.Продукт import продукты
from keyboards.default.Product import product
from keyboards.default.Компиютеры import компиютеры
from keyboards.default.Kompiyuterlar import kompiyuterlar
from keyboards.default.Computers import computer
from keyboards.default.Kompaniya import kompaniya
from keyboards.default.Telefonlar import telefonlar
from keyboards.default.Phons import phon
from keyboards.default.Телефоны import телефоны
from keyboards.default.Чехлы import чехол
from keyboards.default.ghtv import прем
from keyboards.default.Самсунг import самсунг
from keyboards.default.Компание import компание
from keyboards.default.Rusumi import samsung
from keyboards.default.Rusumi import rusumi
from keyboards.default.Cases import case
from keyboards.default.Chexolar import chexol
from keyboards.inline.tillar_uchun import tillar_bot
from loader import dp,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Tilni tanlang,{message.from_user.full_name}",reply_markup=tillar_bot)


@dp.callback_query_handler(text="til1")
async def bot_start(xabar:CallbackQuery):
    await xabar.message.answer(f"Salom, siz Ozbek tilini tanladingiz!",reply_markup=mahsulotlar)

@dp.callback_query_handler(text="til2")
async def bot_start(xabar:CallbackQuery):
    await xabar.message.answer(f"Здраствуйте, вы выбрали Русский язык!",reply_markup=продукты)

@dp.callback_query_handler(text="til3")
async def bot_start(xabar:CallbackQuery):
    await xabar.message.answer(f"Hello, you have selected English!",reply_markup=product)

@dp.message_handler(text='🖥Kompiyuterlar')
async def bot_start(message: types.Message):
    await message.answer(text=f"Kompiyuterni tanglang!",reply_markup=kompiyuterlar)

@dp.message_handler(text='')
async def bot_start(message: types.Message):
    await message.answer(text=f"Kompiyuterni tanglang!",reply_markup=kompiyuterlar)


@dp.message_handler(text='Kolgan kompaniyalar')
async def bot_start(message: types.Message):
    await message.answer(text=f"Kompiyuterni tanglang!",reply_markup=kompaniya)

@dp.message_handler(text="Другие похожие компание")
async def bot_start(message: types.Message):
    await message.answer(f"Hello, you have selected English!",reply_markup=компание)

@dp.message_handler(text="Айфон")
async def bot_start(message: types.Message):
    await message.answer(f"Выберите телефон!",reply_markup=прем)

@dp.message_handler(text="Самсунг")
async def bot_start(message: types.Message):
    await message.answer(f"Выберите телефон!",reply_markup=самсунг)

@dp.message_handler(text='Samsunglar')
async def bot_start(message: types.Message):
    await message.answer(text=f"Kompiyuterni tanglang!",reply_markup=samsung)


@dp.message_handler(text='🖥Компиютеры')
async def bot_start(message: types.Message):
    await message.answer(text=f"Выберите компиютер!",reply_markup=компиютеры)

@dp.message_handler(text='🖥Computers')
async def bot_start(message: types.Message):
    await message.answer(text=f"Choose computers!",reply_markup=computer)


@dp.message_handler(text='📱Telefonlar')
async def bot_start(message: types.Message):
    await message.answer(text=f"Telefonni tanglang!",reply_markup=telefonlar)

@dp.message_handler(text='Iphonelar')
async def bot_start(message: types.Message):
    await message.answer(text=f"Telefonni tanglang!",reply_markup=rusumi)


@dp.message_handler(text='📱Телефоны')
async def bot_start(message: types.Message):
    await message.answer(text=f"Выберите телефон!",reply_markup=телефоны)

@dp.message_handler(text='Чехлы')
async def bot_start(message: types.Message):
    await message.answer(text=f"Выберите чехол!",reply_markup=чехол)


@dp.message_handler(text='Iphone 7+')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/2'
    await bot.send_photo(chat_id=user_id,photo=rasm)

@dp.message_handler(text='Iphone 8')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/3'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Iphone X s')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/4'
    await bot.send_photo(chat_id=user_id,photo=rasm)



@dp.message_handler(text='Iphone X')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/5'
    await bot.send_photo(chat_id=user_id,photo=rasm)



@dp.message_handler(text='Iphone se')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/6'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Iphone 8 +')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/7'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Iphone X s max')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/8'
    await bot.send_photo(chat_id=user_id,photo=rasm)



@dp.message_handler(text='Iphone 11')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/9'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Iphone 12 pro max')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/10'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Iphone 13')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/11'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Iphone 13 pro')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/12'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Iphone 14 pro max')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/13'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Samsung A7')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/14'
    await bot.send_photo(chat_id=user_id,photo=rasm)

@dp.message_handler(text='Samsung A10 s')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/15'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Samsung S10+')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/16'
    await bot.send_photo(chat_id=user_id,photo=rasm)



@dp.message_handler(text='Samsung A32 s')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/17'
    await bot.send_photo(chat_id=user_id,photo=rasm)



@dp.message_handler(text='Samsung A33')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/18'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Samsung A50')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/19'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Samsung A51')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/20'
    await bot.send_photo(chat_id=user_id,photo=rasm)



@dp.message_handler(text='Samsung A52')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/21'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Samsung S 9')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/22'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Samsung S 23 Ultra')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/26'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Samsung S20')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/25'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Samsung S22')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    rasm = 'https://t.me/asalomu_alaykum_giybatchilar/24'
    await bot.send_photo(chat_id=user_id,photo=rasm)


@dp.message_handler(text='Chexolar')
async def bot_start(message: types.Message):
    await message.answer(text=f"Chexolni tanglang!",reply_markup=chexol)


@dp.message_handler(text='Cases')
async def bot_start(message: types.Message):
    await message.answer(text=f"Choose case!",reply_markup=case)


@dp.message_handler(text='📱Phons')
async def bot_start(message: types.Message):
    await message.answer(text=f"Select a phone!",reply_markup=phon)


@dp.message_handler(text='Orqaga')
async def bot_start(message: types.Message):
    await message.answer(f"Mahsulotni tanglang,{message.from_user.full_name}",reply_markup=mahsulotlar)

@dp.message_handler(text='Назад')
async def bot_start(message: types.Message):
    await message.answer(f"Выберите продукт!,{message.from_user.full_name}",reply_markup=продукты)


@dp.message_handler(text='Back')
async def bot_start(message: types.Message):
    await message.answer(f"Choose a product!,{message.from_user.full_name}",reply_markup=product)



@dp.message_handler(commands='boshlash')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, botga hush kelibsiz!,{message.from_user.full_name}")