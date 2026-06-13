import customtkinter as ctk
from tkinter import messagebox

app = ctk.CTk()
app.title("Cálculo de Imposto de Renda")
app.geometry("520x560")
app.resizable(False, False)
app.configure(fg_color="#0b1520") 

def calcular_imposto():
    nome = entry_nome.get().strip()
    salario_texto = entry_salario.get().strip().replace(",", ".")

    if not nome:
        messagebox.showwarning("Atenção", "Digite o nome do funcionário.")
        return

    if not salario_texto:
        messagebox.showwarning("Atenção", "Digite o salário bruto.")
        return

    try:
        salario = float(salario_texto)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido para o salário.")
        return

    if salario < 0:
        messagebox.showerror("Erro", "O salário não pode ser negativo.")
        return

    if salario <= 2112.00:
        desconto = 0
    elif salario <= 2826.65:
        desconto = salario * 0.075
    else:
        desconto = salario * 0.15

    salario_liquido = salario - desconto

    label_resultado.configure(
        text=f"R$ {salario_liquido:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

main_frame = ctk.CTkFrame(
    app,
    width=460,
    height=500,
    corner_radius=22,
    fg_color="#102030",
    border_width=1,
    border_color="#20364d"
)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

label_titulo = ctk.CTkLabel(
    main_frame,
    text="Cálculo de Imposto de Renda",
    font=("Arial", 22, "bold"),
    text_color="white"
)
label_titulo.pack(pady=(28, 0))

label_subtitulo = ctk.CTkLabel(
    main_frame,
    text="(Simplificado)",
    font=("Arial", 16, "bold"),
    text_color="#3b82f6"
)
label_subtitulo.pack(pady=(0, 25))

label_nome = ctk.CTkLabel(
    main_frame,
    text="Nome do Funcionário:",
    font=("Arial", 14, "bold"),
    text_color="white"
)
label_nome.pack(anchor="w", padx=28)

entry_nome = ctk.CTkEntry(
    main_frame,
    width=400,
    height=44,
    corner_radius=8,
    placeholder_text="Digite o nome do funcionário",
    font=("Arial", 14),
    fg_color="#1a2735",
    border_color="#32475c",
    text_color="white",
    placeholder_text_color="#8a97a6"
)
entry_nome.pack(padx=28, pady=(8, 18))

label_salario = ctk.CTkLabel(
    main_frame,
    text="Salário Bruto (R$):",
    font=("Arial", 14, "bold"),
    text_color="white"
)
label_salario.pack(anchor="w", padx=28)

entry_salario = ctk.CTkEntry(
    main_frame,
    width=400,
    height=44,
    corner_radius=8,
    placeholder_text="Digite o salário bruto",
    font=("Arial", 14),
    fg_color="#1a2735",
    border_color="#32475c",
    text_color="white",
    placeholder_text_color="#8a97a6"
)
entry_salario.pack(padx=28, pady=(8, 24))

botao_calcular = ctk.CTkButton(
    main_frame,
    text="CALCULAR IMPOSTO",
    command=calcular_imposto,
    width=400,
    height=46,
    corner_radius=8,
    font=("Arial", 16, "bold"),
    fg_color="#3b82f6",
    hover_color="#2563eb",
    text_color="white"
)
botao_calcular.pack(padx=28, pady=(0, 26))

resultado_frame = ctk.CTkFrame(
    main_frame,
    width=400,
    height=130,
    corner_radius=10,
    fg_color="#131f2b",
    border_width=1,
    border_color="#2c4054"
)
resultado_frame.pack(padx=28, pady=(0, 20))
resultado_frame.pack_propagate(False)

label_texto_resultado = ctk.CTkLabel(
    resultado_frame,
    text="Salário Líquido:",
    font=("Arial", 18, "bold"),
    text_color="white"
)
label_texto_resultado.pack(pady=(22, 5))

label_resultado = ctk.CTkLabel(
    resultado_frame,
    text="R$ 0,00",
    font=("Arial", 26, "bold"),
    text_color="#59d04f"
)
label_resultado.pack()

app.mainloop()