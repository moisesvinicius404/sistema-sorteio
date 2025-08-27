import tkinter as tk
import tkinter.messagebox as mb
import random as ra
from threading import Timer
from tkinter import PhotoImage, Tk

class SorteioApp:
    def __init__(self, root):
        self.root = root
        self.root.title('SISTEMA DE SORTEIO')
        self.root.geometry('510x590')
        self.icon = PhotoImage(file='dice.png')
        self.root.iconphoto(False, self.icon)
        self.root.config(bg='orange')
        
        # Lista para armazenar as informações dos usuários
        self.dados_usuarios = []
        
        # Página 1: Entrada de Dados
        self.page1()
        
    def page1(self):
        self.clear_frame()
        
        tk.Label(self.root, text='Nome:', bg='orange').grid(row=0, column=0, padx=10, pady=10)
        self.entrada_nome = tk.Entry(self.root)
        self.entrada_nome.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text='Telefone:', bg='orange').grid(row=1, column=0, padx=10, pady=10)
        self.telefone_var = tk.StringVar()
        self.entrada_telefone = tk.Entry(self.root, textvariable=self.telefone_var)
        self.entrada_telefone.grid(row=1, column=1, padx=10, pady=10)
        self.telefone_var.trace_add("write", self.formatar_telefone)

        tk.Label(self.root, text='Número:', bg='orange', fg='green', font=('Arial', 9)).grid(row=2, column=0, padx=10, pady=10)
        self.entrada_numero = tk.Entry(self.root, width=3)
        self.entrada_numero.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text='Sorteio de Números Premiados!', bg='orange', font=('Arial', 20)).place(x=60, y=200)
        
        tk.Button(self.root, text='Enviar', bg='green', fg='white', command=self.verificar).place(x=110, y=130)
        tk.Button(self.root, text='Sortear', bg='blue', fg='white', command=self.page_sorteio).place(x=200, y=130)

    def formatar_telefone(self, *args):
        telefone = self.telefone_var.get().replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
        
        if len(telefone) > 2:
            telefone = f"({telefone[:2]}) {telefone[2:]}"
        if len(telefone) > 13:
            telefone = telefone[:13]
        
        if len(telefone) > 6:
            telefone = f"{telefone[:9]}-{telefone[9:]}"
        
        self.telefone_var.set(telefone)
        self.entrada_telefone.icursor(tk.END)

    def page_sorteio(self):
        self.clear_frame()
        tk.Label(self.root, text='Sorteando número, aguarde...', bg='orange', font=('Arial', 20)).pack(pady=50)
        self.root.after(1000, self.iniciar_sorteio)

    def iniciar_sorteio(self):
        # Emula uma pausa de 10 minutos
        Timer(10, self.page_resultado).start()
    
    def page_resultado(self):
        self.clear_frame()
        
        # Frame para a área de rolagem
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        # Canvas e barra de rolagem
        canvas = tk.Canvas(frame, bg='orange')
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='orange')
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        tk.Label(scrollable_frame, text='Resultado do Sorteio', bg='orange', font=('Arial', 20)).pack(pady=20)
        
        for i, (nome, telefone, numero) in enumerate(self.dados_usuarios):
            tk.Label(scrollable_frame, text=f'Participante {i+1}', bg='orange', font=('Arial', 14)).pack(pady=5)
            tk.Label(scrollable_frame, text=f'Nome: {nome}', bg='orange').pack()
            tk.Label(scrollable_frame, text=f'Telefone: {telefone}', bg='orange').pack()
            tk.Label(scrollable_frame, text=f'Número Sorteado: {numero}', bg='orange').pack()
            tk.Label(scrollable_frame, text='-------------------------', bg='orange').pack()
        
        sorteado = ra.randint(1, 100)  # Gera um número aleatório entre 1 e 100
        tk.Label(scrollable_frame, text=f'Número Vencedor: {sorteado}', bg='orange',fg='green', font=('Arial', 16)).pack(pady=20)

        tk.Button(scrollable_frame, text='Voltar', bg='green', fg='white', command=self.page1).pack(pady=20)

    def verificar(self):
        if self.entrada_nome.get() == '' or self.telefone_var.get() == '' or self.entrada_numero.get() == '':
            mb.showerror('Error', 'Preencha todos os campos!')
            return
        elif len(self.telefone_var.get().replace(' ', '').replace('(', '').replace(')', '').replace('-', '')) < 10:
            mb.showerror('Error', 'Número de Telefone inválido!')
            return
        elif len(self.entrada_numero.get()) > 3:
            mb.showerror('Error', 'Você só pode ter de 1 a 3 números dentro do campo (número) que no caso 1 até 100!')
            return
        else:
            mb.showinfo('Info', 'Informações enviadas com sucesso!')
            # Armazenar as informações para uso futuro
            self.dados_usuarios.append([
                self.entrada_nome.get(),
                self.telefone_var.get(),
                self.entrada_numero.get()
            ])
            
            # Limpar os campos após armazenamento
            self.entrada_nome.delete(0, tk.END)
            self.telefone_var.set('')
            self.entrada_numero.delete(0, tk.END)
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = SorteioApp(root)
    root.mainloop()
    
    

