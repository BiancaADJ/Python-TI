combus = str(input("Digite uma das opções de combustíveis que deseja comprar: \n[A] - Álcool\t[G] - Gasolina\n\n-->\t")) # guardando resposta na variável
if (combus.upper() != 'G') and (combus.upper() != 'A'):
    print("[Opção inválida]")
else:
    if combus.upper() == 'G':
        combus = "Gasolina"
    else:
        combus = "Álcool"
    qnt = float(input(f'Digite a quantidade que deseja comprar de {combus}:')) # guardando resposta na variável de quantidade de combustível
    if qnt < 0:
        print("[Valor inválido]")
    else:
        if combus == "Álcool": # descontos do Álcool
            preco: float = (qnt * 1.9)
            if qnt <= 20:
                preco = preco - (preco * 0.03)
                des = "3%"
            else:
                preco = preco - (preco * 0.05)
                des = "5%"
        else: # descontos da Gasolina
            preco: float = (qnt * 2.5)
            if qnt <= 20:
                preco = preco - (preco * 0.04)
                des = "4%"
            else:
                preco = preco - (preco * 0.06)
                des = "6%"
        
        print(f'Combustível: [{combus}]\nQuantidade comprada: [{qnt}]\n(-) Desconto de {des}\n\nValor a pagar: R${preco:.2f}')