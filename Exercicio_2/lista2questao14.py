def dezena(x):
	d = (x % 100)//10
	return d

def main():
	n = int(input("Entre com um numero de 3 digitos: "))
	resultado = dezena(n)
	print("O algarismo da dezena é ", resultado)

main()
