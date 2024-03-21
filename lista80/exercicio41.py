ano_nao = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # definindo vetores (ano não bissexto)
ano_bi  = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # (ano bissexto)

def anula(): # função anular
    print(f'\n[{(d).zfill(2)}/{(m).zfill(2)}/{(a).zfill(4)}]\n\nEssa data não é válida')
def aprova(): # fução aceitar
    print(f'\n[{(d).zfill(2)}/{(m).zfill(2)}/{(a).zfill(4)}]\n\nEssa data é válida')

dia = int(input('Por favor digite o dia: ')) # guardando valores nas variáveis
mes = int(input('Por favor digite o mês: '))
ano = int(input('Por favor digite o ano: '))

d = str(dia) # transformar INT -> STR
m = str(mes)
a = str(ano)

if (dia <= 31) and (mes <= 12) and (ano > 0): # se não ultrapassar os limites de dia / mes / ano
    if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0): # se o ano for bissexto
        if (dia > ano_bi[mes - 1]) or (mes > 12):
            anula() # chamando a  função
        else:
            aprova()
    else:
        if (dia > ano_nao[mes - 1]) or (mes > 12):
            anula()
        else:
            aprova()
else:
    anula()