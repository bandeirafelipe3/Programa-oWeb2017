def main():
	num = int(input("Entre com um numero maior que 1: "))
	soma = 0
	for x in range(1,num+1):
		if x % 5 == 0:
			soma = soma + x
		else:
			continue
	print(soma)

main()