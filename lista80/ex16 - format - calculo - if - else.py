peso = float(input("Digite (Em Kg) a quantidade de peixes que você pescou: ")) # colocar o valor dentro da variável
if peso > 50: # se o peso for > 50
    multa: float = (peso - 50) * 4 # multa = 4 reais * resto
else:
    multa: float = 0 # senao sem multa

print(f'Quantidade pescada: {peso}\nMulta: R${multa:.2f}') # exibindo o resultado