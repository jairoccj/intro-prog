lista_x = []
lista_y = []
vertice_x = 0
vertice_y = 0
for i in range(3):
    x,y = map(int, input().split())
    lista_x.append(x)
    lista_y.append(y)
for i in range(3):
    if lista_x.count(lista_x[i]) == 1:
        vertice_x = lista_x[i]
    if lista_y.count(lista_y[i]) == 1:
        vertice_y = lista_y[i]
print(vertice_x, vertice_y)