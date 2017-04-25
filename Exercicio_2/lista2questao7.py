def soma_por_sub(x,y):
	return (x+y)/(x-y)

def main():
	x = float(input("Primeiro numero = "))
	y = float(input("Segundo numero = "))

	print("Resultado = ", soma_por_sub(x,y))

main()