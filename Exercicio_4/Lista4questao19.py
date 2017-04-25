def triplo(x):
	return x * 3

def main():
	#n = int(input("Informe um numero: "))
	op = 1
	while op != 0:
		n = int(input("Informe um numero: "))
		print(triplo(n))		
		op = int(input("Digite 0 para parar ou qualquer valor para continuar: "))

main()
