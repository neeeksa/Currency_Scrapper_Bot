from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text=f"Выбрать город🏙️")

    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выбери город')


def city_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text=f"Днепр")
    builder.button(text=f"Харьков")
    builder.button(text=f"Киев")
    builder.button(text="Львов")
    builder.button(text="Запорожье")

    builder.button(text="Назад")

    builder.adjust(3, 2)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выбирай')
