def par_divide_tres(x):
	if x % 3 == 0 and x % 2 == 0:
		return "Verdadeiro"
	else:
		return "Falso"

def main():
	x = int(input("Entre com um número: "))
	print("É par e divisivel por três? ", par_divide_tres(x))

main()
