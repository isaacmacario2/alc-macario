import numpy as np

def MODQRGRSCH(A):

    m, n = A.shape
    
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    A = np.array(A, dtype=float)
    
    for i in range(n):
        Q[:, i] = A[:, i]
        
        for j in range(i):
            
            R[j, i] = Q[:, j].T@Q[:, i]
            Q[:, i] = Q[:, i] - R[j, i]*Q[:, j]
        
        R[i, i] = np.linalg.norm(Q[:, i])
        
        if R[i, i] != 0:  
            Q[:, i] = Q[:, i]/R[i, i]
    
    return Q, R


A1 = np.array([
    [1, 9, 0, 5, 3, 2],
    [-6, 3, 8, 2, -8, 0],
    [3, 15, 23, 2, 1, 7],
    [3, 57, 35, 1, 7, 9],
    [3, 5, 6, 15, 55, 2],
    [33, 7, 5, 3, 5, 7]
])

A2 = np.array([
    [1, 9, 0, 5, 3, 2],
    [-6, 3, 8, 2, -8, 0],
    [3, 15, 23, 2, 1, 7],
    [3, 57, 35, 1, 7, 9],
    [3, 5, 6, 15, 55, 2],
    [33, 7, 5, 3, 5, 7]
])


Q, R = MODQRGRSCH(A1)
print("Q =\n", Q)
print("R =\n", R)
print("\n")
      
q, r = np.linalg.qr(A2)

print("q =\n", q)
print("r =\n", r)

print("\n")
A = Q@R
print(A)