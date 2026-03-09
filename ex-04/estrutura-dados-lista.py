# Listas

frutas = ["Maça", "banana", "Laranja", "Manga", "Acerola", "Melancia"]

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
print(frutas[4])
print(frutas[5])

frutas.append ("pera")
print(frutas)

frutas.insert(1, "uva")
print(frutas)

frutas.remove("banana")
print(frutas)

fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]