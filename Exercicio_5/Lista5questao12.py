def unir_listas(l1,l2,l3,n):
	l4 =  []
	for i in range(n):
		l4.append(l1[i])
		l4.append(l2[i])
		l4.append(l3[i])
	return l4

def main():
	lista1 = [1,3,5,7,9,11,13,15,17,19]
	lista2 = [2,4,6,8,10,12,14,16,18,20]
	lista3 = [21,22,23,24,25,26,27,28,29,30]
	print(unir_listas(lista1,lista2,lista3,10))

main()
