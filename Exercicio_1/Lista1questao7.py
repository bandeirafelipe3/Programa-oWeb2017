def qtdlata(x):
	return x * 0.35

def garrafaM(x):
	return x * 0.6

def garrafaG(x):
	return x * 2

def main():
	tl = float(input("Total de latas compradas = "))
	tgm = float(input("Total de garrafas de 600ml compradas = "))
	tgg = float(input("Total de garrafas de 2l compradas = "))

	total_litros = qtdlata(tl) + garrafaM(tgm) + garrafaG(tgg)

	print("Total de litros de refrigerante = ", total_litros)

main()