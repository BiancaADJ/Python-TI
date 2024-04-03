carnes = [
    [4.9, 5.8], # file duplo
    [5.9, 6.8], # alcatra
    [6.9, 7.8]  # picanha
#   <=5     >5
]

es = str(input('Digite qual das carnes irá comprar:\n[F] - Filé Duplo\n[A] - Alcatra\n[P] - Picanha\n\n-->\t'))

if es.upper() != 'F' and es.upper() != 'A' and es.upper() != 'P':
    print("[Valor inválido]")
else:
    if es.upper() == 'F':
        car:str = 'Filé duplo'
    elif es.upper() == 'A':
        car:str = 'Alcatra'
    elif es.upper() == 'P':
        car:str = 'Picanha'

    qnt = float(input(f'Digite a quantidade de {car} que irá comprar:\t'))

    if qnt > 0:
        if qnt <= 5:
            if es.upper() == 'F':
                result: float = qnt * carnes[0][0]
            elif es.upper() == 'A':
                result: float = qnt * carnes[1][0]
            else:
                result: float = qnt * carnes[2][0]
        else:
            if es.upper() == 'F':
                result: float = qnt * carnes[0][1]
            elif es.upper() == 'A':
                result: float = qnt * carnes[1][1]
            else:
                result: float = qnt * carnes[2][1]
        
        es = input('Você irá usar o cartão Tabajara?\t[S] - Sim\n[n] - Não\n\n-->\t')
        
        if es.upper() == 'S':
            result = result - ((result / 100) * 5)
        
        print(f'Total da compra de {car}:\tR${result}')
    else:
        print("[Valor inválido]")