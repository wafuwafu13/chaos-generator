import matplotlib.pyplot as plt

def ask_x(xn, lam, generation, x_axis, y_axis):
    generation += 1
    if generation <= 40:
        x_axis.append(xn)
        xn_plus_one = lam * xn * (1-xn)
        y_axis.append(xn_plus_one)
        ask_x(xn_plus_one, lam, generation, x_axis, y_axis)
    else:
        pass

def input_x0():
    try:
        x0 = float(input('x0の値を入力してください(x0 > 0):  '))
        return x0
    except ValueError:
        input_x0()

def input_lambda():
    try:
        lam = float(input('lambdaの値を入力してください:  '))
        return lam
    except ValueError:
        return input_lambda()

def set_initialize_value():
    x0 = input_x0()
    x_axis = [x0]
    lam = input_lambda()
    y0 = lam * x0 * (1-x0)
    generation = 0
    x_axis = [x0]
    y_axis = [y0]
    ask_x(x0, lam, generation, x_axis, y_axis)

    plt.title('捕食者の割合の状態遷移(相空間)図')
    plt.xlabel('xn')
    plt.ylabel('xn+1')
    plt.plot(x_axis, y_axis)
    plt.show()

set_initialize_value()