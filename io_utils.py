from math import exp
import matplotlib.pyplot as plt



def gettask(task_id):
    """ Получить выбранную функцию """
    if task_id == '1':
        return lambda x, y: y + (1 + x) * (y ** 2), \
               lambda x: -1 / x, \
               1, \
               1.5, \
               -1
    elif task_id == '2':
        return lambda x, y: (x ** 2) - 2 * y, \
               lambda x: 0.75 * exp(-2 * x) + 0.5 * (x ** 2) - 0.5 * x + 0.25, \
               0, \
               1, \
               1
    else:
        return None


def getdata_input():
    """ Получить данные с клавиатуры """
    data = {}

    print("\nВыберите метод дифференцирования.")
    print(" 1 — Метод Эйлера")
    print(" 2 — Метод Адамса")
    while True:
        try:
            method_id = input("Метод дифференцирования: ")
            if method_id != '1' and method_id != '2':
                raise AttributeError
            break
        except AttributeError:
            print("Метода нет в списке!")
    data['method_id'] = method_id

    print("\nВыберите задачу.")
    print(" 1 — y' = y + (1 + x)y²\n     на [1; 1,5] при y(1) = -1")
    print(" 2 - y' = x² - 2y\n     на [0; 1] при y(0) = 1")
    while True:
        try:
            task_id = input("Задача: ")
            func, acc_func, a, b, y0 = gettask(task_id)
            if func is None:
                raise AttributeError
            break
        except AttributeError:
            print("Функции нет в списке!")
    data['f'] = func
    data['acc_f'] = acc_func
    data['a'] = a
    data['b'] = b
    data['y0'] = y0

    print("\nВведите шаг точек.")
    while True:
        try:
            h = float(input("Шаг точек: "))
            if h <= 0:
                raise ArithmeticError
            break
        except (ValueError, ArithmeticError):
            print("Шаг точек должен быть положительным числом.")
    data['h'] = h

    return data
def plot(x, y, acc_x, acc_y):
    """ Отрисовать графики точного и численного решений """
    # Настраиваем всплывающее окно
    plt.rcParams['toolbar'] = 'None'
    plt.gcf().canvas.set_window_title("График")
    # Настриваем оси
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker=">", ms=5, color='k',
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker="^", ms=5, color='k',
            transform=ax.get_xaxis_transform(), clip_on=False)

    # Отрисовываем график
    plt.plot(x, y, label="y(x)")
    plt.plot(acc_x, acc_y, label="acc_y(x)")

    plt.legend()
    plt.show(block=False)