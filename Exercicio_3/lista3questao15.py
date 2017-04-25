def eh_volgal(x):
	if x in "AEIOUaeiou":
		return "verdadeiro"
	else:
		return "falso"

def main():
	x = input("Entre com a letra: ")
	print("É vogal? ", eh_volgal(x))

main()