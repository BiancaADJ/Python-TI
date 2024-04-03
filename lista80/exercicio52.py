va = int(input('Digite o valor total da compra:\t'))
va = va - int(input('Digite quanto o cliente pagou:\t'))
va1 = va

notas = 0
cem = 0
cin = 0
vin = 0
dez = 0
cinco = 0
dois = 0
um = 0

if va == 0:
    print("[Não possui troco]")
else:
    while va1 >= 100:
        cem = cem + 1
        va1 = va1 - 100
    while va1 >= 50:
        cin = cin + 1
        va1 = va1 - 50
    while va1 >= 20:
        vin = vin + 1
        va1 = va1 - 20
    while va1 >= 10:
        dez = dez + 1
        va1 = va1 - 10
    while va1 >= 5:
# Considerando que alguém está pagando uma compra,
# escreva um algoritmo que mostre o número mínimo de notas
# que o caixa deve fornecer como troco. Mostre também: o valor
# da compra, o valor do troco e a quantidade de cada tipo de nota
# do troco. Suponha que o sistema monetário não utilize moedas.