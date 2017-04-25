def main():
	consoante = []
	cont = 0
	i = 0
	while i < 10:
		letra = input("Entre com 10 caracteres: ")
		if letra in "BCDFGHJKLMNPQRSTVWXYZ"or letra in "bcdfghjklmnpqrstvxwyz":
			consoante.append(letra)
			cont += 1
			i += 1
		else:
			i += 1
	print("Total de consoantes = ", cont)
	print("Consoantes = ", consoante)

main()