import numpy as np
matrix = np.array([[0, 1, 1, 0],
                   [1, 0, 0, 0],
                   [0, 1, 0, 1],
                   [0, 0, 0, 1]])
matrix1 = np.array([[0,1,0,0],
             [1,0,1,0],
             [0,0,0,1],
             [0,0,0,0]])
n = 20
for i in range(1, n + 1):
    print("已经循环到了第", i,"次")
    res = np.linalg.matrix_power(matrix, i)
    res = np.where(res > 1, 1, res)
    print(res)


