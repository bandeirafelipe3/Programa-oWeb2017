def main():
	op = 1
	soma = 0
	while op != 0:
		numero = int(input("Entre com um numero: "))
		soma = soma + numero
		op = int(input("Tecle 0 para parar ou qualquer valor para continuar: "))
	print("Soma = ",soma)

main()
