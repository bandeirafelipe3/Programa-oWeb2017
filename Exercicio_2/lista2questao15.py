def inverte(x):
	c = x//100
	d = (x%100)//10
	u = x % 10
	udc = (u*100)+(d*10)+(c)
	return udc

def main():
	n = int(input("Entre com um numero de 3 algarismos: "))
	inverso = inverte(n)
	print("Inverso = ", inverso)

main()