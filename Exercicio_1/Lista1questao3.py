conta = float(input("Digite o valor da conta = "))

carlos = conta/3
andre = conta/3
felipe = int(conta/3) + (conta % 3)

print("Carlos = ", int(carlos))
print("Andre = ", int(andre))
print("Felipe = %.2f" % round(felipe,2))