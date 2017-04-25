def inverte_lista(list):
	return list[::-1]

def main():
	notas = []
	parar = 0
	i = 0
	j = 0
	soma = 0
	cont = 0
	inf = 0
	nota = float(input("Entre com a nota %d ou digite -1 para encerrar: "%(i + 1)))
	while nota != -1:
		j += 1
		i += 1
		notas.append(nota)
		soma += nota
		nota = float(input("Entre com a nota %d ou digite -1 para encerrar: "%(i + 1)))
		#parar = int(input("Digite -1 para encerrar: "))
	media = soma/j
	for x in range(j):
		if notas[x] > media:
			cont += 1
		if notas[x] < 7:
			inf += 1
	lista_inversa = inverte_lista(notas)
	print("\nTotal de valores digitados = ",j)
	print("\nValores digitados = ",notas)
	print("Valores invertidos: ")
	for x in range(j):
		print(lista_inversa[x])
	print("\nSoma = ", soma)
	print("\nMedia = ",media)
	print("\nValores acima da media = ",cont)
	print("\nValores inferiores a 7.0 = ",inf)
	print("\nAté breve!")

main()