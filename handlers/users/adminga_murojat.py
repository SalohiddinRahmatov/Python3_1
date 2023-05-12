from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from states.holatlar import Murojaat
from loader import dp,bot
from keyboards.default.tastiqlash import tastiqlash
from keyboards.default.Mahsulot import mahsulotlar

# Echo bot
@dp.message_handler(text='Adminga murojat')
async def bot_echo(message: types.Message):
    await message.answer(text='Ismingizni kiriting',reply_markup=ReplyKeyboardRemove())
    await Murojaat.ism_qabul_qilish.set()

@dp.message_handler(state=Murojaat.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'ism':matn})
    await message.answer(text='Familiyangizni kiriting')
    await Murojaat.familya_qabul_qilish.set()

@dp.message_handler(state=Murojaat.familya_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'fam':matn})
    await message.answer(text='Yoshingizni kiriting')
    await Murojaat.yosh_qabul_qilish.set()

@dp.message_handler(state=Murojaat.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'yosh':matn})
    await message.answer(text='Telefon raqamingizni kiriting kiriting')
    await Murojaat.tel_qabul_qilish.set()

@dp.message_handler(state=Murojaat.tel_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'tel':matn})
    await message.answer(text='Murojatingizni kiriting')
    await Murojaat.murojat_qabul_qilish.set()

@dp.message_handler(state=Murojaat.murojat_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'murojaat':matn})
    malumot = await state.get_data()
    ismi = malumot.get('ism')
    familiya = malumot.get('fam')
    yosh = malumot.get('yosh')
    tel = malumot.get('tel')
    murojaat = malumot.get('murojaat')

    textt= f"Ism : {ismi}\n" \
           f"Fam : {familiya}\n" \
           f"Yosh : {yosh}\n" \
           f"Tel : {tel}\n" \
           f"Murojaat : {murojaat}\n" \

    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text=textt,reply_markup=tastiqlash)
    await Murojaat.tastiqlash_holati.set()

@dp.message_handler(state=Murojaat.tastiqlash_holati,text="Yo'q")
async def bot_echo(message: types.Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="Yo'q",reply_markup=mahsulotlar)
    await state.finish()

@dp.message_handler(state=Murojaat.tastiqlash_holati,text="Xa")
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'murojaat':matn})
    malumot = await state.get_data()
    ismi = malumot.get('ism')
    familiya = malumot.get('fam')
    yosh = malumot.get('yosh')
    tel = malumot.get('tel')
    murojaat = malumot.get('murojaat')

    textt= f"Ism : {ismi}\n" \
           f"Fam : {familiya}\n" \
           f"Yosh : {yosh}\n" \
           f"Tel : {tel}\n" \
           f"Murojaat : {murojaat}\n" \

    await bot.send_message(chat_id='777933252',text=textt)
    await bot.send_message(chat_id=message.from_user.id,text="Adminga yuborildi",reply_markup=mahsulotlar)
    await state.finish()


