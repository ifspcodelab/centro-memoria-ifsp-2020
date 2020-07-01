import requests
from .models import Instituicao

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

class GeradorDinamico():

    @classmethod
    def gerarDatasVisita(cls):
        instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
        list_datas = instituicao.datas_visita.split(';')

        choice_datas = (
            ('', 'Selecione'),
        )

        for data in list_datas:
            choice_datas += ((data, data),)

        return choice_datas

    @classmethod
    def gerarAreasVisita(cls):
        instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
        list_areas = instituicao.areas_visita.split(';')
        choice_areas = ()

        for area in list_areas:
            choice_areas += ((area, area),)

        return choice_areas

    @classmethod
    def gerarPeriodoVisita(cls):
        instituicao = Instituicao.objects.all().order_by('-criado_em')[0]
        list_periodos = instituicao.periodos_visita.split(';')
        choice_periodos = ()

        for periodo in list_periodos:
            choice_periodos += ((periodo, periodo),)

        return choice_periodos
