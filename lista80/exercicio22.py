num1 = float(input("Digite o primeiro número: ")) # guardando primeiro número
maior = num1 # deixando o primeiro número como maior
num2 = float(input("Digite o segundo número: ")) # guardando o segundo número

if num2 > maior: # se o segundo número for maior, ele substitui
    maior = num2

print("O maior número é: ",maior) # exibe resultado