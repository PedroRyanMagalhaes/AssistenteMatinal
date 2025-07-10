import requests
import config

"""
    Busca a previsão do tempo atual para a cidade definida no arquivo de configuração.
    Retorna uma string formatada ou uma mensagem de erro.
"""
def buscar_previsao_tempo():
    if not config.Weather_api_key in config.Weather_api_key:
        return "Chave API do OpenWeatherMap fora do ar."
    
    # Este é o endereço base da API do OpenWeatherMap para previsão do tempo atual
    url_base = "http://api.weatherapi.com/v1/forecast.json"

    # Parâmetros que enviaremos na nossa requisição.
    # É como preencher um formulário para pedir a informação
    params = {
        "q": config.Cidade,  # Cidade para a qual queremos a previsão
        "key": config.Weather_api_key,  # Nossa chave de API para autenticação7
        "days": 1,
        "aqi": "no", # Queremos a temperatura em graus Celsius
        "alerts" : "no"  # Queremos a resposta em português
    }
    
    try: 
        # AQUI ACONTECE A MÁGICA:
        # O requests.get() envia uma requisição GET para a URL com os nossos parâmetros.
        # É o equivalente a acessar o site no navegador.
        resposta = requests.get(url_base, params=params)  # Faz a requisição para a API
        
        # Verifica se a requisição foi um sucesso (código 200)
        resposta.raise_for_status()

        # A API retorna os dados em um formato chamado JSON.
        # O .json() transforma esse texto em um dicionário Python para podermos usar.
        dados_clima = resposta.json()

        # Agora, pegamos as informações que queremos de dentro do dicionário.
        # A estrutura do dicionário é definida pela documentação da API.
        descricao = dados_clima["current"]["condition"]["text"]
        temp_atual = dados_clima["current"]["temp_c"]

        forecast_dia = dados_clima["forecast"]["forecastday"][0]["day"]
        temp_max = forecast_dia["maxtemp_c"]
        temp_min = forecast_dia["mintemp_c"]

        # Montamos a nossa string final com as informações formatadas.
        # O :.0f formata o número para não ter casas decimais.
        texto_clima = (
            f"Clima {descricao}\n"
            f"Temperatura atual: {temp_atual: .0f}°C\n"
            f"Máxima de hoje: {temp_max: .0f}°C\n"
            f"Mínima de hoje: {temp_min: .0f}°C"
        )
        return texto_clima  # Retorna a string formatada com as informações do clima
    
    except requests.exceptions.HTTPError as http_err:
    # Se a API retornar um erro (ex: chave inválida, cidade não encontrada)
        if resposta.status_code == 401:
            return "Chave API inválida ou não autorizada."
        elif resposta.status_code == 404:
            return "Cidade não encontrada. Verifique o nome da cidade."
        else:
            return f"Erro HTTP: {http_err}"
    except requests.exceptions.RequestException as err:
        # Se houver outro tipo de erro na requisição (ex: problemas de conexão)
        return f"Erro ao conectar com a API: {err}"
    
if __name__ == "__main__":
    previsao = buscar_previsao_tempo()
    print ("-----Previsao do tempo-----")
    print(previsao)  # Exibe a previsão do tempo no console

