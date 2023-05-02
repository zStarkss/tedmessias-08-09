#Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
#números repetidos no vetor VET e em que posições se encontram.

vet = []

for i in range(10):
    numero = int(input(f'digite o {i+1}º número:'))
    vet.append(numero)

repetidos = []
for i in range(len(vet)):
    for j in range(i+1, len(vet)):
        if vet[i] == vet[j] and vet[i] not in repetidos:
            repetidos.append(vet[i])

if len(repetidos) > 0:
    print("Os seguintes números aparecem mais de uma vez no vetor:")
    for numero in repetidos:
        posicoes = [i for i in range(len(vet)) if vet[i] == numero]
        print(f"O número {numero} aparece nas posições {posicoes}")
else:
    print("Não há números repetidos no vetor.")