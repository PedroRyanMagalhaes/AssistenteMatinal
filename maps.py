import requests
import config

def buscar_tempo_transito():

    if not config.Maps_Api_Key:
        return "chave Maps nao configurada"
    
    url_base = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {
        'key': config.Maps_Api_Key,
        'origins': config.Endereço_Origem,
        'destinations': config.Endereço_Destino,
        'departure_time':'now',
        'language': 'pt-BR'
    }

    try:
        resposta = requests.get(url_base, params=params)
        resposta.raise_for_status()
        dados = resposta.json()

        status = dados.get('status')
        if status != "OK":
            return f"Erro da Api google: {dados.get('error_massage', status)}"
        
        element = dados['rows'][0]['elements'][0]
        status_element = element.get('status')

        if status_element == "OK":
            if 'duration_in_traffic' in element:
                duracao_texto = element['duration_in_traffic']['text']
                return f'Travel time to work (without traffic): {duracao_texto}'
            else:
                duracao_texto = element['duration']['text']
                return f"Travel time to work (without traffic):  {duracao_texto}"
        else:
            return f"Não foi possivel calcular a rota: Verifique os endereços (Status: {status_element})"
        
    except requests.exceptions.HTTPError as http_err:
        return f"Erro HTTP: {http_err}"
    except Exception as err:
        return f"Ocorreu erro geral: {err}"
    
if __name__ == "__main__":
    tempo = buscar_tempo_transito()
    print ("----INFORMAÇÔES DO TRÂNSITO-----")
    print (tempo)