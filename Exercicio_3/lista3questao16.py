def mes_ano(x):
	mes = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
	if x < 1 or x > 12:
		return "Invalido"
	else:
		return mes[x - 1]
def main():
	x = int(input("Entre com um numero: "))
	print("Mes: ", mes_ano(x))

main()