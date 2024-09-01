import random as rd

cpf_list = []
for i in range(10):
    cpf = rd.randint(100000000, 999999999)

    cpf = [int(i) for i in str(cpf)]

    pesos_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    total = 0
    for a, b in zip(pesos_1, cpf):
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

    cpf.append(rest)

    # Se o primeiro passar, executar segunda validação:
    pesos_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    total = 0
    for a, b in zip(pesos_2, cpf):
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

    cpf.append(rest)

    new_cpf = ''
    for i in cpf:
        new_cpf = new_cpf + str(i)
    cpf_list.append(new_cpf)

print(cpf_list)
