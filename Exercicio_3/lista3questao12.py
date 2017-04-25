def eh_multiplo(x):
	if x % 7 == 0:
		return "O número é múltiplo de 7"
	else:
		return "O número não é múltiplo de 7"

def main():
	x = int(input("Digite um numero: "))
	print(eh_multiplo(x))

main()
