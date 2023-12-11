import tkinter as tk
from tkinter import ttk, simpledialog

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    contador_alunos = 1

    def __init__(self, nome, matricula, notas):
        super().__init__(nome)
        self.matricula = matricula
        self.notas = notas
        self.numero_chamada = Aluno.contador_alunos
        Aluno.contador_alunos += 1

    def calcular_media(self):
        if len(self.notas) > 0:
            media = sum(self.notas) / len(self.notas)
            return f"{media:.2f}"
        else:
            return "Sem notas disponíveis"

    def aprovado(self):
        media = self.calcular_media()
        if media != "Sem notas disponíveis" and float(media) >= 6.0:
            return "Aprovado"
        else:
            return "Reprovado"

class InterfaceApp:
    def __init__(self, root, disciplina):
        self.alunos_predefinidos = [
            Aluno("Wallison", "M001", [0.0, 0.0, 0.0]),
            Aluno("Felipe", "M002", [0.0, 0.0, 0.0]),
            Aluno("Victor", "M003", [0.0, 0.0, 0.0])
        ]

        self.aluno_selecionado = None

        self.root = root
        self.root.title("Sistema Escolar")
        self.root.geometry("800x600")

        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12), padding=5)
        style.configure("TEntry", font=("Arial", 12))

        ttk.Label(root, text="Alunos Predefinidos:").grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.alunos_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=5)
        self.alunos_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        for aluno in self.alunos_predefinidos:
            self.alunos_listbox.insert(tk.END, aluno.nome)

        ttk.Button(root, text="Selecionar Aluno", command=self.selecionar_aluno_predefinido).grid(row=2, column=0, pady=10)

        ttk.Label(root, text="Notas do Aluno Selecionado:").grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.notas_entry = ttk.Entry(root)
        self.notas_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        ttk.Button(root, text="Modificar Notas", command=self.modificar_notas).grid(row=5, column=0, pady=10)
        ttk.Button(root, text="Limpar Entradas", command=self.limpar_entradas).grid(row=5, column=1, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=5)

    def selecionar_aluno_predefinido(self):
        index = self.alunos_listbox.curselection()
        if index:
            aluno_selecionado = self.alunos_predefinidos[index[0]]
            self.aluno_selecionado = aluno_selecionado
            result_text = f"Aluno selecionado: {aluno_selecionado.nome}\nSituação: {aluno_selecionado.aprovado()}"
            self.result_label.config(text=result_text)
            self.notas_entry.delete(0, tk.END)
            self.notas_entry.insert(0, ", ".join(map(str, aluno_selecionado.notas)))

    def modificar_notas(self):
        index = self.alunos_listbox.curselection()
        if index:
            aluno_selecionado = self.alunos_predefinidos[index[0]]
            notas_digitadas = self.notas_entry.get().split(", ")

            if len(notas_digitadas) == len(aluno_selecionado.notas):
                aluno_selecionado.notas = [float(nota) for nota in notas_digitadas]
                media = aluno_selecionado.calcular_media()
                resultado_aprovacao = aluno_selecionado.aprovado()
                result_text = f"Notas modificadas para {aluno_selecionado.nome}: {', '.join(notas_digitadas)}\nMédia: {media}\nSituação: {resultado_aprovacao}"
                self.result_label.config(text=result_text)
            else:
                self.result_label.config(text="Número inválido de notas. Digite novamente.")

    def limpar_entradas(self):
        self.notas_entry.delete(0, tk.END)
        self.result_label.config(text="")

# Test the application
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root, None)
    root.mainloop()
