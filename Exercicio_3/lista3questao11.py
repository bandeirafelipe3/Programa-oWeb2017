def febre(x):
	if x > 36.5:
		return "Está com febre"
	else:
		return "Sem febre"

def main():
	temp = float(input("Temperatura: "))
	print(febre(temp))

main()