import numpy as np

from adams import adams_method
from euler import euler_method
from io_utils import getdata_input, plot

if __name__ == "__main__":
    print("\tЛабораторная работа #6 (19)")
    print("\tЧисленное дифференцирование")

    data = getdata_input()
    if data['method_id'] == '1':
        answer = euler_method(data['f'], data['a'], data['b'], data['y0'], data['h'])
    elif data['method_id'] == '2':
        answer = adams_method(data['f'], data['a'], data['b'], data['y0'], data['h'])
    else:
        answer = None

    if answer is None:
        print("\n\nВо время вычисления произошла ошибка!")
    else:
        x = np.array([dot[0] for dot in answer])
        y = np.array([dot[1] for dot in answer])
        acc_x = np.linspace(np.min(x), np.max(x), 100)
        acc_y = [data['acc_f'](i) for i in acc_x]
        plot(x, y, acc_x, acc_y)

        print("\n\nРезультаты вычисления.")
        print("%12s%12s%12s" % ("x", "y", "acc_y"))
        for i in range(len(answer)):
            print("%12.4f%12.4f%12.4f" % (answer[i][0], answer[i][1], data['acc_f'](answer[i][0])))
