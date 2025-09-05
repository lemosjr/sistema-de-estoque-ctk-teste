import customtkinter as ctk
from tkinter import messagebox
import os
import json

class View(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Sistema de estoque")
        self.geometry("1280x720")
        self.configure(bg="#3c0a0a")
        self.create_widgets()
        self.load_data()
        self.protocol("wm_delete_window", self.on_closing)

    def create_widgets(self):
        self.frame = ctk.CTkFrame(self, corner_radius=0)
        self.frame.pack(fill="both", expand=True)

        self.label_title = ctk.CTkLabel(self.frame, text="Sistema de Estoque", font=("Arial", 24), fg_color="#3c0a0a", text_color="white")
        self.label_title.pack(pady=20)

        self.entry_name = ctk.CTkEntry(self.frame, placeholder_text="Nome do Produto")
        self.entry_name.pack(pady=10)

        self.entry_quantity = ctk.CTkEntry(self.frame, placeholder_text="Quantidade")
        self.entry_quantity.pack(pady=10)

        self.entry_price = ctk.CTkEntry(self.frame, placeholder_text="Preço")
        self.entry_price.pack(pady=10)

        self.button_add = ctk.CTkButton(self.frame, text="Adicionar Produto", command=self.add_product)
        self.button_add.pack(pady=10)

        self.listbox_products = ctk.CTkListbox(self.frame)
        self.listbox_products.pack(pady=10, fill="both", expand=True)

        self.button_remove = ctk.CTkButton(self.frame, text="Remover Produto", command=self.remove_product)
        self.button_remove.pack(pady=10)
    
        self.button_update = ctk.CTkButton(self.frame, text="Atualizar Produto", command=self.update_product)
        self.button_update.pack(pady=10)
        self.button_view = ctk.CTkButton(self.frame, text="Ver Detalhes do Produto", command=self.view_product)
        self.button_view.pack(pady=10)
        self.button_refresh = ctk.CTkButton(self.frame, text="Atualizar Lista", command=self.refresh_list)

        self.button_refresh.pack(pady=10)
        self.refresh_list()

    def add_product(self):
        name = self.entry_name.get()
        quantity = self.entry_quantity.get()
        price = self.entry_price.get()
        if name and quantity.isdigit() and price.replace('.', '', 1).isdigit():
            self.controller.add_product(name, int(quantity), float(price))
            self.entry_name.delete(0, 'end')
            self.entry_quantity.delete(0, 'end')
            self.entry_price.delete(0, 'end')
            self.refresh_list()
        else:
            messagebox.showerror("Erro", "Por favor, insira dados válidos.")

