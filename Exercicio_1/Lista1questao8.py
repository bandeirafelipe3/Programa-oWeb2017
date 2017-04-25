def moedasUm(x):
	return x * 0.01

def moedasCinco(x):
	return x * 0.05

def moedasDez(x):
	return x * 0.1

def moedasVC(x):
	return x * 0.25

def moedasCinq(x):
	return x * 0.5

def moedasReal(x):
	return x * 1

def main():
	uc = float(input("Quantidade de moedas de um centavo = "))
	cc = float(input("Quantidade de moedas de cinco centavos = "))
	dc = float(input("Quantidade de moedas de dez centavos = "))
	vcc = float(input("Quantidade de moedas de vinte cinco centavos = "))
	ccc = float(input("Quantidade de moedas de cinquenta centavos = "))
	ur = float(input("Quantidade de moedas de um real = "))

	total_economizado = moedasUm(uc) + moedasCinco(cc) + moedasDez(dc) + moedasVC(vcc) + moedasCinq(ccc) + moedasReal(ur)

	print("Total economizado = %.2f" % round(total_economizado,2))

main()
