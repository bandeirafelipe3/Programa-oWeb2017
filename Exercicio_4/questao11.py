def CalculaTempo(populacaoA, taxaA, populacaoB, taxaB):
    ano = 0
    while (populacaoA <= populacaoB):
        populacaoA = populacaoA * (1 + (taxaA/100))
        populacaoB = populacaoB * (1 + (taxaB/100))
        ano += 1
    return ano

print("Tempo:", CalculaTempo(5000000, 3, 7000000, 2))