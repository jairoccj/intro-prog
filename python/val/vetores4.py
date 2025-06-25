"""Problema 4
Escreva um programa, em Python, para ler 6 (seis) números. Calcule e exiba o maior
valor e sua respectiva posição."""
lista = [0] * 6
for i in range(6):
    lista[i] = int(input("Insira um número inteiro: "))
maior = max(lista)
print(f"{maior} é o maior número e sua posição é {lista.index(maior)}")