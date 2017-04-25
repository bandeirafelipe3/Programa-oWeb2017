def main():
	popA = 5000000 
	popB = 7000000
	passou = True
	cont = 0
	while passou:
		popA = popA + (popA*0.03)
		popB = popB + (popB*0.02)
		cont = cont + 1
		if popA > popB:
			passou = False
		else:
			continue

	print("No ano", cont,"a população A passou a população B")
	print("população A = ", popA)
	print("população B = ", popB)

main()