import os
import pyautogui
import telegram

from dotenv import load_dotenv

load_dotenv()
print('Вас приветствует Мышеловка V1.1')
print('(C) Глеб Карловский, 2023')
print('Для выхода нажмите <Ctrl+C>.')
pyautogui.FAILSAFE = True
w, h = pyautogui.size()
sizeStr = 'Ширина экрана: ' + str(w).rjust(4) + ' Высота экрана: ' + str(h).rjust(4)
print(sizeStr)
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


def send_message(bot, message):
    try:
        bot.send_message(TELEGRAM_CHAT_ID, message)
    except Exception:
        pass


bot = telegram.Bot(token=TELEGRAM_TOKEN)
send_message(bot, 'Пользователь запустил Мышеловку')

while True:
    try:
        count = int(input('Введите количество повторов нажатий: '))
        pyautogui.PAUSE = float(input('Введите время задержки в секундах: '))
        quantity = int(input('Введите количество точек: '))
        positions = {}
        for i in range(quantity):
            input(f'Нажмите <Enter> для {i+1} точки')
            positions[i] = pyautogui.position()
        message = f'count={count}, quantity={quantity}, positions={positions}'
        send_message(bot, message)
        for i in range(count):
            for n in range(quantity):
                pyautogui.click(positions[n].x, positions[n].y, button='left')
    except Exception:
        print('Что-то пошло не так. Давай заново.')
