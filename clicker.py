# Кликер / Clicker
import keyboard                                                     # Импорт модуля keyboard для обработки клавиш
import mouse                                                        # Импорт модуля mouse для работы с мышью
import time                                                         # Импорт модуля time для работы с задержками

is_click = False                                                    # Флаг для отслеживания состояния кликера
click_interval = 0.01                                               # Интервал между кликами (в секундах)

def go_click():
    global is_click                                                 # Используем глобальную переменную
    if is_click:
        is_click = False                                            # Если кликер был включен, отключаем его
        print(f'Кликер выключен')
    else:
        is_click = True                                             # Если кликер был выключен, включаем его
        print(f'Кликер включен')

def set_interval():
    global click_interval                                           # Используем глобальную переменную
    interval_str = input("Введите интервал между кликами (в секундах): ")  # Запрос пользователю ввести интервал
    try:
        click_interval = float(interval_str)                        # Преобразуем введенное значение в число
        print(f'Интервал между кликами установлен: {click_interval} сек')
    except ValueError:
        print('Некорректное значение интервала!')

def stop_clicker():                                                 # Задаем функцию останова программы
    global is_click
    is_click = False
    print(f'Кликер остановлен')

keyboard.add_hotkey('Alt + Q', go_click)                            # Назначаем горячую клавишу Alt + Q для вызова функции go_click
keyboard.add_hotkey('Alt + I', set_interval)                        # Назначаем горячую клавишу Alt + I для вызова функции set_interval
keyboard.add_hotkey("Alt + S", stop_clicker)                        # Добавление комбинации клавиш для остановки кликера

while True:
    if is_click:                                                    # Если кликер включен
        mouse.double_click(button='left')                           # Совершаем двойной клик левой кнопкой мыши
        time.sleep(click_interval)                                  # Задержка между кликами согласно установленному интервалу


