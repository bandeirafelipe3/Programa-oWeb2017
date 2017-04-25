def main():
	soma = 0
	for x in range(25,201):
		if x % 2 == 0:
			soma = soma + x
		else:
			continue

	print(soma)

main()