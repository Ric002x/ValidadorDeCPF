from time import sleep

# Usuário Insere CPF:
print("insira um CPF para inicar validação\n")
print("Exemplos de valores de CPF válidos:\n"
      "1. 111.111.111-11\n2. 11111111111\n")

cpf_input = input("CPF: ")

while cpf_input != "parar":

    # Máquina executa a separção dos valores para uma lista
    cpf_item = cpf_input.replace('.', '').replace('-', '')
    try:
        cpf_item = [int(i) for i in cpf_item]
        if len(cpf_item) != 11:
            raise ValueError("\nInsira um CPF válido!")
    except ValueError:
        print("\nInsira um CPF válido!")
        raise SystemExit

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

    if rest == digit_for_validation_1:
        print("Executando validação...")
        sleep(0.8)
        print("\n1º Validação feita. Executanto segunda valiação...")
    else:
        print("Executando validação...")
        sleep(0.8)
        print("\n1º Validação feita. Este CPF é \033[31mInválido!\033[0m")
        raise SystemExit

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
        print("\n2º Validação feita. Este CPF é \033[32mVálido!\033[0m")
    else:
        sleep(0.8)
        print("\n2º Validação feita. Este CPF é \033[31mInválido!\033[0m")
        raise SystemExit

    print("\nSe deseja testar um outro CPF, basta inseri-lo logo abaixo."
          " Se não, digite 'parar'")
    cpf_input = input("CPF: ")
