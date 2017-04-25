def main():
	notas = []
	i = 0
	media = 0
	soma = 0
	while i < 4:
		n = float(input("Entre com as notas do aluno: "))
		notas.append(n)
		i += 1
		soma = soma + n
	media = soma/4
	print("Notas = ",notas)
	print("Media = ",media)

main()