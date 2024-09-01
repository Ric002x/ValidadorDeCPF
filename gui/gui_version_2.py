import customtkinter as ctk
import pandas as pd


def file_select():
    file_path = ctk.filedialog.askopenfilename()
    file_entry.set(file_path)


def add_label(text, color):
    label = ctk.CTkLabel(scrollframe, text=text, text_color=color)
    label.pack_configure(pady=0.1)


labels = []


def validator():
    file_path = file_entry.get()

    if file_path[-4:] != '.csv':
        add_label("Arquivo Inválido!", "red")
    else:
        file = pd.read_csv(file_path)

        for i in file.index:
            cpf_item = str(file.loc[i, 'CPF'])
            cpf_item = cpf_item.replace('.', '').replace('-', '')
            name = str(file.loc[i, 'Nome'])
            last_name = str(file.loc[i, 'Sobrenome'])
            try:
                cpf_item = [int(i) for i in cpf_item]
                if len(cpf_item) != 11:
                    add_label(f"O CPF de {name} {last_name}"
                              " não possui 11 dígitos", "black")
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
                add_label(f"O CPF de {name} {last_name} é Inválido!", "red")
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
                add_label(f"O CPF de {name} {last_name} é Válido!", "green")
            else:
                add_label(f"O CPF de {name} {last_name} é Inválido!", "red")


app = ctk.CTk()

app.config(width=800, height=600)
app.resizable(False, False)

input_frame = ctk.CTkFrame(app, fg_color="#3d4988")
input_frame.place_configure(
    relx=0, rely=0,
    relwidth=1, relheight=0.2)

output_frame = ctk.CTkFrame(app, fg_color="white")
output_frame.place_configure(
    relx=0, rely=0.2,
    relheight=0.8, relwidth=1)

scrollframe = ctk.CTkScrollableFrame(output_frame, fg_color='white')
scrollframe.pack(side='left', fill='both', expand=True)

file_button = ctk.CTkButton(
    input_frame, text="Selecionar Arquivo", command=file_select)
file_button.place_configure(x=10, y=10)

start_validation = ctk.CTkButton(
    input_frame, text="Iniciar Validação", command=validator)
start_validation.place_configure(x=10, y=70)

file_entry = ctk.StringVar()
file_input = ctk.CTkEntry(input_frame, width=400, textvariable=file_entry)
file_input.place_configure(x=250, y=80)


if __name__ == "__main__":
    app.mainloop()
