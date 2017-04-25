def main():
	divisores = []
	x = 1
	numero = int(input("Entre com um numero: "))
	while x <= numero:
		if (numero % x) == 0:
			divisores.append(x)
			x = x + 1
		else:
			x = x + 1
	print(divisores)

main()