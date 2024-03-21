hr = input("Em que horário você trabalha?\n[M] - Matutino\t[V] - Vespertino\t[N] - Noturno\n\n-->\t") # guardando resposta na variável
if hr.upper() == 'V': # se o valor for V
    print("Boa tarde!")
elif hr.upper() == 'M': # se o valor for M
    print("Bom dia!")
elif hr.upper() == 'N': # se o valor for N
    print("Boa noite!")
else: # senao 
    print("Valor inválido!")