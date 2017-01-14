import parser
import numpy as np
from math import sin, cos, tan, exp
import matplotlib.pyplot as plt

# math.sin(x)
# math.exp(x)
# function = "2+x*2"
# x**2
print('Bisection Implementation  \n')

try:

    def evalfunction(func,x):
        fx = parser.expr(func).compile()
        return eval(fx)
    # Inputs
    function = input("Enter Function: \n")
    x0 = float(input("Enter value of x0: "))
    x1 = float(input("Enter value of x1: "))
    imax = int(input("Enter maximum Iterations: "))
    t = float(input("Enter Tolerance: "))

    funcValues = np.array([])
    xValues = np.array([])

    f0 = evalfunction(function, x0)
    f1 = evalfunction(function, x1)

    if f0 * f1 < 0:

        # Loop and Bisection Algo
        for i in range(0, imax):
            f0 = evalfunction(function, x0)
            f1 = evalfunction(function, x1)
            x2 = (x1 + x0) / 2
            f2 = evalfunction(function, x2)
            funcValues = np.append(funcValues, f2)
            xValues = np.append(xValues, x2)
            if abs(f2) <= t:
                print("this is desired Output on iteration:", i , f2)
                print('f(x): ',funcValues)
                print('(x): ',xValues)
                plt.title("Bisection", fontsize=24)
                plt.xlabel("x", fontsize=14)
                plt.ylabel("F(x)", fontsize=14)
                plt.plot(funcValues, xValues)
                plt.show()
                break
            if f0 * f2 < 0:
                x1 = x2
            else:
                x0 = x2
            if i == imax-1:
                print('Answer not Found in the given range')


    else:
        print('Values of Function For x0 and x1 are not Correct')

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