import math

def simple_iteration_method(x, accuracy=0.1):
    iter = 0
    rezult = 0
    while((math.fabs(x-rezult) > accuracy) and (iter < 10000)):
        rezult = x
        x = (math.exp(x) - 4*x*x)/3
        iter+=1
    print(f'Number of iterations: {iter}')
    return x

def Newton_method(x, accuracy=0.1):
    iter = 0
    func = math.exp(x) - 4*x*x - 3*x
    while((math.fabs(func) > accuracy) and (iter < 10000)):
        func = math.exp(x) - 4*x*x - 3*x
        p_func = math.exp(x) - 8*x - 3
        x = x - func/p_func
        iter+=1
    print(f'Number of iterations: {iter}')
    return x

if __name__ == '__main__':
    print(simple_iteration_method(1.0, 0.0001))
    print(Newton_method(1.0, 0.0001))
    print(Newton_method(-1.0, 0.0001))
