import requests
import pandas as pd
import csv
import json

PAGE = 0
URL_BASE = "http://api.salic.cultura.gov.br/v1/projetos/?limit=100&offset="
URL_BASE_END = "&format=json&"
url = URL_BASE + str(PAGE) + URL_BASE_END

req = requests.get(URL_BASE + str(PAGE) + URL_BASE_END)
json_parsed = json.loads(req.content)
total_elems = json_parsed['total']
lenght = int(total_elems / 100) * 100
salic = list()

while PAGE <= lenght:
    req = requests.get(URL_BASE + str(PAGE) + URL_BASE_END)
    PAGE += 100
    parametros = {'formato': 'json', 'itens': 1}
    dados = req.json()['_embedded']
    projetos = dados['projetos']
    for projeto in projetos:
        info = {
            'nome': projeto['nome'], 'proponente': projeto['proponente'],
            'providencia': projeto['providencia'], 'etapa': projeto['etapa'],
            'area': projeto['area'], 'ficha_tecnica': projeto['ficha_tecnica'],
            'situacao': projeto['situacao'], 'sinopse': projeto['sinopse'],
            'codigo': projeto['cgccpf'], 'mecanismo': projeto['mecanismo'],
            'segmento': projeto['segmento'], 'pronac': projeto['PRONAC'],
            'ano': int(projeto['ano_projeto']),
            'valor_solicitado': int(projeto['valor_solicitado']),
            'valor_aprovado': int(projeto['valor_aprovado']),
            'valor_projeto': int(projeto['valor_projeto']),
            'estrategia_execucao': projeto['estrategia_execucao'],
            'justificativa': projeto['justificativa'], 'resumo': projeto['resumo'],
            'municipio': projeto['municipio'], 'data_termino': projeto['data_termino'],
            'UF': projeto['UF'], 'data_inicio': projeto['data_inicio'],
            'valor_captado': int(projeto['valor_captado']),
            'valor_proposta': int(projeto['valor_proposta']),
            'democratizacao': projeto['democratizacao'],
            'estrategia_execucao': projeto['estrategia_execucao'],
            'acessibilidade': projeto['acessibilidade'],
            'enquadramento': projeto['enquadramento'], 'objetivos': projeto['objetivos']
        }
        salic.append(info)

df = pd.DataFrame(salic, columns= ['nome', 'proponente', 'providencia', 'etapa', 'area', 'ficha_tecnica', 'situacao', 'sinopse', 'codigo', 'mecanismo', 'segmento', 'pronac', 'ano', 'valor_solicitado', 'valor_aprovado', 'valor_projeto', 'estrategia_execucao', 'justificativa', 'resumo', 'municipio', 'data_termino', 'UF', 'data_inicio', 'valor_captado', 'valor_proposta', 'democratizacao', 'estrategia_execucao', 'acessibilidade', 'enquadramento', 'objetivos'])
df.to_csv("salic3.csv", index=False, header=True)
