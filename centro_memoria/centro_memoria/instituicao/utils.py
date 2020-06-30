import requests

class GeoAPI():

    ENDPOINT_UF = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

    @classmethod
    def getEstado(cls):
            response = requests.get(cls.ENDPOINT_UF)
            estados_list = (
                ('', 'Selecione'),
            )
            json_estados = response.json()
            for uf in json_estados:
                estados_list += ((uf.get('sigla'),uf.get('sigla') + ' - ' + uf.get('nome')),)
            return sorted(estados_list, key = lambda x: x[0])