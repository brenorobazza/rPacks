import requests, urllib, json


CORREIOS_URL = "https://buscacepinter.correios.com.br/app/endereco/carrega-cep-endereco.php?pagina=%2Fapp%2Fendereco%2Findex.php&cepaux=&mensagem_alerta=&endereco={address}&tipoCEP=ALL"

class CorreiosAPI:
    def __init__():
        pass
    
    @staticmethod
    def getData(address):
        formated_address = urllib.parse.quote(address, safe='')
        url = CORREIOS_URL.format(address = formated_address)
        result = requests.get(url)
        json_data = json.loads(result.text)
        return json_data

    @classmethod
    def printData(cls, address):
        cls.getData(address)
