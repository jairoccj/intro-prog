def somar(num1: int, num2: int) -> int:
    """Soma dois números.
    num1: int - primeiro número 
    num2: int - segundo número
    """
    return num1 + num2
def dividir (num1: int, num2: int) -> int:
    """Divide dois números.
    num1: int - primeiro número 
    num2: int - segundo número
    """
    return num1 / num2
def multiplicar (num1: int, num2: int) -> int:
    """Multiplica dois números.
    num1: int - primeiro número 
    num2: int - segundo número
    """
    return num1 * num2
def subtrair (num1: int, num2: int) -> int:
    """Subtrai dois números.
    num1: int - primeiro número 
    num2: int - segundo número
    """
    return num1 - num2
def exibir (num1: int, num2: int) -> str:
    """Exibe dois números.
    num1: int - primeiro número 
    num2: int - segundo número
    """
    print(f"Primeiro número: {num1}")
    print(f"Segundo número: {num2}")
def mensagem_pt() -> str:
    """Retorna uma mensagem de boas-vindas em português."""
    return "Olá, bem-vindo ao programa de operações matemáticas!"
def mensagem_en() -> str:
    """Retorna uma mensagem de boas-vindas em inglês."""
    return "Hello, welcome to the math operations program!"
def boas_vindas() -> str:
    """Exibe o retorno da função mensagem_pt()."""
    msg = mensagem_pt()
    print(msg)

## Teste
n1, n2 = 10, 20

boas_vindas()
exibir(n1, n2)
print(f"{somar(n1, n2) = }") # 30
print(f"{subtrair(n1, n2) = }") # -10
print(f"{multiplicar(n1, n2) = }") # 200
print(f"{dividir(n1, n2) = }") # 0.5