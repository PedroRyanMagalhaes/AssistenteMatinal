import requests
import config

def enviar_mensagem(texto_mensagem):

    if not config.Telegram_Token or not config.Telegram_Chat_Id:
        print ("Erro no token do telegram")
        return False
    
    url_base = f"https://api.telegram.org/bot{config.Telegram_Token}/sendMessage"

    params = {
        'chat_id': config.Telegram_Chat_Id,
        'text': texto_mensagem,
        'parse_mode': 'Markdown'
    }

    try:
        resposta = requests.get(url_base, params=params)
        resposta.raise_for_status()

        resultado_json = resposta.json()
        if resultado_json.get("ok"):
            print ("MEnsagem enviada com Sucesso")
            return True
        else:
            print(f"Erro da API do telegram: {resultado_json.get('description')}")
            return False
    except requests.exceptions.RequestException as err:
        print(f"Erro de conexao: {err}")


if __name__ == "__main__":
    mensagem_teste = "Ola! Este é um *teste*"
    enviar_mensagem(mensagem_teste)
