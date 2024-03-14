sx = 'a' # declarando uma variável o tipo caracter
alt = float(input("Digite a sua altura: ")) # coloca o valor na variável de altura
sx = input("Agora digite o seu sexo biológico: \n[F] - Feminino\t[M] - Masculino\n\n-->\t") # guarda o valor na variável do tipo caracter
peso = float(input("Digite seu peso atual: ")) # coloca o valor na variável de peso atual

if (sx == 'M' or 'm') or (sx == 'F' or 'f') and peso > 25.0: # validando  a entrada de dados
    if sx == 'M' or sx == 'm':
        peso_ideal: float = (72.7 * alt) - 58
    elif sx == 'F' or sx == 'f':
        peso_ideal: float = (62.1 * alt) - 44.7
    else:
        print('[Entrada de dados inválida]') # entrada inválida

    if peso < peso_ideal - 1.0: # peso atual > peso_atual
        print(f'Você está abaixo do peso, que deveria ser: {peso_ideal:.2f}')
    elif peso > peso_ideal + 1.0: # peso atual < peso_atual
        print(f'Você está acima do peso, que deveria ser: {peso_ideal:.2f}')
    else: # peso atual = peso_atual
        print(f'Você está no peso ideal: {peso_ideal:.2f}')

else: # senao a entrada é inválida
    print('[Entrada de dados inválida]')