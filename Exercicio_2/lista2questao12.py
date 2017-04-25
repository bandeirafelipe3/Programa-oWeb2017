def media_ponderada(x,y,z,s):
	return (x*1+y*2+z*3+s*4)/10

def main():
	n1 = float(input("N1 = "))
	n2 = float(input("N2 = "))
	n3 = float(input("N3 = "))
	n4 = float(input("N4 = "))

	print("Media = ", media_ponderada(n1,n2,n3,n4))

main()