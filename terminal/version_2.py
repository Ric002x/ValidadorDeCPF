from time import sleep

import pandas as pd

file = pd.read_csv("./cpf_.csv")

n = 0
for i in file.index:
    n += 1
    cpf_item = str(file.loc[i, 'CPF'])
    cpf_item = cpf_item.replace('.', '').replace('-', '')
    name = str(file.loc[i, 'Nome'])
    last_name = str(file.loc[i, "Sobrenome"])
    try:
        cpf_item = [int(i) for i in cpf_item]
        if len(cpf_item) != 11:
            print(f"\n O CPF de {name} {last_name} não possui 11 números!")
    except ValueError:
        print("\nInsira um CPF válido!")

    # Separando os valores para testar validação:
    digit_for_validation_1 = cpf_item[-2]
    digit_for_validation_2 = cpf_item[-1]

    # Máquina executa primeiras multiplicações
    first_validation_numbers = cpf_item[:-2]
    pesos_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    total = 0
    for a, b in zip(pesos_1, first_validation_numbers):
        c = a * b
        total += c
    total = str(round(total % 11))
    rest = int(total[-1])

    if rest < 2:
        rest = 0
    elif rest >= 2:
        rest = 11 - rest
    else:
        print("erro")

    if rest != digit_for_validation_1:
        sleep(0.8)
        print(f"\nO CPF de {name} {last_name} é \033[31mInválio\033[0m")
        continue

    # Se o primeiro passar, executar segunda validação:
    second_validation_numbers = cpf_item[:-1]
    pesos_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    total = 0
    for a, b in zip(pesos_2, second_validation_numbers):
        c = a * b
        total += c

    total = str(round(total % 11))
    rest = int(total[-1])

    if rest < 2:
        rest = 0
    elif rest >= 2:
        rest = 11 - rest
    else:
        print("erro")

    if rest == digit_for_validation_2:
        sleep(0.8)
        print(f"\nCPF de {name} {last_name} \033[32mVálido!\033[0m")
    else:
        sleep(0.8)
        print(f"\nO CPF de {name} {last_name} é \033[31mInválio\033[0m")
