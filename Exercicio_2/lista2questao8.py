def quociente(x,y):
	return x/y

def resto(x,y):
	return x % y

def main():
	n1 = float(input("Primeiro numero = "))
	n2 = float(input("Segundo numero = "))
	n3 = int(input("Digite um numero = "))

	print("Quociente = ", quociente(n1,n2))
	print("Resto = ", resto(n1,n2))
	print("Numero = ", n3)

main()