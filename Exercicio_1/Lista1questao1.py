def calculapao(x):
	return x * 0.12

def calculabroa(y):
	return y * 1.5

def main():
	pao = float(input("Quantos paes: "))
	broa = float(input("Quantas broas: "))

	totalpao = calculapao(pao)
	totalbroa = calculabroa(broa)
	guardar = (totalbroa + totalpao)*0.1

	print("Total de paes comprados %.2f" % round(totalpao,2))
	print("Total de broas compradas %.2f" % round(totalbroa,2))
	print("Total guardado na poupanca %.2f " % round(guardar,2))


main()


