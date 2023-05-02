
numeros = []

for i in range(20):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    
print(numeros)    

numeros_invertidos = numeros[::-1]

print("Os números digitados na ordem inversa são:")
for numero in numeros_invertidos:
    print(numero)
