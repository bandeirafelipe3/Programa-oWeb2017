def status_num(x):
	if x > 0:
		return "Positivo"
	elif x < 0:
		return "Negativo"
	else:
		return "Igual a zero"

def main():
	x = int(input("Entre com um numero: "))
	print(status_num(x))

main()