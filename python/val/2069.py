bombas = int(input())
matriz = []
for i in range(4):
    matriz.append([0]*6)
for i in range(bombas):
    linha, coluna = map(int, input().split())
    linha -= 1
    coluna -= 1
    matriz[linha][coluna] = 10 #bomba
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i != 0 and i != 3 and j != 0 and j != 5 and matriz[i][j] != 10: # se a célular nao estiver nas extremidades
            if matriz[i-1][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i-1][j] == 10:
                matriz[i][j] += 1
            if matriz[i-1][j+1] == 10:
                matriz[i][j] += 1
            if matriz[i][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i][j+1] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j+1] == 10:
                matriz[i][j] += 1
        
        elif i == 0 and j == 0:
            if matriz[i][j+1] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j+1] == 10:
                matriz[i][j] += 1
        
        elif i == 3 and j == 0:
            if matriz[i-1][j] == 10:
                matriz[i][j] += 1
            if matriz[i-1][j+1] == 10:
                matriz[i][j] += 1
            if matriz[i][j+1] == 10:
                matriz[i][j] += 1

        elif i == 0 and j == 5:
            if matriz[i][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j] == 10:
                matriz[i][j] += 1

        elif i == 3 and j == 5:
            if matriz[i-1][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i-1][j] == 10:
                matriz[i][j] += 1
            if matriz[i][j-1] == 10:
                matriz[i][j] += 1
        
        elif i == 0 and j != 0 and j != 5:
            if matriz[i+1][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j+1] == 10:
                matriz[i][j] += 1
            if matriz[i][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i][j+1] == 10:
                matriz[i][j] += 1
        
        elif i == 3 and j != 0 and j != 5:
            if matriz[i-1][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i-1][j] == 10:
                matriz[i][j] += 1
            if matriz[i-1][j+1] == 10:
                matriz[i][j] += 1
            if matriz[i][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i][j+1] == 10:
                matriz[i][j] += 1

        elif j == 0 and i != 0 and i != 3:
            if matriz[i-1][j] == 10:
                matriz[i][j] += 1
            if matriz[i-1][j+1] == 10:
                matriz[i][j] += 1
            if matriz[i][j+1] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j+1] == 10:
                matriz[i][j] += 1
            
        elif j == 5 and i != 0 and i != 3:
            if matriz[i-1][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i-1][j] == 10:
                matriz[i][j] += 1
            if matriz[i][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j-1] == 10:
                matriz[i][j] += 1
            if matriz[i+1][j] == 10:
                matriz[i][j] += 1

checar_linha, checar_coluna = map(int, input().split())
checar_linha -= 1
checar_coluna -= 1
if matriz[checar_linha][checar_coluna] == 0:
    print("X")
elif matriz[checar_linha][checar_coluna] == 10:
    print("B")
else:
    print(matriz[checar_linha][checar_coluna])