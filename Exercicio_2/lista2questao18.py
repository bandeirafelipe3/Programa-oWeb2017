def troca(x,y):
	temp = x
	x = y
	y = temp
	return x,y

def main():
	a = int(input("Valor A = "))
	b = int(input("Valor B = "))

	print("A = ",a,"B = ",b)
	valor = troca(a,b)
	#print("A e B",troca(a,b))
	print("A = ", valor[0],"B = ",valor[1])

main()