def area_quadrado(x):
	return x * x

def perimetro_quadrado(x):
	return 4*x

def main():
	lado = float(input("Entre com o lado do quadrado: "))
	print("Perímetro = ",perimetro_quadrado(lado))
	print("Área = ",area_quadrado(lado))

main()

