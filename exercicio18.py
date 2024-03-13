m = float(input("Digite a quantidade de metros a ser pintada: ")) # coloca o valor dentro da variável
litros: float = m / 3
latas: float = litros / 18
razao = round(latas)
resto = latas - razao # fazendo as contas das latas e o resto

if resto > 0:
    razao = razao + 1 # adicionando uma lata a mais caso tenha resto
print(f'A quantidade de latas que você precisará comprar é: {razao}\nE você terá que pagar: R${razao * 80}') # exibindo resultado