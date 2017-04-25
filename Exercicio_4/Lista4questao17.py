def main():
	h = 0
	n = int(input("Entre com a quantidade de termos: "))
	for x in range(1,n+1):
		h = h + 1/x

	print(h)

main()