"""Problema 2
Escreva um programa, em Python, para ler 10 (dez) números inteiros e armazenar em um
vetor. Em seguida, leia um número inteiro e diga se este número está presente no vetor."""
lista = [0] * 10
for i in range(10):
    lista[i] = int(input("Insira um número inteiro: "))
numero = int(input("Insira um número repetido (ou não): "))
if lista.count(numero) >= 1:
    print("Esse número está presente na lista.")
else:
    print("Esse número não está na lista")