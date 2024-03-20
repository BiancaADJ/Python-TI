frutas: float = [
    [0, 2.5, 2.2],
    [0, 1.8, 1.5]
]

frutas[0][0] = float(input("Digite a quantidade de morangos que deseja comprar (em KG): "))
frutas[1][0] = float(input("Digite a quantidade de maças que deseja comprar (em KG): "))

if frutas[0][0] <=  5:
    preco = frutas[0][0] * frutas[0][1]
else:
    preco = frutas[0][0] * frutas[0][2]
if frutas[1][0] <= 5:
    preco = preco + (frutas[1][0] * frutas[1][1])
else:
    preco = preco + (frutas[1][0] * frutas[1][2])

if (frutas[0][0] + frutas[1][0] > 8) or (preco > 25):
    preco = preco - (preco * 0.1)

print(f'Quantidade total de frutas (Em KG): {frutas[0]}')