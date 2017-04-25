def converte_em_ms(x):
	return x * 3.6

def main():
	velocidade = float(input("Entre com a velocidade: "))
	print("Velocidade em m/s = ", converte_em_ms(velocidade),"m/s")

main()