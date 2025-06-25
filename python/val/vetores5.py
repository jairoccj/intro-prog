"""Problema 5
Escreva um programa, em Python, para ler 8 (oito) números e armazenar em um vetor
(A). Leia mais 8 (oito) números e armazene em outro vetor (B). Gere um vetor (C), onde
cada elemento é a soma dos correspondentes nos vetores A e B.
Exemplo: C[0] = A[0] + B[0]"""
listaA = [0] * 8
for i in range(8):
    listaA[i] = int(input("Insira um elemento na lista A: "))
listaB = [0] * 8
for i in range(8):
    listaB[i] = int(input("Insira um elemento na lista B: "))
listaC = [0] * 8
for i in range(8):
    listaC[i] = listaA[i] + listaB[i]
print("Lista C com a soma das posições das listas anteriores: ")
print(listaC, end=" ")