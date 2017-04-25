def quadrados_lista(list):
	soma = 0
	for item in list:
		soma += item**2
	return soma


'''def main():
	numeros = [10,30,2,3,4,9,11,5,6,12]
	soma = 0
	for numero in numeros:
		soma += numero**2
	print(soma)'''
def main():
	numeros = [10,30,2,3,4,9,11,5,6,12]
	print(quadrados_lista(numeros))

main()
