def converte_em_hh(x):
	h = x//60
	return h 

def converte_em_mm(x):
	m = x%60
	return m

def main():
	total_minutos = int(input("Quantos minutos? "))

	minutos = converte_em_mm(total_minutos)
	hora = converte_em_hh(total_minutos)

	print(hora,"h",minutos,"minutos")

main()


