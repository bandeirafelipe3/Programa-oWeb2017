'''
	sanduiche = 2q + 1p + 1h
	q = 50g
	p = 50g
	h = 100g
'''
def queijo(x):
	return x * 100

def presunto(x):
	return x * 50

def hamburguer(x):
	return x * 100

def main():
	s = int(input("Quantos sanduiches = "))

	totalQ = queijo(s)
	totalP = presunto(s)
	totalH = hamburguer(s)

	print("Total de queijo = ", totalQ,"g")
	print("Total de presunto = ", totalP,"g")
	print("Total de hamburguer = ", totalH,"g")

main()
