boletim = [
    [0, 0, 0, 0], # Português
    [0, 0, 0, 0], # Matemática
    [0, 0, 0, 0]  # Ed. Física 
]
somas = 0
for i in range(3):
    for j in range(4):
        if i == 0:
            boletim[i][j] = float(input(f'Digite o {i + 1}ª nota de Português: '))
        elif i == 1:
            boletim[i][j] = float(input(f'Digite o {i + 1}ª nota de Matemática: '))
        else:
            boletim[i][j] = float(input(f'Digite o {i + 1}ª nota de Ed. Física: '))
        
