def eh_multiplo_5(x):
	if x % 5 == 0:
		return "Verdadeiro"
	else:
		return "Falso"

def main():
	x = int(input("Entre com um numero: "))
	print("É multiplo de 5? ", eh_multiplo_5(x))

main()