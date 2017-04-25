def chipId(x):
	return x * 4.00

def chipF(x):
	return x * 7.00

def main():
	f = float(input("Entre com o total de frangos = "))

	direito = chipId(f)
	esquerdo = chipF(f)

	gasto = direito + esquerdo

	print("Gasto com chip de Identificacao = ", direito)
	print("Gasto com o chip de Alimentacao = ", esquerdo)
	print("Gasto para marcar todos os frangos = ", gasto)

main()