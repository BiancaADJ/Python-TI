hr = input("Em que horário você trabalha?\n[M] - Matutino\t[V] - Vespertino\t[N] - Noturno\n\n-->\t")
if hr == 'V' or 'v':
    print("Boa tarde!")
elif hr == 'M' or 'm':
    print("Bom dia!")
elif hr == 'N' or 'n':
    print("Boa noite!")
else:
    print("Valor inválido!")