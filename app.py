# Pesquisa de Opinião - TudoWeb

excelente = 0
ruim = 0

# Teste com 50 entrevistados
for entrevistado in range(50):
    print(f"\nEntrevistado {entrevistado + 1}")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        pass
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida.")

# Resultado da pesquisa
print("\nResultado da pesquisa:")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)