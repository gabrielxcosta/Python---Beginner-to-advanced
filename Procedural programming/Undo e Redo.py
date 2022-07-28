"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""
def do_add(todo, todo_list):
    todo_list.append(todo)
    return todo_list

def list_todo(todo_list):
    print('Tarefas:', todo_list)

def do_undo(todo_list, redo_list):
    if todo_list == []:
        return 
    last_todo = todo_list.pop()
    redo_list.append(last_todo)

def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer!')
        return 
    last_redo = redo_list.pop()
    todo_list.append(last_redo)

def show_menu():
    opcoes = ['Adicionar tarefa?', 'Listar tarefas?', 'Desfazer a última ação?', 'Refazer a última ação?']
    for index, op in enumerate(opcoes):
        print(f'{index + 1} - {op}')
    return input('Qual a sua opção? ')

todo_list = []
redo_list = []

# Título
print(23 * '-', '\n\tTarefas\n', 23 * '-', sep = '')

continua = True
while continua:
    op = show_menu()
    if op == '1':
        tarefa = input('\nInforme a tarefa: ')
        do_add(tarefa, todo_list)
        print()
    elif op == '2':
        print()
        list_todo(todo_list)
        print()
    elif op == '3':
        if todo_list == []:
            continua = do_undo(todo_list, redo_list)
        do_undo(todo_list, redo_list)
        print()
    elif op == '4':
        do_redo(todo_list, redo_list)
        print()
    else:
        print('\nOpção inválida!\n')