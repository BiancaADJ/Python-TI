qnt = float(input("Digite quanto você ganha por hora: ")) 
hrs = float(input("Digite quantas horas você trabalhou este mês: ")) # coloca os valores dentro da variáveis
total = qnt * hrs # conta do salário bruto
sl: float = total - ((total * 0.11) + (total * 0.08) + (total * 0.05)) # conta do salário líquido
print(f'\nSalário Bruto: R${total:.2f}\n(-) IR [11%]: R${total * 0.11:.2f}\n(-) INSS [5%]: R${total * 0.08:.2f}\n(-) Sindicato [5%]: R${total * 0.05:.2f}') # exibindo o valor bruto e descontos
print(f'\n\nSalário Líquido: {sl:.2f}')# exibindo o salário líqido