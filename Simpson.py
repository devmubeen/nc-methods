import numpy as np
import matplotlib.pyplot as plt

print('Simpson 1/3 Implementation  \n')

try:
    #data set test 1
    # xArr = np.array([1.,1.1,1.2,1.3,1.4])
    # yArr = np.array([1.543,1.669,1.811,1.971,2.151])

    #data set test 2
    # xArr = np.array([2.1,2.4,2.7,3.0,3.3,3.6])
    # yArr = np.array([3.2,2.7,2.9,3.5,4.1,5.2])

    # xArr = np.array([0.0, 1.0, 2.0, 3.0, 4., 5., 6.])
    # yArr = np.array([1.,2.,5.,10.,17.,26.,37.])

    # inputs

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
    four_mul = 0
    two_mul = 0


    diff_div = h/3

    if xArr.size == yArr.size:

        if xArr.size % 2:

            for i in range(1, xArr.size-1):
                #temp_mid_add += yArr[i]
                if i % 2:
                    four_mul += 4*yArr[i]
                    # print(four_mul)
                else:
                    two_mul += 2*yArr[i]
                    # print(two_mul)
                if xArr.size-2 == i:
                    lastIndex = yArr[i+1]
                    # print(lastIndex)
            area = diff_div*((yArr[0] + lastIndex) + four_mul + two_mul)
            print(area, 'sq.m')
            # plt.title("Simpson", fontsize=24)
            # plt.xlabel("x", fontsize=14)
            # plt.ylabel("F(x)", fontsize=14)
            # plt.plot(yArr, xArr)
            # plt.show()

        else:
            print('Dataset should be odd')
            print(xArr.size)

    else:
        print('Values of x or f(x) is not Correct')



except:
    print('Error Deducted')