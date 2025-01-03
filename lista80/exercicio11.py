cel = float(input("Digite a temperatura em Graus Celsius: ")) # coloca o valor na variável
print(f'{cel}° Celsius fica {(9 * cel / 5) + 32:.2f}° Graus Farenheit') # exibe resultado

# Github Copilot:
print(f'{(cel := float(input("Digite a temperatura em Graus Celsius: ")))}° Celsius fica {(cel * 9 / 5) + 32:.2f}° Farenheit')