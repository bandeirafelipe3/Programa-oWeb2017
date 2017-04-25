def main():
	lista = []
	par = []
	impar = []
	i = 0
	while i < 20:
		n = int(input("Entre com 20 numeros: "))
		lista.append(n)
		if n % 2 == 0:
			par.append(n)
			i += 1
		else:
			impar.append(n)
			i += 1
	print("Numeros = ", lista)
	print("Pares = ", par)
	print("Impares = ", impar)
main()
