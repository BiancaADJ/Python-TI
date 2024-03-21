lds: float = [] # declarando um vetor

for i in range(3): # laço de repetição para receber os valoresdos lados
    lado = float(input(f'Digite o {i + 1}° lado do triângulo: '))
    lds.append(lado)

if (lds[0] + lds[1] > lds[2]) or (lds[1] + lds[2] > lds[0]) or (lds[2] + lds[0] > lds[1]): # se ... 
    if (lds[0] == lds[1]) and (lds[1] == lds[2]): # se tiver 2 lados iguais
        print("Esse é um triângulo equilátero")
    elif (lds[0] != lds[1]) and (lds[1] != lds[2]): # se tiver os 3 lados diferentes
        print("Esse é um triângulo Escaleno")
    else: # senao
        print("Esse é um triângulo Isósceles")
else: # senao
    print("[Esses lados não formam um triângulo]")