def main():
	alunos = []
	soma = 0
	i = 0
	while i < 5:
		j = 0
		info = []
		while j < 1:
			idade = int(input("Entre com a idade do aluno %d: " %(i+1)))
			altura = float(input("Entre com a altura do aluno %d: "%(i+1)))
			j += 1
			info.append(idade)
			info.append(altura)
		soma += altura
		alunos.append(info)
		i += 1
	media = soma/i
	cont = 0
	for x in range(i):
		if alunos[x][0] > 13 and alunos[x][1] < media:
			cont += 1
	#print(alunos)
	print("Media de alturas = ",media)
	print("Total de alunos com altura inferior á media de alturas = ",cont)

main()