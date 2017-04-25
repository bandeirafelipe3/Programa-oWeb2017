def unir_listas(l1,l2,n):
	l3 =  []
	for i in range(n):
		l3.append(l1[i])
		l3.append(l2[i])
	return l3

def main():
	lista1 = [1,3,5,7]
	lista2 = [0,2,4,6]
	print(unir_listas(lista1,lista2,4))

main()
