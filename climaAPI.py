import requests

'''
Difficulty => Easy
'''


class ViaCepApi:
    def __init__(self):
        self.url = 'https://viacep.com.br/ws/'

    def obter_dados_cep(self, cep):
        url = f'{self.url}{cep}/json/'
        headers = self._definir_headers()

        try:
            resposta = requests.get(url, headers=headers)
            resposta.raise_for_status()
            return resposta.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Erro de conexão: {conn_err}')
        except requests.exceptions.Timeout as timeout_err:
            print(f'Tempo de solicitação expirado: {timeout_err}')
        except requests.exceptions.RequestException as req_err:
            print(f'Erro durante a solicitação: {req_err}')
        except Exception as err:
            print(f'Erro desconhecido: {err}')

        return None

    @staticmethod
    def _definir_headers():
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/122.0.0.0 Safari/537.36'
        }


class Endereco:
    def __init__(self, dados):
        self.cep = dados.get('cep')
        self.logradouro = dados.get('logradouro')
        self.complemento = dados.get('complemento')
        self.bairro = dados.get('bairro')
        self.cidade = dados.get('localidade')
        self.estado = dados.get('uf')

    def __str__(self):
        return f'CEP: {self.cep}\n' \
               f'Logradouro: {self.logradouro}\n' \
               f'Complemento: {self.complemento}\n' \
               f'Bairro: {self.bairro}\n' \
               f'Cidade: {self.cidade}\n' \
               f'Estado: {self.estado}'


if __name__ == "__main__":
    cep = '49100000'

    viacep_api = ViaCepApi()
    dados_endereco = viacep_api.obter_dados_cep(cep)

    if dados_endereco:
        endereco = Endereco(dados_endereco)
        print(endereco)
    else:
        print('Não foi possível obter os dados do CEP.')
