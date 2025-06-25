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
l = float(input("Insira o valor do lado do quadrado: "))
print(f"Área do quadrado = {quadrado(l)}\n")
b = float(input("Insira o valor da base (retângulo, triângulo e paralelogramo): "))
h = float(input("Insira o valor da altura (retângulo, triângulo, paralelogramo e trapézio): "))
print(f"Área do retângulo = {retangulo(h, b)}")
print(f"Área do paralelogramo = {paralelogramo(h, b)}")
print(f"Área do triângulo = {triangulo(h, b)}\n")
r = float(input("Insira o valor do raio: "))
print(f"Área do círculo ≈ {circulo(r)}\n")
bezinho = float(input("Insira o valor da base menor: "))
bezao = float(input("Insira o valor da base maior: "))
print(f"Área do trapézio = {trapezio(bezinho, bezao, h)}\n")
d1 = float(input("Insira o valor da maior diagonal do losango: "))
d2 = float(input("Insira o valor da menor diagonal do losango: "))
print(f"Área do losango = {losango(d1, d2)}\n")