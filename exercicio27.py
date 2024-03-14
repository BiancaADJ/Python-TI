j = 1 # definindo variáveis
maior = -9999.9
for i in range(3): # laço de repetição
    print("Digite o ",j,"º número: ")
    num = float(input()) # guardando valor na variável
    if num > maior: # se valor atual for maior que variável "maior"
        maior = num
    j = j + 1
print("O maior número é: ",maior) # exibindo resultado