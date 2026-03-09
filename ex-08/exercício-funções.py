def saudacao():
    print("Olá mundo! Essa é minha primeira função com python")

saudacao()

def saudacao_funcionario(nome):
    print(f"Olá, {nome}!")

saudacao_funcionario("João")
saudacao_funcionario("Maria")

def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)

quadrado = lambda x: x ** 2
print(quadrado(5))

def funcao():
    variavel_local = 10
    print(variavel_local)

variavel_global = 20

def funcao2():
    print(variavel_global)

funcao()
funcao2()
print(variavel_global)


def area_retangulo(base, altura):

    """
    calcula a área de um retângulo

    args:
        base (float): a base do retângulo
        altura (float): A altura do retângulo
    """
    return base * altura

def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(soma_variavel(1, 2, 3))
print(soma_variavel(4, 5, 6, 7))