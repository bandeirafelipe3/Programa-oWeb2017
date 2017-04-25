def velocidade_media(x,y):
	 v = x/y
	 return v

def main():
	x = float(input("Entre com a distancia em km: "))
	y = float(input("Entre com o tempo de viagem: "))

	print("A velocidde da viagem é: ", velocidade_media(x,y),"km/h")

main()
