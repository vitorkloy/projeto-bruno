import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from cartoes import Cartao
from pagamentos import Pagamento

root = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root.title("Sistema de pagamentos")
root.geometry("900x600")

def show_cartao():
    apagarTudo()
    Cartao(pagina)

def show_pagamento():
    apagarTudo()
    Pagamento(pagina)

menu = ctk.CTkFrame(root)
menu.pack(side="left", fill="y", ipadx=10)

label_menu = ctk.CTkLabel(menu, text="Menu", font=("Arial", 20))
label_menu.pack(pady=10)

btn_cartoes = ctk.CTkButton(menu, text="Cartões", command=show_cartao)
btn_cartoes.pack(pady=10)

btn_pagamento = ctk.CTkButton(menu, text="Pagamentos", command=show_pagamento)
btn_pagamento.pack(pady=10)

pagina = ctk.CTkFrame(root)
pagina.pack(side="right", fill="both", expand=True)

def apagarTudo():
    for widget in pagina.winfo_children():
        widget.destroy()

root.mainloop()