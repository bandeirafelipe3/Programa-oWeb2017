def eh_par(x):
	if x % 2 == 0:
		return True
	else:
		return False

def main():
	x = int(input("Entre com um número: "))
	print(eh_par(x))

main()