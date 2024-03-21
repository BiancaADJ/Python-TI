import math # importando a biblioteca de Matematica

num = [] # 0 = a, 1 = b, 2 = c
for i in range(3): # solicitar os coeficientes do usuário
    valor = float(input(f'Digite o {i + 1}º valor: '))
    num.append(valor)

if num[0] == 0: # verificando se é equação do segundo grau
    print("[A equação não é do segundo grau]")
else: # calcular o delta
    delta = num[1] * num[1] - 4 * num[0] * num[2]
    if delta < 0: # verificar a natureza das raízes
        print("[A equação não possui raízes reais]")
    else: # calcular as raízes
        raiz1 = (-num[1] + math.sqrt(delta)) / (2 * num[0])
        raiz2 = (-num[1] - math.sqrt(delta)) / (2 * num[0])

        if delta == 0: # imprimir as raízes
            print('A única raiz real dessa equação é: {raiz1}')
        else:
            print('A primeira raiz real da equação é: {raiz1}\nA segunda raiz real dessa equação é: {raiz2}')