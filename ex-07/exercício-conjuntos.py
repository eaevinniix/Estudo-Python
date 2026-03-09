frutas = {"maça", "banana", "laranja"}  # um jeito de criar um conjunto
numeros = set([1, 2, 3, 4]) # outra forma de criar conjunntos 

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)

intersecao = conjunto1 & conjunto2
print(intersecao)

diferenca = conjunto1 - conjunto2
print(diferenca)

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)


frutas.add("pera")
print(frutas)

frutas.remove("banana")
print(frutas)

frutas.discard("uva")
print(frutas)

frutas.clear()
print(frutas)


""""As estruturas de dados em Python nos oferecem grande flexibilidade e potência para armazenar e manipular dados em nossos programas.
 As listas são úteis para coleções ordenadas e mutáveis, as tuplas para coleções ordenadas e imutáveis, os dicionários para armazenar 
 pares de chave valor e os conjuntos para coleções não ordenadas de elementos únicos"""