def main():
	maior = 0
	numeros = []
	for x in range(0,101):
		numero = int(input("Digite 100 numeros: "))
		numeros.append(numero)
	'''while x < 10:
		if numero[x] < numero[x+1]:
			maior = numero[x+1]
		else:
			maior = numero[x]'''
	print(max(numeros))

main()