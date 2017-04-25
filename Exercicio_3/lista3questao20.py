def i_mc(m,h):
	i_mc = m/(h**2)
	return i_mc

def main():
	massa = float(input("Entre com o peso: "))
	altura = float(input("Entre com a altura: "))

	imc = i_mc(massa,altura)

	if imc < 18.5:
		print("IMC = ",imc,"Abaixo do peso")
	elif imc < 25:
		print("IMC = ",imc,"Peso normal")
	elif imc < 30:
		print("IMC = ",imc,"Sobrepeso")
	elif imc < 35:
		print("IMC = ",imc,"Obeso leve")
	elif imc < 40:
		print("IMC = ",imc,"Obeso moderado")
	elif imc >= 40:
		print("IMC = ",imc,"Obeso mórbido")

main()