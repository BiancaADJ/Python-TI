num = float(input("Digite um valor: ")) # guardando o valor na variável
if num < 0: # se for menor que 0
    res: str = 'é negativo'
elif num == 0: # senao for igual a 0
    res: str = 'não é positivo e nem negativo = (0)'
else: # senao, é positivo
    res: str = 'é positivo'

print("O número inserido",res) # exibe resultado