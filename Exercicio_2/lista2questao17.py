def desconto(x,y):
	valor = x - (x*y)
	return valor

def main():
	p = float(input("Entre com o preço: "))
	d = float(input("Entre com o desconto: "))

	vp = desconto(p,d)
	print("Valor a pagar: ",vp)

main()