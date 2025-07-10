import wheather
import news



if __name__ == "__main__":
    print("-----Iniciando Asssistente Matinal-----")

    #1 - Buscar previsão do tempo
    print("\n Buscando previsão do tempo...")
    previsao = wheather.buscar_previsao_tempo()
    print(previsao)  # Exibe a previsão do tempo no console

    #2 - MAPS

    #3 - Buscar notícias
    print("----- Buscando news -----")
    noticias_tec = news.buscar_noticias("technology", 2)
    print(noticias_tec)  # Exibe as notícias de tecnologia no console
    noticias_ent = news.buscar_noticias("entertainment", 2)
    print(noticias_ent)  # Exibe as notícias de entretenimento no console


