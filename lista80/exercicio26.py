j = 1 # definindo viriáveis
media = 0
nota: float = 0.0
res: str = 'avaliacao'
for i in range(2): # laço de repetição
    print("Digite a ",j,"ª nota do aluno:")
    nota = float(input()) # guardando os valores na variável de nota
    media = media + nota # soma das notas
    j = j + 1

if (media / 2) == 10: # se a media = 10
    print("O aluno foi aprovado com distinção")
elif (media / 2) >= 7: # se for >= 7
    print("O aluno foi aprovado")
else: # senao
    print("O aluno foi reprovado")