from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

token = "5841737401:AAHMEOnwuxnXLrKSi6V7GrYohC_StKpQYAc"
bot = Bot(token)
dp = Dispatcher(bot)
keyboard = InlineKeyboardMarkup()
menu = InlineKeyboardButton('����', callback_data="menu")
keyboard.add(menu)

faq = InlineKeyboardMarkup(row_width=1)
b1 = InlineKeyboardButton('��� ����� ����� �� �������', callback_data="q1")
b2 = InlineKeyboardButton('��� ����� ��������', callback_data="q2")
b3 = InlineKeyboardButton('��� ����������� ���������', callback_data='q3')
b4 = InlineKeyboardButton('������� �����', callback_data="q4")
b5 = InlineKeyboardButton('�����-���', callback_data="q5")
faq.add(b1, b2, b3, b4, b5)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    privet = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('FAQ', callback_data="faq")
    privet.add(b1)
    await bot.send_message(message.from_user.id,
                           text="�����������!\n� ���� ������ ��� � ������ � �����!",
                           reply_markup=privet)
    await message.delete()


@dp.callback_query_handler(lambda c: c.data == "faq")
async def main_menu(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "FAQ", reply_markup=faq)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "q1")
async def question1(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id,
                           "������� � ����� � ������� ������ � �� ��������� ���������� �����.",
                           reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "q2")
async def question2(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id,
                           "����� �������� ������� ������������� �� '��������' � ���������� �������� ���-������.\n �� ��� ����� ������ � ���� � ������ � ������� �� ����������",
                           reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "q3")
async def question3(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id,
                           "���������� � ��������� ����������� ���������, ����������� ������, �����������, ��������� ������� ������������ ������� ����� �������� � ������ ������������� ��������� �����: interdepomgtu@gmail.com, 8 (3812) 65-64-92.",
                           reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "q4")
async def question4(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id,
                           "�������� �������� � ��������� ����� � ������� ������-������� �� ����� ����. ������� �� ������ ����� ������ ������������ ������ ���������� ���������.",
                           reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "q5")
async def question5(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "��������� ����� �� ���, ����� ������� ����� � ����",
                           reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "menu")
async def menu(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "FAQ", reply_markup=faq)
    await call.message.delete()
