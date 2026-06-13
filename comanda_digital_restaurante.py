import customtkinter as ctk
from tkinter import messagebox

app = ctk.CTk()
app.title("Comanda Digital de Restaurante")
app.geometry("560x610")
app.resizable(False, False)
app.configure(fg_color="#0b1520")


def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def fechar_conta():
    valor_texto = entry_valor.get().strip().replace(",", ".")
    pessoas_texto = entry_pessoas.get().strip()

    if not valor_texto:
        messagebox.showwarning("Atenção", "Digite o valor consumido.")
        return

    if not pessoas_texto:
        messagebox.showwarning("Atenção", "Digite a quantidade de pessoas.")
        return

    try:
        valor_consumido = float(valor_texto)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor consumido válido.")
        return

    try:
        quantidade_pessoas = int(pessoas_texto)
    except ValueError:
        messagebox.showerror("Erro", "Digite uma quantidade de pessoas válida.")
        return

    if valor_consumido < 0:
        messagebox.showerror("Erro", "O valor consumido não pode ser negativo.")
        return

    if quantidade_pessoas <= 0:
        messagebox.showerror("Erro", "A quantidade de pessoas deve ser maior que zero.")
        return

    taxa_servico = valor_consumido * 0.10
    valor_total = valor_consumido + taxa_servico
    valor_individual = valor_total / quantidade_pessoas

    label_taxa_valor.configure(text=formatar_moeda(taxa_servico))
    label_total_valor.configure(text=formatar_moeda(valor_total))
    label_individual_valor.configure(text=formatar_moeda(valor_individual))


main_frame = ctk.CTkFrame(
    app,
    width=500,
    height=560,
    corner_radius=20,
    fg_color="#102030",
    border_width=1,
    border_color="#20364d"
)
main_frame.place(relx=0.5, rely=0.5, anchor="center")
main_frame.pack_propagate(False)

titulo = ctk.CTkLabel(
    main_frame,
    text="Comanda Digital de Restaurante",
    font=("Arial", 22, "bold"),
    text_color="#ff8a00"
)
titulo.pack(pady=(18, 18))

dados_frame = ctk.CTkFrame(
    main_frame,
    width=430,
    height=120,
    corner_radius=10,
    fg_color="#131f2b",
    border_width=1,
    border_color="#64748b"
)
dados_frame.pack(padx=20, pady=(0, 18))
dados_frame.pack_propagate(False)

label_dados = ctk.CTkLabel(
    dados_frame,
    text="Dados da Conta",
    font=("Arial", 16, "bold"),
    text_color="#ff9a1f"
)
label_dados.grid(row=0, column=0, columnspan=2, sticky="w", padx=12, pady=(10, 8))

label_valor = ctk.CTkLabel(
    dados_frame,
    text="Valor Consumido (R$):",
    font=("Arial", 14),
    text_color="white"
)
label_valor.grid(row=1, column=0, sticky="w", padx=12, pady=6)

entry_valor = ctk.CTkEntry(
    dados_frame,
    width=180,
    height=34,
    corner_radius=6,
    placeholder_text="Digite o valor consumido",
    font=("Arial", 13),
    fg_color="#1a2735",
    border_color="#3b4d5e",
    text_color="white",
    placeholder_text_color="#8895a7"
)
entry_valor.grid(row=1, column=1, padx=12, pady=6)

label_pessoas = ctk.CTkLabel(
    dados_frame,
    text="Quantidade de Pessoas:",
    font=("Arial", 14),
    text_color="white"
)
label_pessoas.grid(row=2, column=0, sticky="w", padx=12, pady=6)

entry_pessoas = ctk.CTkEntry(
    dados_frame,
    width=180,
    height=34,
    corner_radius=6,
    placeholder_text="Digite a quantidade de pessoas",
    font=("Arial", 13),
    fg_color="#1a2735",
    border_color="#3b4d5e",
    text_color="white",
    placeholder_text_color="#8895a7"
)
entry_pessoas.grid(row=2, column=1, padx=12, pady=6)

botao_fechar = ctk.CTkButton(
    main_frame,
    text="FECHAR CONTA",
    command=fechar_conta,
    width=430,
    height=48,
    corner_radius=8,
    font=("Arial", 18, "bold"),
    fg_color="#ff6a00",
    hover_color="#e55d00",
    text_color="white"
)
botao_fechar.pack(padx=20, pady=(0, 18))

resumo_frame = ctk.CTkFrame(
    main_frame,
    width=430,
    height=210,
    corner_radius=10,
    fg_color="#131f2b",
    border_width=1,
    border_color="#64748b"
)
resumo_frame.pack(padx=20, pady=(0, 10))
resumo_frame.pack_propagate(False)

label_resumo = ctk.CTkLabel(
    resumo_frame,
    text="Resumo da Conta",
    font=("Arial", 16, "bold"),
    text_color="#68d33d"
)
label_resumo.grid(row=0, column=0, columnspan=2, sticky="w", padx=12, pady=(10, 12))

label_taxa = ctk.CTkLabel(
    resumo_frame,
    text="Taxa de Serviço (10%):",
    font=("Arial", 15),
    text_color="white"
)
label_taxa.grid(row=1, column=0, sticky="w", padx=12, pady=8)

label_taxa_valor = ctk.CTkLabel(
    resumo_frame,
    text="R$ 0,00",
    font=("Arial", 15, "bold"),
    text_color="#59d04f"
)
label_taxa_valor.grid(row=1, column=1, sticky="e", padx=12, pady=8)

label_total = ctk.CTkLabel(
    resumo_frame,
    text="Valor Total:",
    font=("Arial", 15),
    text_color="white"
)
label_total.grid(row=2, column=0, sticky="w", padx=12, pady=8)

label_total_valor = ctk.CTkLabel(
    resumo_frame,
    text="R$ 0,00",
    font=("Arial", 15, "bold"),
    text_color="#59d04f"
)
label_total_valor.grid(row=2, column=1, sticky="e", padx=12, pady=8)

linha = ctk.CTkFrame(
    resumo_frame,
    width=390,
    height=2,
    fg_color="#4b5b6b"
)
linha.grid(row=3, column=0, columnspan=2, padx=12, pady=10)

label_individual = ctk.CTkLabel(
    resumo_frame,
    text="Valor Individual (por pessoa):",
    font=("Arial", 15),
    text_color="white"
)
label_individual.grid(row=4, column=0, sticky="w", padx=12, pady=8)

label_individual_valor = ctk.CTkLabel(
    resumo_frame,
    text="R$ 0,00",
    font=("Arial", 22, "bold"),
    text_color="#59d04f"
)
label_individual_valor.grid(row=4, column=1, sticky="e", padx=12, pady=8)

app.mainloop()