from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # Токен нужно указать в Render → Environment

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопки
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    KeyboardButton("Нархнома 💱"),
    KeyboardButton("Тафтиши трек-код ♻️"),
)
keyboard.add(
    KeyboardButton("Суроғаи мо 📍"),
    KeyboardButton("Тарзи пур кардани адрес ㊙️"),
)
keyboard.add(
    KeyboardButton("Молҳои манъшуда 🚫"),
)

# Обработчик /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Салом! Ман боти ширкати ONLINE CARGO TJ ҳастам. Лутфан, фармонро интихоб кунед:", reply_markup=keyboard)

# Обработчик всех кнопок
@dp.message_handler(lambda message: message.text)
async def handle_message(message: types.Message):
    text = message.text

    if text == "Нархнома 💱":
        await message.reply("Лутфан барои нархнома бо оператор тамос гиред.")

    elif text == "Тафтиши трек-код ♻️":
        await message.reply("Лутфан трек-кодро фиристед ва ман онро тафтиш мекунам.")

    elif text == "Суроғаи мо 📍":
        await message.reply("ш. Душанбе, н. Фирдавси")

    elif text == "Тарзи пур кардани адрес ㊙️":
        await message.reply_photo(photo=open("address-example.jpg", "rb"), caption="Ин намунаи пур кардани адрес дар Чин мебошад.")

    elif text == "Молҳои манъшуда 🚫":
        await message.reply(
            "Молҳои манъшуда:\n"
            "- Вейпҳо\n"
            "- Кальяны\n"
            "- Ҳамаи намудҳои силоҳ (ҳатто бозичаҳо)\n"
            "- Маҳсулоти 18+\n"
  
        )
    else:
        await message.reply("Лутфан яке аз тугмаҳоро интихоб кунед.")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
