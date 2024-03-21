sal = float(input("Digite o salário de um colaborador que você deseja fazer o reajuste: ")) # guardando valor do salário
if sal <= 280: # se salário for >= 280
    rea = sal * 0.2
    por = '20%'
elif (sal > 280) and (sal <= 700): # se salário for entre 280 e 700
    rea = sal * 0.15
    por = '10%'
elif (sal > 700) and (sal <= 1500): # se salário for entre 700 e 1500
    rea = sal * 0.1
    por = '10%'
elif sal > 1500: # se salário for > 1500
    rea = sal * 0.05
    por = '5%'
print(f"Salário anterior do funcionário: R${sal}\nValor do reajuste: R${rea:.2f} - ({por})\nSalário atual: R${sal + rea:.2f}")
# exibindo resultado