import numpy as np

from adams import adams_method
from euler import euler_method
from io_utils import getdata_input, plot

if __name__ == "__main__":
    print("\tЛабораторная работа #6 (19)")
    print("\tЧисленное дифференцирование")

    data = getdata_input()
    answer_el = euler_method(data['f'], data['a'], data['b'], data['y0'], data['h'])
    answer_adam = adams_method(data['f'], data['a'], data['b'], data['y0'], data['h'])

    x = np.array([dot[0] for dot in answer_adam])
    y = np.array([dot[1] for dot in answer_adam])
    acc_x = np.linspace(np.min(x), np.max(x), 100)
    acc_y = [data['acc_f'](i) for i in acc_x]
    plot(x, y, acc_x, acc_y)

    print("\n\nРезультаты вычисления.")
    print("%12s%12s%12s%12s" % ("x", "y_el", "e_adam", "acc_y"))
    for i in range(len(answer_adam)):
        print("%12.4f%12.4f%12.4f%12.4f" % (
            answer_adam[i][0], answer_el[i][1], answer_adam[i][1], data['acc_f'](answer_adam[i][0])))
