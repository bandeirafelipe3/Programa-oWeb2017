def main():
	pares = []
	impares = []
	cont = 0
	total = 0
	for x in range(0,200):
		numero = int(input("Digite um numero: "))
		if numero % 2 == 0:
			pares.append(numero)
			cont = cont + 1
		else:
			impares.append(numero)
			total = total + 1
	print(pares)
	print("Total de pares = ", cont)
	print(impares)
	print("Total de impares = ", total)

main()

