"""Problema 3
Escreva um programa, em Python, para ler 10 (dez) números inteiros. Ao final, exiba o
dobro dos números pares e o triplo dos números ímpares."""
lista = [0] * 10
pares = []
impares = []
for i in range(10):
    lista[i] = int(input("Insira um número inteiro: "))
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print("O dobro de cada número par: ")
for i in pares:
    print(i * 2, end=" ")
print()
print("O triplo de cada número ímpar: ")
for i in impares:
    print(i * 3, end=" ")