def maior(x,y,z):
	if x>y and x > z:
		return x
	elif y>x and y>z:
		return y
	else:
		return z

def main():
	n1 = int(input("Digite o primeiro numero: "))
	n2 = int(input("Digite o primeiro numero: "))
	n3 = int(input("Digite o primeiro numero: "))

	print("O maior é: ", maior(n1,n2,n3))

main()