from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from states.holatlar import Murojaat
from loader import dp,bot
from keyboards.default.lk import lk
from keyboards.default.Product import product

# Echo bot
@dp.message_handler(text='Contact the admin')
async def bot_echo(message: types.Message):
    await message.answer(text='Enter your name',reply_markup=ReplyKeyboardRemove())
    await Murojaat.ism_qabul_qilish.set()

@dp.message_handler(state=Murojaat.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'nam':matn})
    await message.answer(text='Enter your last name')
    await Murojaat.familya_qabul_qilish.set()

@dp.message_handler(state=Murojaat.familya_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'sur':matn})
    await message.answer(text='Enter your age')
    await Murojaat.yosh_qabul_qilish.set()

@dp.message_handler(state=Murojaat.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'yers':matn})
    await message.answer(text='Enter your phone number')
    await Murojaat.tel_qabul_qilish.set()

@dp.message_handler(state=Murojaat.tel_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'phon':matn})
    await message.answer(text='Enter your address')
    await Murojaat.murojat_qabul_qilish.set()

@dp.message_handler(state=Murojaat.murojat_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'appeal':matn})
    malumot = await state.get_data()
    ismi = malumot.get('nam')
    familiya = malumot.get('sur')
    yosh = malumot.get('year')
    tel = malumot.get('phon')
    murojaat = malumot.get('appeal')

    textt= f"Name: {ismi}\n" \
           f"Surname: {familiya}\n" \
           f"Years: {yosh}\n" \
           f"Phon: {tel}\n" \
           f"Appeal: {murojaat}\n" \

    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text=textt,reply_markup=lk)
    await Murojaat.tastiqlash_holati.set()

@dp.message_handler(state=Murojaat.tastiqlash_holati,text="Now")
async def bot_echo(message: types.Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="Now",reply_markup=product)
    await state.finish()

@dp.message_handler(state=Murojaat.tastiqlash_holati,text="Yes")
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({'appeal':matn})
    malumot = await state.get_data()
    ismi = malumot.get('nam')
    familiya = malumot.get('sur')
    yosh = malumot.get('year')
    tel = malumot.get('phon')
    murojaat = malumot.get('appeal')

    textt= f"Name: {ismi}\n" \
           f"Surname: {familiya}\n" \
           f"Years: {yosh}\n" \
           f"Phon: {tel}\n" \
           f"Appeal : {murojaat}\n" \

    await bot.send_message(chat_id='777933252',text=textt)
    await bot.send_message(chat_id=message.from_user.id,text="Sent to admin",reply_markup=product)
    await state.finish()


