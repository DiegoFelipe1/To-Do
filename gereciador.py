import os
import json
from tarefa import Tarefa

class Gerenciador(Tarefa):
    def __init__(self):
        self.tarefas = []
        self.arquivo = os.path.join(os.path.dirname(__file__), "tarefas.json")

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)
    
    def listar(self):
        for i, tarefas in enumerate(self.tarefas):
            print(f"{i+1}. {tarefas.resumir()}")

    def salvar(self):
        tarefas_dict = [tarefas.to_dict() for tarefas in self.tarefas]

        with open(self.arquivo, 'w') as f:
            json.dump(tarefas_dict, f, indent = 4)

    def carregar(self):
        if os.path.exists(self.arquivo) > 0:
            with open(self.arquivo, 'r') as f:
                tarefas_dict = json.load(f)
                self.tarefas = [Tarefa.from_dict(d) for d in tarefas_dict]
        
        else:
            self.tarefas = []