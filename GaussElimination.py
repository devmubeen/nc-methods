import numpy as np

A = np.array([[4.,-2.,1.],[-3., -1., 4.],[1., -1., 3.]])
b = np.array([[15.],[8.],[13.]])

print(A)
print(b)


# b = np.array([])
# A = np.array([[]])
# temp = np.array([[]])
#
#
#
# no_of_rows = int(input('Enter No. of Rows'))
#
# for i in range(no_of_rows):
#     print('Row: ', i)
#     AValues = input("Enter Input x Values , Separated: \n")
#     for j in AValues.split(','):
#         temp = np.append(temp, j)
#         temp = temp.astype(float)
#     #for k in range(0,len(temp)):
#     # A = np.concatenate((A, temp), axis=0)
#     # temp = np.array([])
#     print(A, temp)
#     temp = np.array([])
    #Aval = np.row_stack((A, Aarr))
    # print(Aval)

# A = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
#
# print(np.concatenate((A, b), axis=0))

n =  len(A)
if b.size != n:
    raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
for pivot_row in range(n-1):
    for row in range(pivot_row+1, n):
        multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
        #the only one in this column since the rest are zero
        A[row][pivot_row] = multiplier
        for col in range(pivot_row + 1, n):
            A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
            #Equation solution column
        b[row] = b[row] - multiplier*b[pivot_row]
        #print('b',b[row])
    print(A)
    print(b)
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    print('Vals',x)

