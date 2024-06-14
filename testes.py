def soma(x, y):
    return x + y

def multi(x, y):
    return x * y

def integration_test():
    # Valores de entrada para teste
    a = 2
    b = 3
    
    # Resultado esperado da adição
    soma_esperada = 5

    # Teste de adição
    soma_atual = soma(a, b)
    if soma_atual != soma_esperada:
        print(f"Erro na adição: Esperado {soma_esperada}, obtido {soma_atual}")
        return False
    
    # Resultado esperado da multiplicação
    multi_esperada = 6
    
    # Teste de multiplicação
    multi_atual = multi(a, b)
    if multi_atual != multi_esperada:
        print(f"Erro na multiplicação: Esperado {multi_esperada}, obtido {multi_atual}")
        return False
    
    return True

# Executar o teste de integração
if integration_test():
    print("Teste de integração bem-sucedido.")
else:
    print("Teste de integração falhou.")
