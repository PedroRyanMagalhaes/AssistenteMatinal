import requests
import config

"""
    Busca a previsão do tempo atual para a cidade definida no arquivo config.
"""
def buscar_previsao_tempo():
    if not config.Weather_api_key in config.Weather_api_key:
        return "Chave API weather fora do ar."
    
    url_base = "http://api.weatherapi.com/v1/forecast.json"

   
    params = {
        "q": config.Cidade,  
        "key": config.Weather_api_key, 
        "days": 1,
        "aqi": "no", 
        "alerts" : "no"  
    }
    
    try: 
        
        resposta = requests.get(url_base, params=params) 
        
        # Verifica se a requisição foi um sucesso (código 200)
        resposta.raise_for_status()

      
        dados_clima = resposta.json()

       
        descricao = dados_clima["current"]["condition"]["text"]
        temp_atual = dados_clima["current"]["temp_c"]

        forecast_dia = dados_clima["forecast"]["forecastday"][0]["day"]
        temp_max = forecast_dia["maxtemp_c"]
        temp_min = forecast_dia["mintemp_c"]

        # O :.0f formata o número para não ter casas decimais.
        texto_clima = (
            f"{descricao}\n"
            f"Current weather: {temp_atual: .0f}°C\n"
            f"Max: {temp_max: .0f}°C\n"
            f"Min: {temp_min: .0f}°C"
        )
        return texto_clima  
    
    except requests.exceptions.HTTPError as http_err:

        if resposta.status_code == 401:
            return "Chave API inválida ou não autorizada."
        elif resposta.status_code == 404:
            return "Cidade não encontrada. Verifique o nome da cidade."
        else:
            return f"Erro HTTP: {http_err}"
    except requests.exceptions.RequestException as err:
        return f"Erro ao conectar com a API: {err}"
    
if __name__ == "__main__":
    previsao = buscar_previsao_tempo()
    print ("-----Previsao do tempo-----")
    print(previsao)  

