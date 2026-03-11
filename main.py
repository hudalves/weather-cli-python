import requests
import os
from dotenv import load_dotenv

load_dotenv()


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def clima():

    api_key = os.getenv("KEY")

    if not api_key:
        print("API KEY não encontrada no arquivo .env")
        return

    while True:

        city = input("Digite uma cidade: ")

        try:
            days = int(input("Você quer saber a previsão de quantos dias (1-3): "))
            if days < 1 or days > 3:
                print("Digite um número entre 1 e 3.")
                continue
        except ValueError:
            print("Digite um número válido.")
            continue

        parametros = {
            'key': api_key,
            'q': city,
            'days': days,
            'lang': 'pt'
        }

        forecast = 'https://api.weatherapi.com/v1/forecast.json'

        try:
            previsao = requests.get(forecast, params=parametros, timeout=10)
        except requests.exceptions.RequestException:
            print("Erro ao conectar com a API.")
            continue

        if previsao.status_code == 200:

            dados_previsao = previsao.json()
            lista_dias = dados_previsao['forecast']['forecastday']

            for i in range(days):

                print('-=' * 25)

                print(f"Cidade: {dados_previsao['location']['name']}")
                print(f"Data: {lista_dias[i]['date']}")
                print(f"Clima: {lista_dias[i]['day']['condition']['text']}")
                print(f"Temperatura máxima: {lista_dias[i]['day']['maxtemp_c']}°C")
                print(f"Temperatura mínima: {lista_dias[i]['day']['mintemp_c']}°C")
                print(f"Chance de chuva: {lista_dias[i]['day']['daily_chance_of_rain']}%")

                print('-=' * 25)

        else:
            print("Erro ao buscar previsão.")
            print(previsao.text)

        d = input("Pressione (f) para terminar ou qualquer tecla para continuar: ")

        if d.lower() == 'f':
            break
        else:
            limpar_terminal()


if __name__ == "__main__":
    clima()