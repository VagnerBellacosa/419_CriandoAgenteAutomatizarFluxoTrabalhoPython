import os
import requests
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("TRELLO_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")

TODO_ID = os.getenv("TODO_ID")
DOING_ID = os.getenv("DOING_ID")
DONE_ID = os.getenv("DONE_ID")


class TrelloAgent:

    BASE_URL = "https://api.trello.com/1"

    def __init__(self):
        self.key = KEY
        self.token = TOKEN

    def criar_card(self, titulo, descricao=""):

        url = f"{self.BASE_URL}/cards"

        params = {
            "idList": TODO_ID,
            "name": titulo,
            "desc": descricao,
            "key": self.key,
            "token": self.token
        }

        response = requests.post(url, params=params)

        if response.status_code == 200:
            return response.json()

        return None

    def listar_cards(self, lista_id):

        url = f"{self.BASE_URL}/lists/{lista_id}/cards"

        params = {
            "key": self.key,
            "token": self.token
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()

        return []

    def mover_card(self, card_id, destino_id):

        url = f"{self.BASE_URL}/cards/{card_id}"

        params = {
            "idList": destino_id,
            "key": self.key,
            "token": self.token
        }

        response = requests.put(url, params=params)

        return response.status_code == 200

    def obter_card(self, card_id):

        url = f"{self.BASE_URL}/cards/{card_id}"

        params = {
            "key": self.key,
            "token": self.token
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()

        return None

    def testar_conexao(self):

        url = f"{self.BASE_URL}/members/me"

        params = {
            "key": self.key,
            "token": self.token
        }

        response = requests.get(url, params=params)

        return response.status_code == 200