from gereciador import Gerenciador
from tarefa import Tarefa

g = Gerenciador()
g.carregar()

def menu():
    print("\nBem vindo ao TO-DO\n")
    print("\nEscolha a opção que deseja\n")
    print("\n1 - Adicionar tarefa\n")
    print("2 - Listar tarefas\n")
    print("3 - Sair\n")
    return input('Digite a opção desejada: ')

def add_tarefa():
    titulo = input('Qual é o titulo?\n')
    descricao = input("Por favor, digite uma descrição\n")
    prioridade = input("Qual a prioridade? Alta/Media/Baixa\n")

    g.adicionar(Tarefa(titulo, descricao, prioridade))
    g.salvar()
    print("Tarefa adcionada com sucesso!")

def main():
    while True:
        opcao = menu()

        if opcao == '1':
          add_tarefa()
        
        elif opcao == '2':
            g.listar()
        
        elif opcao == '3':
            break
            
        
main()