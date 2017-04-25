def inverte_lista(list):
	return list[::-1]

def main():
	lista = []
	i = 0
	while i < 10:
		n = int(input("Entre com uma sequencia de 10 numeros: "))
		lista.append(n)
		i += 1
	#print(lista[::-1])
	print(inverte_lista(lista))

main()