ano = int(input("Digite o ano: ")) # guardando valor na variável

if ano > 0: # se a variável "ano" > 0
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    # se o ano for divisível por 4 e 100 = não é bissexto;
    # se o ano for divísivel por 400 = é bissexto;
    # se for divisível apenas por 4 = é bissexto.
        print("Esse ano é bissexto")
    else: # senao
        print("Esse ano não é bissexto")
else: # senao
    print("Esse ano não existe")