def preenche_lista(x):
	lista = []
	i = 0
	while i < x:
		lista.append(i)
		i = i + 1
	return lista 

def imprime_lista(lista):
	for posicao in range(len(lista)):
		print(lista[posicao],end=" ")

def main():
	n = int(input("Quantos itens na lista? "))
	lao = preenche_lista(n)
	imprime_lista(lao)

main()



