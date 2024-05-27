import numpy as np
import random

def crossprod(u,v):

    eixo_i = u[1] * v[2] - u[2] * v[1]
    eixo_j = u[2] * v[0] - u[0] * v[2]
    eixo_k = u[0] * v[1] - u[1] * v[0]
    
    uxv = [eixo_i, eixo_j, eixo_k]

    return uxv

def main():
    
    # Gerando valores aleatórios para u e v
    u1 = random.randint(1,10)
    u2 = random.randint(1,10)
    u3 = random.randint(1,10)
    v1 = random.randint(1,10)
    v2 = random.randint(1,10)
    v3 = random.randint(1,10)

    u = [u1, u2, u3]
    print(u)
    v = [v1, v2, v3]
    print(v)
    
    # u x v
    uxv = crossprod(u,v)
    print(uxv)

    # v x u
    vxu = crossprod(v,u)
    print(vxu)

    # (u x v, u)
    uxv_u = np.inner(uxv,u)
    print(uxv_u)

    # (v x u, v)
    vxu_v = np.inner(vxu,v)
    print(vxu_v)


if __name__ == "__main__":
    main()