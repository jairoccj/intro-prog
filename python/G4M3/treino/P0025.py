cortes = 0
lista = []
casos = int(input())
for i in range(casos):
    duracao = int(input())
    lista.append(duracao)
videos = casos
for i in lista:
    while i > 1:
        i -= 1
        cortes += 1
        videos += 1
print(cortes, videos)