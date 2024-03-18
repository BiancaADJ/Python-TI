func = ["Bianca","Caique","Luiz","Eduardo","Lucas"] # criando o vetor dos funcionários
sal = [1500.56, 1200.74, 3120.30, 4000.50, 2000.99 ,1200.56] # vetor dos salários

for i in range(5): # laço de repetição
    print("Gostaria de mudar o salário de ",func[i],"?\n[S] - Sim\t[N] - Não\n ")
    es = str(input()) # recebe a resposta
    
    if es.upper() == 'S': # se a resposta (em caixa alta) == 'S'
        print("Salário atual de ",func[i],": R$",sal[i],"Digite a porcentagem de reajuste que gostaria de fazer: ")
        rea = float(input()) # recebe porcentagem do reajuste

        rea = (sal[i] / 100) * rea # calculo do reajuste
        sal[i] = sal[i] + rea # colocando valor novo no lugar do valor antigo no vetor de salario

    elif es.upper() == 'N': # se a resposta (em caixa alta) == 'N'
        print(" ")
    else: # senao == 'Valor inválido'
        print("\n[Valor inválido]\n")

for i in range(5): # laço de repetição para a exibição dos salários
    print(f'\nFuncionário: {func[i]}\tSalário atual: R${sal[i]:.2f}')