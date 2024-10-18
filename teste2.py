import requests

def get_municipios(uf, pagina_inicial=1, registros_por_pagina=50, max_paginas=5):
    municipios = []
    pagina = pagina_inicial
    base_url = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios'
    
    while pagina <= max_paginas:
        params = {
            'offset': (pagina - 1) * registros_por_pagina,
            'orderBy': 'nome'
        }
        
        response = requests.get(base_url, params=params)
        
        if response.status_code != 200:
            print(f"Erro na requisição: {response.status_code}")
            break
        
        data = response.json()
        
        if not data:  # Se a lista retornada estiver vazia, acabaram os dados
            break
        
        municipios.extend(data)
        
        if len(data) < registros_por_pagina:  # Se retornou menos que o solicitado, é a última página
            break
        
        pagina += 1
    
    return municipios

# Buscando municípios do estado de São Paulo (SP)
municipios_sp = get_municipios('SP')

for municipio in municipios_sp[:5]:  # Mostrando apenas os 5 primeiros municípios
    print(f"Nome: {municipio['nome']}")
    print(f"Microrregião: {municipio['microrregiao']['nome']}")
    print(f"Mesorregião: {municipio['microrregiao']['mesorregiao']['nome']}")
    print("---")