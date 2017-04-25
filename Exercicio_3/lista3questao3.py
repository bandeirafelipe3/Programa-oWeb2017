def maior(x,y):
	if x > y:
		maior = x
		return maior
	else:
		maior = y
		return maior

def main():
	n1 = int(input("Entre com um numero: "))
	n2 = int(input("Entre com um numero: "))

	maior_num = maior(n1,n2)

	print(maior_num)

main()