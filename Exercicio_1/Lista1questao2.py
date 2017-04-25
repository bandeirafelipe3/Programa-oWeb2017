p = int(input("Quantidade de camisas P: "))
m = int(input("Quantidade de camisas M: "))
g = int(input("Quantidade de camisas G: "))

totalVendas = (p*10) + (m*12) + (g*15)

print("Total da venda = %.2f" % round(totalVendas,2))