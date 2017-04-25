def tales(x,y,z):
	h = (x*y)/z
	return h

def main():
	alturaH = float(input("Sua altura: "))
	sombraH = float(input("Comprimento de sua sombra: "))
	sombraP = float(input("Sombra do predio: "))

	altura_predio = tales(alturaH, sombraP, sombraH)

	print("Altura predio = ", altura_predio)

main()