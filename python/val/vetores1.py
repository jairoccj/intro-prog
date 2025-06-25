"""Problema 1
Escreva um programa, em Python, para ler 6 (seis) números inteiros. Ao final, exiba todos
os números pares que foram informados."""
numeros = [0] * 6
for i in range(6):
    numeros[i] = int(input("Insira um número inteiro: "))
pares = []
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
for i in pares:
    print(i, end=" ")