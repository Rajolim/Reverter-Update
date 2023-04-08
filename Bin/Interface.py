import tkinter as tk
from tkinter import ttk
import subprocess

class InterfaceNumerica(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        estilo = ttk.Style()
        estilo.configure("TEntry", font=("Arial", 14))
        estilo.configure("TButton", font=("Arial", 8))

        self.rotulo = ttk.Label(self, text="Numero do update")
        self.rotulo.pack(pady=10)

        self.numero_entry = ttk.Entry(self, validate="key")
        self.numero_entry.configure(validatecommand=(self.register(self.validate_numero), '%P'))
        self.numero_entry.pack(pady=2)

        self.botao = ttk.Button(self, text="Reverter", command=self.clique_botao)
        self.botao.pack(pady=5)

    def validate_numero(self, valor):
        if valor.isdigit() or valor == "":
            return True
        else:
            return False

    def clique_botao(self):
        numero = self.numero_entry.get()
        print(f"O número digitado foi: {numero}")
        subprocess.run(f"wusa /uninstall /kb:{numero}", shell=True)

root = tk.Tk()
root.title("Interface Numérica")
root.geometry("300x180")
interface_numerica = InterfaceNumerica(root)
interface_numerica.pack(pady=20, padx=20)
root.mainloop()