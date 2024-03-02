import requests
from random import randint
from googletrans import Translator

'''
Difficulty => Normal
'''


class AdviceAPI:
    def __init__(self, url='https://api.adviceslip.com/advice/'):
        self._url = url

    def get_advice_by_id(self, slip_id):
        try:
            url = f'{self._url}{slip_id}'
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as req_err:
            print(f'Erro durante a solicitação: {req_err}')
            return None


class TranslatorService:
    def __init__(self):
        self._translator = Translator()

    def translate_text(self, text, dest='pt'):
        translation = self._translator.translate(text, dest=dest)
        return translation.text


class ConselhoDoDia:
    def __init__(self):
        self._advice_api = AdviceAPI()
        self._translator_service = TranslatorService()

    @staticmethod
    def _get_random_advice_id():
        return randint(1, 100)

    def get_random_advice(self):
        slip_id = self._get_random_advice_id()
        data = self._advice_api.get_advice_by_id(slip_id)
        if data:
            advice = data.get('slip', {}).get('advice')
            if advice:
                return self._translator_service.translate_text(advice)
        return "Não foi possível obter um conselho."


if __name__ == '__main__':
    conselho_do_dia = ConselhoDoDia()
    print(conselho_do_dia.get_random_advice())

'''AdviceAPI: Classe responsável por interagir com a API de conselhos, encapsulando a lógica de fazer requisições 
HTTP e tratar erros. 

TranslatorService: Classe responsável por encapsular a funcionalidade de tradução de texto, 
utilizando a biblioteca googletrans. 

ConselhoDoDia: Classe que coordena a obtenção de um conselho aleatório do dia, 
utilizando instâncias das classes AdviceAPI e TranslatorService. Esta classe contém o método get_random_advice, 
que encapsula a lógica de obter um conselho aleatório, traduzi-lo e retorná-lo como texto.'''
