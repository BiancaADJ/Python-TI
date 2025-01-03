num = float(input("Digite um número: ")) # guardando valor na variável
resto: float = num - round(num) # calculando o resto com função de arredondar
if resto != 0: # se tiver resto
    print(f'O número {num} é decimal')
else: # senao
    print(f'O número {num} é inteiro')

#Github Copilot:
num = float(input("Digite um número: "))
print(f'O número {num} é {"decimal" if num % 1 else "inteiro"}')