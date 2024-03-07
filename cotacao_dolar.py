import requests


class Cotacao:
    API_URL = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

    @staticmethod
    def _imprimirCotacoes():
        try:
            cotacoes = requests.get(Cotacao.API_URL).json()
            print(cotacoes)  # Imprime o JSON completo
        except Exception as e:
            raise ValueError(f"Erro ao obter cotações: {e}")

    def dolar_para_real(self):
        cotacoes = requests.get(self.API_URL).json()
        return cotacoes['USDBRL']['bid']
    
    def euro_para_real(self):
        cotacoes = requests.get(self.API_URL).json()
        return cotacoes['EURBRL']['bid']
    
    def bitcoin_para_real(self):
        cotacoes = requests.get(self.API_URL).json()
        return cotacoes['BTCBRL']['bid']

# Testando o método _imprimirCotacoes() para imprimir o JSON completo
Cotacao._imprimirCotacoes()

# Criando uma instância da classe e obtendo cotações específicas
cotacao = Cotacao()
print(cotacao.dolar_para_real())
print(cotacao.euro_para_real())
print(cotacao.bitcoin_para_real())
