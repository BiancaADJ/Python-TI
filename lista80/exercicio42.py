cen = 0 # iniciando variáveis
dez = 0
uni = 0

num = int(input("Digite um número inteiro menor que 1000 e maior que 0: ")) # guardando o número na variável
num1 = num
if num >= 1000: # número maior que 1000, faça:
    print("Esse número não é menor que 1000")
elif num <= 0: # número menor que 0, faça:
    print("Número inválido")
else:
    while num1 > 99: # se for maior que 99, repita:
        cen = cen + 1
        num1 = num1 - 100
    while num1 > 9: # se for maior que 9, repita:
        dez = dez + 1
        num1 = num1 - 10
    while num1 > 0: # se for maior que 0, repita:
        uni = uni + 1
        num1 = num1 - 1

    if (cen == 0) and (dez == 0): # exibição de resultados
        print(f'O número {num} possui {uni} unidades')
    elif cen == 0:
        print(f'O número {num} possui {dez} dezenas e {uni} unidades. ')
    else:
        print(f'O número {num} possui: {cen} centenas, {dez} dezenas e {uni} unidades. ')