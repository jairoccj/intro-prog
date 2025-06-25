"""Problema 1 – Aposta
Escreva um programa, em Python, para ler 06 (seis) números distintos. Cada valor deve
estar no intervalo entre 1 e 60 (inclusive)."""
"""lista = []

for i in range(6):
    numero = int(input("Insira um número: "))
    if numero <= 60 and numero >= 1:
        lista.append(numero)
    else:
        while numero < 1 or numero > 60:
            numero = int(input("Por favor, insira um número entre 1 e 60: "))
for i in range(6):
    print(lista[i])"""

"""Problema 2 – Odenação I
Escreva um programa para ler 10 números. Ordene e exiba os valores digitados."""
"""lista = [0] * 10
lista_certa = []
for i in range(len(lista)):
    numero = int(input("Insira um número: "))
    lista[i] = numero
    
for i in range(len(lista)):
    minimo = min(lista)
    lista.remove(minimo)
    lista_certa.append(minimo)

print(lista_certa)"""

"""Problema 3 – Ordenação II
Escreva um programa, em Python, para ler o nome e a idade de 10 (dez) pessoas. Exiba
os nome ordenados (crescente) pela idade."""
nomes = []
idades = []
for i in range(10):
    nome = input(f"Insira o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Insira a idade da {i+1}ª pessoa: "))
    nomes.append(nome)
    idades.append(idade)

for i in range(9):
    for j in range(9 - i):
        if idades[j] > idades[j+1]:
            idades[j], idades[j+1] = idades[j+1], idades[j]
            nomes[j], nomes[j+1] = nomes[j+1], nomes[j]

print("\nNomes ordenados (por idade):")
for i in range(10):
    print(f"{nomes[i]} ({idades[i]} anos)")