soma = 0 # iniciando variável
for i in range(3): # laço de repetição
    nota = float(input(f'Digite a {i + 1}ª nota do aluno: ')) # guardando nota na variável
    soma = soma + nota # fazendo a soma das notas

soma = soma / 3 # calculando a média da nota

if soma == 10: # se me dia for == 10:
    print("Aprovado com Distinção")
elif soma >= 7: # se for maior que 7:
    print("Aprovado")
else: # senao
    print("Reprovado")
