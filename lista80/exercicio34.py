sal = float(input("Digite o salário atual do funcionário: ")) # guardando valor do salário
sin = sal * 0.03
fgts = sal * 0.11 # não descontado
inss = sal * 0.1 # calculo de cada desconto

if sal <= 900:
    ir = 0
    por = "0%"
elif sal <= 1500:
    ir = sal * 0.05
    por = "5%"
elif sal <= 2500:
    ir = sal * 0.1
    por = "10%"
else:
    ir = sal * 0.2
    por = "20%"

print(f'Salário Bruto:\t\tR${sal}\n(-) Sindicato (3%):\tR${sin:.2f}\n(-) IR ({por}):\t\tR${ir:.2f}')
print(f'(-) INSS (10%):\t\tR${inss:.2f}\n( ) FGTS (11%):\t\tR${fgts:.2f}\n\nTotal de descontos:\tR${sin + ir + inss:.2f}')
print(f'Salário Líquido:\tR${(sal - (sin + ir + inss)):.2f}') # exibindo resultados