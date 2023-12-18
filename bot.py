from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

token = "5841737401:AAHMEOnwuxnXLrKSi6V7GrYohC_StKpQYAc"
bot = Bot(token)
dp = Dispatcher(bot)
keyboard = InlineKeyboardMarkup()
menu = InlineKeyboardButton('Меню', callback_data="menu")
keyboard.add(menu)

faq = InlineKeyboardMarkup(row_width=1)
b1 = InlineKeyboardButton('Где можно пойти на перекур', callback_data="q1")
b2 = InlineKeyboardButton('Где лучше покушать', callback_data="q2")
b3 = InlineKeyboardButton('Для иностранных студентов', callback_data='q3')
b4 = InlineKeyboardButton('Опллата услуг', callback_data="q4")
b5 = InlineKeyboardButton('Дресс-код', callback_data="q5")
faq.add(b1, b2, b3, b4, b5)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    privet = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('FAQ', callback_data="faq")
    privet.add(b1)
    await bot.send_message(message.from_user.id,
                           text="Здравстуйте!\nЯ могу помочь вам с учёбой в ОмГТУ!",
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
                           "Перекур у входа в восьмой корпус и за пределами территории ОмГТУ.",
                           reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "q2")
async def question2(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id,
                           "Около восьмого корпуса располагается ТК 'Терминал' с достаточно обширным фуд-кортом.\n Ну или можно ходить в кафе в корусе в котором вы находитесь",
                           reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "q3")
async def question3(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id,
                           "Информацию о поддержке иностранных студентов, пересечении границ, стажировках, получении диплома европейского образца можно уточнить в отделе международных отношений ОмГТУ: interdepomgtu@gmail.com, 8 (3812) 65-64-92.",
                           reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "q4")
async def question4(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id,
                           "Оплатить обучение и общежитие можно с помощью онлайн-сервиса на сайте вуза. Вопросы об оплате можно задать специалистам отдела договорных отношений.",
                           reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "q5")
async def question5(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Приходить можно во всём, кроме нижнего белья и шорт",
                           reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == "menu")
async def menu(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "FAQ", reply_markup=faq)
    await call.message.delete()
