def salvar_arquivo(historico):

    with open('historico.txt', 'w', encoding='utf-8') as arquivo:
        for item in historico:
            arquivo.write(f'{item}\n')

def ler_historico(historico):

    historico = []
    
    try:
        with open('historico.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                tarefa = linha.strip()
                if tarefa:
                    historico.append(tarefa)
            print("Historico carregado com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de historico encontrado. Começando com a lista vazia.")
    
    return historico