import customtkinter as ctk


def change_label(text, color):
    result_label.configure(text=text, text_color=color)


def validator():
    cpf_item = cpf_entry.get()
    cpf_item = cpf_item.replace('.', '').replace('-', '')
    try:
        cpf_item = [int(i) for i in cpf_item]
    except ValueError:
        print("\nInsira um CPF válido!")
        raise SystemExit

    if len(cpf_item) != 11:
        change_label("Este CPF não possui 11 dígitos!", "black")
    else:
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
            change_label("Esse CPF é Inválido!", 'red')
        else:
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
                change_label("Esse CPF é Válido!", 'green')
            else:
                change_label("Esse CPF é Inválido!", 'red')


app = ctk.CTk()
app.config(width=350, height=400)
app.resizable(False, False)

output_frame = ctk.CTkFrame(app, fg_color="white")
output_frame.place_configure(
    relwidth=1, relheight=0.2,
    relx=0, rely=0)

input_frame = ctk.CTkFrame(app, fg_color='black')
input_frame.place_configure(
    relwidth=1, relheight=0.8,
    relx=0, rely=0.2)

result_label = ctk.CTkLabel(
    output_frame, text='Resultado:', text_color='black', font=("Arial", 16))
result_label.pack(anchor='center', pady=10)

cpf_entry = ctk.StringVar()
cpf_input = ctk.CTkEntry(input_frame, textvariable=cpf_entry, width=200)
cpf_input.place_configure(x=50, y=100)

validator_button = ctk.CTkButton(
    input_frame, text="Executar Validação", text_color="green",
    fg_color='transparent', bg_color="transparent", border_color='green',
    border_width=2, font=("Arial", 16), command=validator)
validator_button.place_configure(x=80, y=150)

app.mainloop()
