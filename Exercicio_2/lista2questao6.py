def converte_em_kmh(x):
	return x / 3.6

def main():
	velocidade = float(input("Entre com a velocidade: "))
	print("Velocidade em km/h = ", converte_em_kmh(velocidade),"km/h")

main()