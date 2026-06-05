import os
from dotenv import load_dotenv

from trello import TrelloAgent
from view import exibir_menu
from view import exibir_cards

load_dotenv()

TODO_ID = os.getenv("TODO_ID")
DOING_ID = os.getenv("DOING_ID")
DONE_ID = os.getenv("DONE_ID")

agente = TrelloAgent()


def criar_tarefa():

    titulo = input("Título da tarefa: ")

    descricao = input("Descrição: ")

    card = agente.criar_card(
        titulo,
        descricao
    )

    if card:
        print("\nTarefa criada com sucesso!")
        print(f"ID: {card['id']}")
    else:
        print("\nErro ao criar tarefa.")


def listar_tarefas():

    cards = agente.listar_cards(TODO_ID)

    exibir_cards(cards)


def mover_para_doing():

    card_id = input(
        "\nInforme o ID do card: "
    )

    sucesso = agente.mover_card(
        card_id,
        DOING_ID
    )

    if sucesso:
        print("\nCard movido para DOING.")
    else:
        print("\nFalha ao mover card.")


def mover_para_done():

    card_id = input(
        "\nInforme o ID do card: "
    )

    sucesso = agente.mover_card(
        card_id,
        DONE_ID
    )

    if sucesso:
        print("\nCard movido para DONE.")
    else:
        print("\nFalha ao mover card.")


def main():

    while True:

        opcao = exibir_menu()

        if opcao == "1":

            if agente.testar_conexao():
                print("\nConexão OK com Trello.")
            else:
                print("\nFalha na conexão.")

        elif opcao == "2":
            criar_tarefa()

        elif opcao == "3":
            listar_tarefas()

        elif opcao == "4":
            mover_para_doing()

        elif opcao == "5":
            mover_para_done()

        elif opcao == "0":

            print("\nEncerrando...")
            break

        else:

            print("\nOpção inválida.")


if __name__ == "__main__":
    main()