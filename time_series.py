import matplotlib.pyplot as plt

def ask_x(x, lam, generation, x_axis, y_axis):
    generation += 1
    if generation <= 40:
        x_axis.append(generation)
        ans = lam * x * (1-x)
        y_axis.append(ans)
        ask_x(ans, lam, generation, x_axis, y_axis)
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
    generation = 0
    x_axis = [generation]
    y_axis = [input_x0()]
    ask_x(y_axis[0], input_lambda(), generation, x_axis, y_axis)
    plt.title('捕食者の割合の時系列図')
    plt.xlabel('世代')
    plt.ylabel('捕食者の割合')
    plt.plot(x_axis, y_axis)
    plt.show()

set_initialize_value()