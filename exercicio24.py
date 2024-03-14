sexo = input("Digite um caracter para identificarmos o seu sexo: \n[F] - Feminino\t[M] - Masculino\n\n-->\t") # guardando resposta na variável
sexo = sexo.upper()
if sexo == 'F': # se for "F"
    print("Feminino")
elif sexo == 'M': # Senao, for "M"
    print("Masculino")
else: # senao, é inválido
    print("Inválido") 