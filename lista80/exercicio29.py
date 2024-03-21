j = 1 # declarando variáveis
x = 0
menor = 9999.9
for i in range(3): # laço de repetição
    print("Digite o valor do",j,"º produto: ")
    num = float(input()) # guardando valor na variável
    if num < menor: # se o valor atual for menor que "menor"
        menor = num
        x = j # posição do valor maior
    j = j + 1
print("Você deve comprar o ",x,"º produto que custa R$",menor) # exibiindo resultado