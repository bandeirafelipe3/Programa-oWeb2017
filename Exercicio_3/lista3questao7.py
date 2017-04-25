def saudacao(nome,sexo):
	if sexo == "F" or sexo == "f":
		return "Ilma Sra. "+ nome
	else:
		return "Ilmo Sr. "+nome

def main():
	nome = input("Entre com o nome: ")
	sexo = input("Entre com o sexo: ")

	print(saudacao(nome,sexo))

main()