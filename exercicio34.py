sal = float(input("Digite o salário atual do funcionário: ")) # guardando valor do salário
sin = sal * 0.03
fgts = sal * 0.11 # não descontado
ir = sal * 0.05
inss = sal * 0.1 # calculo de cada desconto

print(f'Salário Bruto:\t\tR${sal}\n(-) Sindicato (3%):\tR${sin:.2f}\n(-) IR (5%):\t\tR${ir:.2f}')
print(f'(-) INSS (10%):\t\tR${inss:.2f}\n( ) FGTS (11%):\t\tR${fgts:.2f}\n\nTotal de descontos:\tR${sin + ir + inss:.2f}')
print(f'Salário Líquido:\tR${(sal - (sin + ir + inss)):.2f}') # exibindo resultados