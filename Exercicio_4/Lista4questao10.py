def main():
	multiplicando = int(input("Entre com o multiplicando: "))
	multiplicador = int(input("Entre com o multiplicador: "))
	produto = 0

	if multiplicador < 0 or multiplicando < 0:
		print("Números negativos não podem ser usados")
	else:
		while multiplicador > 0:
			produto = produto + multiplicando
			multiplicador = multiplicador - 1

	print(produto)

main()