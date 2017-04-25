def eh_primo(x):
	if x % 2 != 0:
		return True
	else:
		return False

def main():
	op = 1
	while op != 0:
		n = int(input("Entre com um numero para saber se é primo: "))
		if eh_primo(n)==True or n == 2:
			print("Primo")
		else:
			print("Não é primo")

		op = int(input("Digite 0 para encerrar o programa: "))

main()