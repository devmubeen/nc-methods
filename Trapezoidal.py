import numpy as np
print('Trapezoidal Implementation  \n')
import matplotlib.pyplot as plt

try:
    #data set test 1
    # xArr = np.array([1.,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8])
    # yArr = np.array([1.543,1.669,1.811,1.971,2.151,2.352,2.577,2.828,3.107])

    #data set test 2
    # xArr = np.array([2.1,2.4,2.7,3.0,3.3,3.6])
    # yArr = np.array([3.2,2.7,2.9,3.5,4.1,5.2])

    # xArr = np.array([1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4])
    # yArr = np.array([6.050, 7.389, 9.025, 11.023, 13.464, 16.445, 20.086, 24.533, 29.964])

    # Input
    xValues = input("Enter Input x Values , Separated: \n")
    xArr = np.array([])

    for i in xValues.split(','):

        xArr = np.append(xArr, i)
        xArr = xArr.astype(float)

    print("x: ", xArr)
    yValues = input("Enter Input y Values ',' Separated: \n")
    yArr = np.array([])

    for i in yValues.split(','):

        yArr = np.append(yArr, i)
        yArr = yArr.astype(float)

    print("f(x): ", yArr)

    h = xArr[1] - xArr[0]
    temp_mid_add = 0
    # print(xArr.size)

    diff_div = h/2

    for i in range(1, xArr.size-1):

       temp_mid_add += yArr[i]
       if xArr.size-2 == i:
            lastIndex = yArr[i+1]
            # print(lastIndex)

    area =  diff_div*(yArr[0] + 2*(temp_mid_add) + lastIndex)
    print(area, 'sq.m')
    plt.title("Trapezoidal", fontsize=24)
    plt.xlabel("x", fontsize=14)
    plt.ylabel("F(x)", fontsize=14)
    plt.plot(yArr, xArr)
    plt.show()

except:
    print('Error Deducted')