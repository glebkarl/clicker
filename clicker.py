import pyautogui
print('Вас приветствует Мышеловка V1.0')
print('(C) Глеб Карловский, 2023')
print('Для выхода нажмите <Ctrl+C>.')
w, h = pyautogui.size()
sizeStr = 'Ширина экрана: ' + str(w).rjust(4) + ' Высота экрана: ' + str(h).rjust(4)
print(sizeStr)
while True:
    try:
        count = int(input('Введите количество повторов нажатий: '))
        pyautogui.PAUSE = float(input('Введите время задержки в секундах: '))
        quantity = int(input('Введите количество точек: '))
        positions = {}
        for i in range(quantity):
            input(f'Нажмите <Enter> для {i+1} точки')
            positions[i] = pyautogui.position()
        for i in range(count):
            for n in range(quantity):
                pyautogui.click(positions[n].x, positions[n].y, button='left')
    except Exception:
        print('Что-то пошло не так. Давай заново.')