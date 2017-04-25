def opcao(x):
	if x > 20:
		return "Va ao cinema!"
	else:
		return "Fique vendo TV"

def main():
	x = float(input("Digite um numero: "))
	print(opcao(x))

main()