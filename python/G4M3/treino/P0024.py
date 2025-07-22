total = 0
lista = []
for i in range(5):
    bloco = int(input())
    lista.append(bloco)
for i in range(5):
    while lista[i] > min(lista):
        lista[i] = lista[i] - 1
        total += 1
print(total)