tam = float(input("Qual o tamanho do arquivo para download? ")) # guardando as informações nas variáveis
vel = float(input("Qual a velocidade de internet? "))
print(f'O tempo estimado para o download do arquivo é {tam / vel:.2f} minutos.') # exibindo resultado