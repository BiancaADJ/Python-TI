media: float = 0
i: int = 1

for j in range(4): # laço de repetição para pogar 4 resultados
    print("Digite a nota do ",i,"º bimestre: ")
    nota = float(input())
    media = media + nota # soma todas as notas
    i = i + 1

print(f'A média das notas é: {media / 4:.2f}') # exibe resultado