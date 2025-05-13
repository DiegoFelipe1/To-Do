class Tarefa:
    def __init__(self, titulo, descricao, prioridade, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = concluida
    
    def concluir(self):
        self.concluida = True
    
    def resumir(self):
        return f'Titulo: {self.titulo} Prioridade: {self.prioridade} Status: {'✔️' if self.concluida else '❌' }'
    
    def to_dict(self):
        return {
            "titulo":self.titulo,
            "descricao":self.descricao,
            "prioridade": self.prioridade,
            "concluida": self.concluida
        }
    
    def from_dict(dados):
        return Tarefa(
            dados["titulo"],
            dados["descricao"],
            dados["prioridade"],
            dados["concluida"]
        )