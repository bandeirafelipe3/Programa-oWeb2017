def semaforo(x):
	if x == 'v':
		return "Siga"
	elif x == 'a':
		return "Atenção"
	elif x == 'e':
		return "Pare"

def main():
	cor = input("Digite uma cor: ")
	print(semaforo(cor))

main()