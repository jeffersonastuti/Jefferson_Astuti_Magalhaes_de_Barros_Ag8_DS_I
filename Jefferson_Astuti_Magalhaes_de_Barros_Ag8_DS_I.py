# Pesquisa de Opinião - Atendimento ao Cliente
# Autor: Jefferson_Astuti_Magalhaes_de_BarrosAg8_DS_I

quantidade_excelente = 0
quantidade_bom = 0
quantidade_ruim = 0

# Para teste, troque 50 por 10
total_entrevistados = 50

for i in range(1, total_entrevistados + 1):
    print(f"\nEntrevistado {i}")

    nome = input("Digite o nome do entrevistado: ")

    idade = int(input("Digite a idade do entrevistado: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite a opção desejada: "))

    while opiniao < 1 or opiniao > 3:
        print("Opção inválida. Digite novamente.")
        opiniao = int(input("Digite a opção desejada: "))

    if opiniao == 1:
        quantidade_excelente += 1
    elif opiniao == 2:
        quantidade_bom += 1
    elif opiniao == 3:
        quantidade_ruim += 1

print("\nRESULTADO FINAL DA PESQUISA")
print(f"Quantidade de respostas EXCELENTE: {quantidade_excelente}")
print(f"Quantidade de respostas BOM: {quantidade_bom}")
print(f"Quantidade de respostas RUIM: {quantidade_ruim}")