qnt_galoes: int = 0 # iniciando varíavel da quantidade de galoes
m = float(input("Digite a quantidade de metros a ser pintada: ")) # colocando o valor na variável de metros
folga = m * 0.1
litros: float = m / 3
latas: float = litros / 18
galoes: float = litros / 3.6 # contas para a quantidade de latas e galoes

razao1 = round(latas)
razao2 = round(galoes) # arredondando

resto1 = (latas - razao1) + folga
resto2 = (galoes - razao2) + folga #calculando resto

if resto1 > 0:
    razao1 = razao1 + 1
if resto2 > 0:
    razao2 = razao2 + 1 # se houver resto, adiciona mais uma lata

print("Você poderá comprar:\n",razao1," latas de 18 litros\t\t= $",razao1 * 80,"\t(+ 10%)\n", razao2," galoes de 3.6 litros\t= $",razao2 * 25,"\t(+ 10%)") #exibindo o primeiro resultado

while resto1 > 0:
    qnt_galoes = qnt_galoes + 1
    resto1 = resto1 - (3.6 * razao1)

if qnt_galoes <= 0:
    print("\n\nVocê pode economizar comprando:\n",razao1," latas de 18 litros\t+ $",razao1 * 80,"\t(+ 10%)\n") # exibindo o resultado que não há galões
else:
    print("\n\nVocê pode economizar comprando:\n",razao1," latas de 18 litros\t\t+ $",razao1 * 80,"\n",qnt_galoes," galões de 3.6 litros\t + $",qnt_galoes * 25,"\n(10%)\t+ $",folga,"\nCusto total:\t= $",((razao1 * 80)+(qnt_galoes * 25)+(folga)))
    #exibindo o resultado onde há latas e galões