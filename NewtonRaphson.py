import parser
import numpy as np
from math import sin, cos, tan, exp
import matplotlib.pyplot as plt

# math.sin(x)
# math.exp(x)
# function = "2+x*2"
# x**2
print('Newton Raphson Implementation  \n')

try:

    def evalfunction(func,x):
        fx = parser.expr(func).compile()
        return eval(fx)
    # Inputs
    function = input("Enter Function: \n")
    function_prime = input("Enter Function Derivative: \n")
    x0 = float(input("Enter value of x0: "))
    imax = int(input("Enter maximum Iterations: "))
    t = float(input("Enter Tolerance: "))

    funcValues = np.array([])
    xValues = np.array([])
    # function = '3*x + sin(x) - exp(x)'
    # function_prime = '3 + cos(x) - exp(x)'

    # x**3+5x-3

    for i in range(0, imax):

        f0 = evalfunction(function, x0)
        f0prime = evalfunction(function_prime, x0)

        x1 = x0 - (f0/f0prime)

        f1 = evalfunction(function,x1)
        funcValues = np.append(funcValues, f1)
        xValues = np.append(xValues, x1)


        if abs(f1) <= t:
            print("this is desired Output on iteration:", i , f1)
            print('f(x): ',funcValues)
            print('x: ',xValues)
            plt.title("Newton Raphson", fontsize=24)
            plt.xlabel("x", fontsize=14)
            plt.ylabel("F(x)", fontsize=14)
            plt.plot(funcValues, xValues)
            plt.show()
            break

        x0 = x1

        if i == imax-1:
            print('Answer not Found in the given range')




except TypeError:

    print('Function have some Error: ', TypeError)


except SyntaxError:
    # !
    print('Function have some Invalid Values')

except NameError:

    # A X
    print('Value is Not Defined')

except ValueError:
    print('iterations can never be in float values')