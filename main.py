import math

def func(x):
    return math.exp(x) - 4*x*x - 3*x
def der_func(x):
    return math.exp(x) - 8*x - 3
def fi(x):
    return x- func(x)/der_func(x)


def Newton_method(a, b, accuracy=0.1):
    iter = 0  # количество итераций
    if (func(a) * func(b) < 0):
        x = a
        while((math.fabs(func(x)) > accuracy) and (iter < 10)):
            f = func(x) #значение уравнения
            der_f = der_func(x) #значение производной уравнения
            x = x - f/der_f
            iter+=1
        print(f'Number of iterations: {iter}')
        return x

def Simple_iteration_method(a, b, accuracy=0.1):
    iter = 0

    if(func(a)*func(b) < 0):
        while((iter < 10)):
            x_pre = (a+b)/2
            while(1):
                x = fi(x_pre)
                iter+=1
                if(math.fabs(x - x_pre) < accuracy):
                    print(f'Number of iterations: {iter}')
                    return x
                else: x_pre = x
    else:
        print("Условие сходимости не выполнено")
        return 0

def Secant_method(a, b, accuracy = 0.1):
    iter = 0
    x_0 = a
    x_1 = b

    if (func(a) * func(b) < 0):
        while((math.fabs(x_1 - x_0) > accuracy) and (iter < 10)):
            tmp = x_1
            x_1 = x_1 - (x_1 - x_0) * func(x_1) / (func(x_1) - func(x_0))
            x_0 = tmp
            iter += 1
        print(f'Number of iterations: {iter}')
        return x_1
    else:
        print("Условие сходимости не выполнено")


if __name__ == '__main__':
    print("Newton method:")
    print(Newton_method(-1, -0.5, 0.01))
    print(Newton_method(0, 1, 0.01))
    print(Newton_method(4, 5, 0.01))

    print("\nSimple iteration method:")
    print(Simple_iteration_method(-1, -0.5, 0.01))
    print(Simple_iteration_method(0, 1, 0.01))
    print(Simple_iteration_method(4, 5, 0.01))

    print("\nSecant method:")
    print(Secant_method(-1, -0.5, 0.01))
    print(Secant_method(0, 1, 0.01))
    print(Secant_method(4, 5, 0.01))
