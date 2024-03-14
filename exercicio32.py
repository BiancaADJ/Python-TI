func = ["Bianca","Caique","Luiz","Eduardo","Lucas"]
sal = [1500.56, 1200.74, 3120.30, 4000.50, 2000.99 ,1200.56]

for i in range(5):
    print("Gostaria de mudar o salário de ",func[i],"?\n[S] - Sim\t[N] - Não\n ")
    es = str(input())
    
    if es == 'S' or es == 's':
        print("Salário atual de ",func[i],": R$",sal[i],"Digite a porcentagem de reajuste que gostaria de fazer: ")
        rea = float(input())

        rea = (sal[i] / 100) * rea
        sal[i] = sal[i] + rea

    elif es == 'N' or es == 'n':
        print(" ")
    else:
        print("\n[Valor inválido]\n")

for i in range(5):
    print(f'\nFuncionário: {func[i]}\tSalário atual: R${sal[i]:.2f}')