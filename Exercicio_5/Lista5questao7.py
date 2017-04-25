def main():
	alunos = []
	medias = []
	i = 1
	while i < 11:
		#print("Este é o numero %d sendo escrito"%i)
		j = 0
		soma = 0
		notas = []
		while j < 4:
			nota = float(input("Digite quatro notas para o aluno %d: "%i))
			notas.append(nota)
			soma += nota
			j += 1
		media = soma/4
		medias.append(media)
		alunos.append(notas)
		i += 1
	cont = 0
	for media in medias:
		if media >= 7.0:
			cont += 1
	#print("\n",alunos)
	print("\nMedias = ",medias)
	print("\nTotal de alunos que conseguiu media maior ou igual a 7.0 = ",cont)

main()