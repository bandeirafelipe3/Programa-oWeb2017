def resto_salario():
	c1 = 200 + (200*0.02)
	c2 = 120 + (120*0.02)
	resto = 1200 - c1 - c2

	return resto

def main():
	print("Sobrou = %.2f" % round(resto_salario(),2))

main()