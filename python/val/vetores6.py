"""Problema 6
Escreva um programa para ler vários nomes, até que o usuário digite “fim”. Ao final,
exiba todos os nomes informados."""
nome = input()
lista = []
while nome != "fim":
    lista.append(nome)
    nome = input()
print("Todos os nomes informados:")
for i in range(len(lista)):
    print(f"{lista[i]}", end=" ")