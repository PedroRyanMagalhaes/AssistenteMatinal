import weather
import news
import maps
import telegram



if __name__ == "__main__":
    print("-----Iniciando Asssistente Matinal-----")

    #1 - Buscar previsão do tempo
    print("\n Buscando previsão do tempo...")
    info_clima = weather.buscar_previsao_tempo()

    #2 - MAPS
    print("\nCalculando tempo de viagem...")
    info_maps = maps.buscar_tempo_transito()

    #3 - Buscar notícias
    print("\n----- Buscando news -----")
    info_tec = news.buscar_noticias("technology", 2)
    info_ent = news.buscar_noticias("entertainment", 2)

    mensagem_final= (
        f"*GOOD MORNING* 🌞 \n"
        f"-----------------------\n"
        f"⛅ {info_clima}\n"
        f"-----------------------\n"
        f"🚘{info_maps}\n"
        f"-----------------------\n"
        f"💻 {info_tec}\n\n"
        f"📽 {info_ent}\n"
    )

    print("\nEnviando mensagem Telegram")
    telegram.enviar_mensagem(mensagem_final)
    print("\nFinaliado")

