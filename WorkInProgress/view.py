def exibir_menu():

    print("\n" + "=" * 50)
    print("AGENTE ORGANIZADOR DE TAREFAS")
    print("=" * 50)

    print("1 - Testar conexão")
    print("2 - Criar tarefa")
    print("3 - Listar tarefas To Do")
    print("4 - Mover tarefa para Doing")
    print("5 - Mover tarefa para Done")
    print("0 - Sair")

    return input("\nEscolha uma opção: ")


def exibir_cards(cards):

    if not cards:
        print("\nNenhum card encontrado.")
        return

    print("\nTAREFAS ENCONTRADAS\n")

    for card in cards:

        print("-" * 40)
        print(f"Título : {card['name']}")
        print(f"ID     : {card['id']}")

        if card["desc"]:
            print(f"Desc   : {card['desc']}")

        print("-" * 40)