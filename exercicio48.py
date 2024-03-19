textos = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",
    "[Não entendi sua resposta, por favor seja mais objetivo.]",
    "[Não entendi, de todo modo foi a última pergunta.]",
    "[Suspeita]", "[Cúmplice]", "[Assassina]"
]
res = [5]
s = 0
n = 0
nulo = 0

for i in range(5):
    re = str(input(f'Policial: {textos[i]}\n[SIM\t[NAO]\n\nSua resposta:\t'))
    re = re.upper()
    res.append(re)

    if (re != "SIM") and (re != "NAO"):
        print(textos[5])
        res[i] = "NULO"
        nulo = nulo + 1
    else:
        res[i] = re
        if re == "SIM":
            s = s + 1
        else:
            n = n + 1

print("Classificação:\t")
if s == 5:
    print(textos[9])
elif (s == 3) or (s == 4):
    print(textos[8])
elif nulo > 3:
    print(textos[7],"\n\nNota: Não colaborou com a investigação")
else:
    print(textos[7])
