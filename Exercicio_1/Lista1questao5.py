ht = int(input("Informe as horas trabalhadas = "))
he = int(input("Informe as horas extras = "))

sb = (ht*10) + (he*15)

sl = sb - (sb*0.1)

print("Salario bruto = ", sb)
print("Salario liquido = %.2f" % round(sl,2))
