import requests
import config

def buscar_noticias(categoria, quant=2):
    
    """
    Busca uma quantidade definida de noticias de uma categoria.
    """

    if not config.NewsApi_Key:
        return "Chave de API news não configurada."
    
    url_base = "https://newsapi.org/v2/top-headlines"

    parametros = {
        'apiKey': config.NewsApi_Key,
        'country': config.Pais_Noticias,
        'category': categoria,
        'pageSize': quant
    }

    try:
        resposta = requests.get(url_base, params=parametros)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados_noticias = resposta.json()

        artigos = dados_noticias.get('articles', [])

        if not artigos:
            return f"Nenhuma notícia da {categoria} encontrada."
        
        manchetes = [f"News about {categoria.capitalize()}:"]
        for artigo in artigos:
            manchetes.append(f"- {artigo['title']}")

        return "\n".join(manchetes)
    
    except requests.exceptions.HTTPError as http_err:
        dados = resposta.json()
        return f"Erro ao buscar noticias ({categoria}): {dados.get('message', str(http_err))}"
    except Exception as err:
        return f"Erro ao buscar noticias ({categoria}): {str(err)}"
    

if __name__ == "__main__":
    print ("-----Teste de noticias-----")
    
    noticias_tec = buscar_noticias("technology", 2)
    print(noticias_tec)  

    noticias_ent= buscar_noticias("entertainment", 2)
    print(noticias_ent) 
    