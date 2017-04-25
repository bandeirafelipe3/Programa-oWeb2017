def par_impar(x,y):
	if x % 2 == 0 and y % 2 == 0:
		return "Os dois são pares"
	elif x % 2 == 0 and y % 2 != 0:
		return "O primeiro é par e o segundo é ímpar"
	elif x % 2 != 0 and y % 2 != 0:
		return "Os dois são ímpares"
	elif x % 2 != 0 and y % 2 == 0:
		return "O primeiro é ímpar e o segundo é par"

def main():
	n1 = int(input("Entre com um numero: "))
	n2 = int(input("Entre com outro numero: "))

	print(par_impar(n1,n2))

main()