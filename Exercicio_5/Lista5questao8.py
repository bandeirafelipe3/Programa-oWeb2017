def main():
	lista = []
	soma = 0
	produto = 1
	for x in range(5):
		x = int(input("Numero %d: "%(x+1)))
		soma += x
		produto = produto * x
		lista.append(x)
	print("Soma = ",soma)
	print("Produto = ",produto)
	print("Lista = ",lista)

main()