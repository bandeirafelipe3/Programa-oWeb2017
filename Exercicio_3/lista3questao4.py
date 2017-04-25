def crescente(x,y,z):
	if x > y and y > z:
		return z,y,x
	elif y > x and x > z:
		return z,x,y
	elif z > x and x > y:
		return y,x,z
	elif x > z and z > y:
		return y,z,x
	elif y > x and z > x and y > z:
		return x,z,y
	else:
		return x,y,z

def main():
	n1 = int(input("Numero: "))
	n2 = int(input("Numero: "))
	n3 = int(input("Numero: "))

	print(crescente(n1,n2,n3))

main()