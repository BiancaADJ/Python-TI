num_m = [] # declarando variáveis e vetores
num_d = []
j = 1
i = 0
while i < 3: # enquanto i < 3
    print("Digite o ",j,"º valor: ")
    valor = float(input()) # guardando valores no primeiro vetor
    num_m.append(valor)
    i = i + 1
i = 0 # voltando i pra 0
while i < 3: # enquanto i < 3
    maior: float = -9999.9
    pos: int = 0
    for k in range(3):
        if num_m[k] > maior: # encontrando o maior número
            maior = num_m[k]
            pos = k
    
    num_d.append(maior) # guardando os maiores números em ordem
    num_m[pos] = -9999.9
    i = i + 1

print("Números na ordem decrescente: ") # exibindo os
for i in range(3):
    print("\n--> ",num_d[i])