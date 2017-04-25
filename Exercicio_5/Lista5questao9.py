def main():
	pessoas = []
	i = 1
	while i < 6:
		j = 0
		info = []
		while j < 1:
			idade = int(input("Idade pessoa %d: "%i))
			altura = float(input("Altura pessoa %d: "%i))
			info.append(idade)		
			info.append(altura)			
			j += 1
		pessoas.append(info)
		i += 1
	print("Informações = ",pessoas[::-1])

main()

