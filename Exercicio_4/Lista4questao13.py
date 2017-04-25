def main():
	media = 0
	cont = 0
	n = int(input("Entre com um numero ou digite 0 para terminar: "))
	while n != 0:
		
		if n < 0:
			print("Numero invalido")
			break
		else:
			if n % 3 == 0:
				media = media + n
				cont = cont + 1
			'''
			else:
				continue
			'''
		n = int(input("Entre com um numero ou digite 0 para terminar: ")) 
	if cont < 0:
		print()
	elif cont == 0:
		print("Não há média")
	else:
		total=media/cont
		print("Total = ",total)

main()
