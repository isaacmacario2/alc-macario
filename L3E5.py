import numpy as np
import matplotlib.pyplot as plt

def wilkinson_bidiagonal(n):

    # Definindo as diagonais
    diag_princ = np.arange(n,0,-1)
    diag_acima = [n]*(n-1)

    # Montando a matriz com as diagonais e preenchendo o resto da matriz com 0
    A = np.diag(diag_princ) + np.diag(diag_acima, k=1) + 0.
    
    return A

def main():

    # Declarando os vetores que serão plotados   
    condicionais = []
    ordem = range(1,16)
    
    # Calculando os números condicionais
    for n in range(1,16):
        A = wilkinson_bidiagonal(n)
        k = np.linalg.cond(A)
        condicionais.append(k)
    
    # Plot
    plt.plot(ordem, condicionais)
    plt.xlabel('Ordem da Matriz')
    plt.ylabel('Número Condicional')
    plt.title('Gráfico do item b')
    plt.grid(True)
    plt.show()
    
    # Item C
    A = wilkinson_bidiagonal(20)

    # Calculando os auto valores de A
    autovalores_A = np.linalg.eigvals(A)
    
    # Perturbando o elemento A(20,1) com 10^-10
    A_perturbado = A.copy()
    A_perturbado[19, 0] += 1e-10
    print(A_perturbado)

    # Calculando os auto valores de A_perturbado
    autovalores_A_perturbado = np.linalg.eigvals(A_perturbado)

    # Calculando a diferença entre os auto valores obtidos
    dif = autovalores_A - autovalores_A_perturbado

    print(autovalores_A)
    print(autovalores_A_perturbado)
    print(dif)

if __name__ == "__main__":
    main()