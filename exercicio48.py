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
    res.append(re.upper())

    if (re != "SIM") and (re != "NAO"):
        print(textos[5])
        res[i] = "NULO"
        nulo = nulo + 1

#       se (re != "SIM" e re != "NAO"){
#         escreva(texto[5])
#         res[i] = "NULO"
#         nulo = nulo + 1
#       }
#       senao{
#         res[i] = re
#         se (re == "SIM") {
#           s = s + 1
#         }
#         senao {
#           n = n + 1
#         }
#       }
#     }

#     escreva("\nClassificaÃ§Ã£o:\t")
#     se (s == 5) {
#       escreva(texto[9])
#     }
#     senao se (s == 3 ou s == 4) {
#       escreva(texto[8])
#     }
#     senao se (nulo > 3) {
#       escreva(texto[7], "\n\nNota: NÃ£o colaborou com a investigaÃ§Ã£o.")
#     }
#     senao {
#       escreva(texto[7])
#     }
#   }
# }
