num1 = float(input("Digite o 1º número: ")) # guardando valores nas variáveis
num2 = float(input("Digite o 2º número: "))
ope = int(input("Qual operação você deseja fazer? \n[1] - Soma\t[2] - Subtração\t[3] - Divisão\t[4] - Multiplicação\n\n-->\t"))

if 1 <= ope <= 4: # se 'ope' entiver entre 1 e 4
    if ope == 1: # soma
        res = num1 + num2
    elif ope == 2: # subtração
        res = num1 - num2
    elif ope == 3: # divisão
        res = num1 / num2
    else: # multiplicação
        res = num1 * num2
    
    if res % 2 == 0: # divisível por 2
        pi = "par"
    else: # senao
        pi = "ímpar"
    
    if res > 0: # maior que 0
        pn = "positivo"
    elif res == 0: # == 0
        pn = "neutro (0)"
    else: # menor que 0
        pn = "negativo"

    resto: float = res - round(res)
    if resto != 0: # se tiver resto
        id = "decimal"
    else: #senao
        id = "inteiro"

    print(f'O resultado da operação: {res:.2f} é: {pi}, {pn} e {id}') # printando a resposta
else: # senao
    print("[Valor inválido]")
