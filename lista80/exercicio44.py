cem = 0 # iniciando variáveis
cin = 0
dez = 0
cinco = 0
um = 0

saque = int(input("Digite o valor que deseja sacar (Mín R$10) (Máx R$600):")) # guardando valor na variável
valor = saque

if saque > 600: # se saque > 600, faça:
    print("Valor muito alto")
elif saque < 10: # se saque < 10, faça:
    print("Valor muito baixo")
else:
    while valor > 99: # se for maior que 99, repita:
        cem = cem + 1
        valor = valor - 100
    while valor > 49: # se for maior que 49, repita:
        cin = cin + 1
        valor = valor - 50
    while valor > 9: # se for maior que 9, repita:
        dez = dez + 1
        valor = valor - 10
    while valor > 4: # se for maior que 4, repita:
        cinco = cinco + 1
        valor = valor - 5
    while valor > 0: # se for maior que 0, repita:
        um = um + 1
        valor = valor - 1
    print(f'O valor de saque: {saque}\n\nNotas que o caixa eletrônico irá te entragar:')
    print(f'{cem} notas de R$100,00\n{cin} notas de R$50,00\n{dez} notas de R$10,00\n{cinco} notas de R$5,00\n{um} moedas de R$1,00')