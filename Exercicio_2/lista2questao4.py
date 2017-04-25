def main():
	total_minutos = int(input("Quantos minutos? "))

	minutos = converte_em_mm(total_minutos)
	hora = converte_em_hh(total_minutos)

	print(hora,"h",minutos,"minutos")

main()
