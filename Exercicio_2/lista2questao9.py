def antecessor(x):
	return x - 1

def sucessor(x):
	return x + 1

def main():
	num = int(input("Entre com um numero = "))

	print("Antecessor = ", antecessor(num))
	print("Sucessor = ", sucessor(num))

main()