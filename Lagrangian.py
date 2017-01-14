import numpy as np
import matplotlib.pyplot as plt
print('lagrangian Implementation  \n')

try:

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
        # xArr = np.array([3.2,2.7,1.0,4.8,5.6])
        # yArr = np.array([22.0,17.8,14.2,38.3,51.7])

    xEval = float(input("Enter the x on which you want Evaluate: "))
    lag_sum = 0

    if len(xArr) == len(yArr):

        # Running Algo From Here
        for i in range(0,len(xArr)):
        # resets temp_numerator such that a new numerator can be created for each i.
            temp_numerator = 1
            denumerator = 1 #resets denumerator such that a new denumerator can be created for each i.
            for j in range(0,len(xArr)):
                if i != j:
                    temp_numerator *= xEval-xArr[j]
                    #print(temp_numerator)
                    denumerator *= xArr[i]-xArr[j] #finds denumerator for L_i
            lag_sum += (temp_numerator/denumerator) * yArr[i] #Linear_combination

        print("The result is: ")
        print(lag_sum)
        # plt.title("Lagrangian", fontsize=24)
        # plt.xlabel("x", fontsize=14)
        # plt.ylabel("F(x)", fontsize=14)
        # plt.plot(yArr, xArr)
        # plt.plot(lag_sum, linestyle='--', marker='o', color='b')
        # plt.show()


    else:
        print('Length of X is not equal to Length of Y')

except:
    print('Error Deducted')