num = int(input("Digite o número de habitantes que irá cadastrar: ")) # guardando informação na variável

nome: str = [] # iniciando vetores para os dados dos habitantes
salario: float = []
filhos: int = []
j = 1 # contagem
maior: float = -100
media_filhos = 0
media_sal = 0
menos: float = 0

for i in range(num): # coletando todos os dados dos habitantes
    nom = str(input(f'Digite o nome do {j}º habitante: '))
    nome.append(nom) # colocando o nome dentro do vetor
    sal = float(input(f'Digite o salário de {nom.upper()}: '))
    salario.append(sal) # colocando o salário dentro do vetor
    fi = int(input(f'Digite o número de filhos que {nom.upper()} possui: '))
    filhos.append(fi) # colocando a informação do número de filhos no vetor
    j = j + 1

    media_sal = media_sal + sal # soma dos salários
    media_filhos = media_filhos + fi # soma dos filhos

    if sal > maior: # maior salário da população
        maior = sal
    if sal < 150: # salário negativo
        menos = menos + 1

print(f'Salário médio da população: R${media_sal / num:.2f}\nMédia do número de filhos: {media_filhos / num:.0f}')
print(f'Maior salário dos habitantes: R${maior:.2f}\nSalário Negativo: {(num / menos) * 100:.0f}% da população.')