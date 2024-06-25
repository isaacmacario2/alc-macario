import numpy as np
import scipy as sp

def LUDECOMP(A):

    n = len(A)
    L = np.eye(n)
    P = np.eye(n)

    A = np.array(A, dtype=float)

    for i in range(n - 1):
        
        k = np.argmax(abs(A[i:n, i]))
        
        pivotindex = i + k

        if pivotindex != i:
            
            #tmp = A[i, i:n]
            #A[i, i:n] = A[pivotindex, i:n]
            #A[pivotindex, i:n] = tmp
            A[[i, pivotindex], i:n] = A[[pivotindex, i], i:n]
            
            #tmp = P[i, 0:n]
            #P[i, 0:n] = P[pivotindex, 0:n]
            #P[pivotindex, 0:n] = tmp
            P[[i, pivotindex], 0:n] = P[[pivotindex, i], 0:n]
            
            #tmp = L[i, 0:i]
            #L[i, 0:i] = L[pivotindex, 0:i]
            #L[pivotindex, 0:i] = tmp
            L[[i, pivotindex], 0:i] = L[[pivotindex, i], 0:i]
                
        multipliers = A[i+1:n, i] / A[i, i]
        
        A[i+1:n, i+1:n] = A[i+1:n, i+1:n] - np.outer(multipliers, A[i, i+1:n])
        
        A[i+1:n, i] = 0

        L[i+1:n, i] = multipliers

    U = A
    return L, U, P

A = np.array([
    [-1, -1, 0, 1],
    [-1, 1, 1, 0],
    [1, 1, 1, 1],
    [2, 0, 1, 0]
])

B = np.array([
    [1, 1, -1, 3],
    [-2, 1, 1, 2],
    [1, 1, 1, 5]
])

L, U, P = LUDECOMP(A)
print("L_A =\n", L)
print("U_A =\n", U)
print("P_A =\n", P)

L, U, P = LUDECOMP(B)
print("L_B =\n", L)
print("U_B =\n", U)
print("P_B =\n", P)
print("\n")

A = np.array([
    [-1, -1, 0, 1],
    [-1, 1, 1, 0],
    [1, 1, 1, 1],
    [2, 0, 1, 0]
])

B = np.array([
    [1, 1, -1, 3],
    [-2, 1, 1, 2],
    [1, 1, 1, 5]
])

p, l, u = sp.linalg.lu(A)
print("l_A =\n", l)
print("u_A =\n", u)
print("p_A =\n", p)

p, l, u = sp.linalg.lu(B)
print("l_B =\n", l)
print("u_B =\n", u)
print("p_B =\n", p)


