def inversa_eliminacao(A):
    n = len(A)
    
    # Verificação de elementos nulos na diagonal principal
    for i in range(n):
        if A[i][i] == 0:
            raise ValueError("A matriz possui elementos nulos na diagonal. Use uma função alternativa para calcular a matriz inversa.")
    
    # Cria a matriz aumentada [A | I]
    AI_matrix = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]
    
    # Eliminação
    for i in range(n):
        
        # Verificação de maior valor absoluto na coluna
        max_row = i
        max_value = abs(AI_matrix[i][i])
        for k in range(i + 1, n):
            if abs(AI_matrix[k][i]) > max_value:
                max_value = abs(AI_matrix[k][i])
                max_row = k
                
        # Trocar a linha atual com a linha com o maior valor absoluto na coluna 
        AI_matrix[i], AI_matrix[max_row] = AI_matrix[max_row], AI_matrix[i]
        
        # Verificação se o pivô é zero após o pivoteamento
        if AI_matrix[i][i] == 0:
            raise ValueError("A matriz não possui inversa.")

        # Normaliza a linha do pivô
        pivot = AI_matrix[i][i]
        AI_matrix[i] = [x / pivot for x in AI_matrix[i]]

        # Subtração de uma linha por outra
        for j in range(n):
            if j != i:
                factor = AI_matrix[j][i]
                for k in range(len(AI_matrix[i])):
                    AI_matrix[j][k] -= factor * AI_matrix[i][k]

    # Extrai a matriz inversa da matriz aumentada
    inv_matrix = [row[n:] for row in AI_matrix]
    return inv_matrix

def main():
    n = int(input("Digite a ordem da matriz quadrada: "))
    print("Digite os elementos da matriz linha por linha, separados por espaço:")
    A = []
    for i in range(n):
        linha = list(map(float, input(f"Linha {i + 1}: ").split()))
        if len(linha) != n:
            raise ValueError("Cada linha deve conter exatamente {} elementos.".format(n))
        A.append(linha)
    
    try:
        inversa = inversa_eliminacao(A)
        print("A matriz inversa é:")
        for row in inversa:
            print(" ".join(map(str, row)))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
