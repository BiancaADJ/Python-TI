letra = input("Digite uma letra do alfabeto: ") # guardando informação na variável
letra = letra.upper() # funcao para colocar na caixa alta
x = letra.isalpha() # retorna True se tiver apenas letras e False se -não
tam = len(letra)
if tam == 1: # se tiver apenas 1 caracter
    if letra == ('A' or 'E' or 'I' or 'O' or 'U'): # se for uma vogal
            print("A letra é uma vogal")
    else:
        if x == True: # se tiver letras apenas e não for uma vogal
            print("A letra é uma consoante")
        else: # senao não é uma letra
                print("Isso não é uma letra")
else: # senao, não é apenas 1 letra
    print("Tem mais de um caracter")