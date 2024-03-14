j = 1 # declarando variáveis
maior = -9999.9
menor = 9999.9
for i in range(3): # laço de repetição
    print("Digite o ",j,"º número: ")
    num = float(input()) # guardando valor na variável
    if num > maior: # se valor atual for maior que "maior"
        maior = num
    if num < menor: # se valor atual for menor que "menor"
        menor = num
    j = j + 1
print("O maior número é ",maior," e o menor número é ",menor) # exibindo resultado