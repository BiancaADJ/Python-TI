sx = 'a' # declarando uma variável o tipo caracter
alt = float(input("Digite a sua altura: ")) # coloca o valor na variável de altura
sx = input("Agora digite o seu sexo biológico: \n[F] - Feminino\t[M] - Masculino\n\n-->\t") # guarda o valor na variável do tipo caracter

if sx == 'M' or sx == 'm': # se sexo biológico for masculino:
    print(f'Seu peso ideal é: {(72.7 * alt) - 58:.2f}') # exibe resultado de acordo com o sexo
elif sx == 'F' or sx == 'f':
    print(f'Seu peso ideal é: {(62.1 * alt) - 44.7:.2f}')
else: # senao a entrada é inválida
    print('[Entrada de dados inválida]')