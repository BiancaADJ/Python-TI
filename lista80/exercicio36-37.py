j = 1
media = 0 # declarando variáveis
rep = ["D", "E"]
apro = ["A", "B", "C"] # declarando vetores

for i in range(2): # laço de repetição para as notas
    nota = float(input(f'Digite a {j}ª nota do aluno: '))
    media = media + nota # somando as notas
    j = j + 1

media = media / 2 # calculando média

if media < 4: # definindo a nota da média
    nt: str = 'E'
elif (media >= 4) and (media < 6):
    nt: str = 'D'
elif (media >= 6) and (media < 7.5):
    nt: str = 'C'
elif (media >= 7.5) and (media < 9):
    nt: str = 'B'
else:
    nt: str = 'A'

for i in range(3): # laço de repetição para ver se foi aprovado
    if nt == apro[i]:
        print(f'Aprovado [{nt}]') # exibir resultado
for i in range(2): # laço de repetição para ver se foi reprovado
    if nt == rep[i]:
        print(f'Reprovado [{nt}]') # exibir resultado