media: float = 0
for i in range(4):
    media = media + float(input(f'Digite o {i + 1}º número: '))

print(f'A média dos números é: {media / 4:.2f}')