textos = [ # declarando vetor de textos
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",
    "Policial: Não entendi sua resposta, por favor seja mais objetivo.",
    "[Não entendi, de todo modo foi a última pergunta.]",
    "[Suspeita]", "[Cúmplice]", "[Assassina]"
]
s = 0 # declarando variáveis
n = 0
nulo = 0

for i in range(5): # laço de repetição
    re = str(input(f'Policial: {textos[i]}\n[SIM]\t[NAO]\n\nSua resposta:\t'))
    re = re.upper() # guardando resposta na variável

    if (re != "SIM") and (re != "NAO"): # add +1 na resposta anulada
        print(textos[5])
        nulo = nulo + 1
    else:
        if re == "SIM": # add +1 na resposta "SIM"
            s = s + 1
        else: # add +1 na resposta "NAO"
            n = n + 1

print("Classificação:\t") # exibindo resultado
if s == 5:
    print(textos[9])
elif (s == 3) or (s == 4):
    print(textos[8])
elif nulo > 3:
    print(textos[7],"\n\nNota: Não colaborou com a investigação")
else:
    print(textos[7])
