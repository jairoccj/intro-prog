#funções
def quadrado(lado: float) -> float:
    return lado**2

def retangulo(altura: float, base: float) -> float:
    return altura * base

def triangulo(altura: float, base: float) -> float:
    return (altura*base)/2

def trapezio(base_menor: float, base_maior: float, altura: float) -> float:
    return ((base_menor+base_maior) * altura ) / 2

def paralelogramo(altura: float, base: float) -> float:
    return altura * base

def losango(diagonal_menor: float, diagonal_maior: float) -> float:
    return (diagonal_maior * diagonal_menor) / 2

def circulo(raio: float) -> float:
    return raio**2 * 3.14159

#programa principal
n1 = float(input("Insira a medida de um lado da travessa: "))
n2 = float(input("Insira a medida da diagonal da forma redonda: "))
if quadrado(n1) <= circulo(n2/2) and quadrado(n1)>0 and circulo(n2/2)>0:
    print("Esse pastel é muito grande!")
elif n1 < 0 or n2 <0:
    print("Você não pode fazer pastéis no vácuo!")
else:
    print(f"A área da travessa é {quadrado(n1):.2f} cm" )
    print(f"A área de uma forma redonda é {circulo(n2/2):.2f} cm")
    circulos = round(quadrado(n1)//circulo(n2/2))
    print(f"A quantidade de formas que ele deve comprar é {circulos}")
    print(f"A área ocupada por pastéis é {circulos*circulo(n2/2):.2f} cm")
    print(f"A área inútil da travessa é {quadrado(n1) - circulos*circulo(n2/2):.2f} cm")