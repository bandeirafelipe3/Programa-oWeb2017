def pode_votar(x,y):
	if y - x >= 16:
		return "Pode votar"
	else:
		return "Não pode votar"

def main():
	x = int(input("Entre com o ano de nascimento: "))
	y = int(input("Ano da eleição: "))

	print("Pode votar? ",pode_votar(x,y))

main()