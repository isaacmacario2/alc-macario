import numpy as np

def alc_cholesky(A):

    n = len(A)
    
    R = np.zeros((n, n))

    A = np.array(A, dtype=float)
    
    for i in range(n):
        tmp = A[i, i] - sum(R[k, i]**2 for k in range(i))
        
        if tmp <= 0:
            raise ValueError("A matriz não é PD")  

        R[i][i] = tmp**(0.5)

        for j in range(i+1, n):
            R[i][j] = (A[i][j] - sum(R[k, i] * R[k, j] for k in range(i))) / R[i, i]
    
    return R

A = np.array([
    [1, 1, 4, -1],
    [1, 5, 0, -1],
    [4, 0, 21, -4],
    [-1, -1, -4, 10]
])

B = np.array([
    [1, 5, 6],
    [-7, 12, 5],
    [2, 1, 10]
])

R = alc_cholesky(A)
print("R =\n", R)
print("R.T @ R =\n", R.T @ R) 