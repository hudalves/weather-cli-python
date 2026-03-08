import requests
import pprint
import os

def clima():
    api_key = os.getenv("KEY")
    while True:
        city= input('digite uma cidade: ')
        days = int(input('Você quer saber a previsão de quantos dias: ')) 

        if days > 3:
            print('Número maximo de dias permitidos é 3')
            continue

        parametros={
            'key':api_key,
            'q':city,
            'days':days,
            'lang': 'pt'
        }

       
        forecast = 'http://api.weatherapi.com/v1/forecast.json'
    
        previsao = requests.get(forecast, params=parametros)

        if previsao.status_code == 200:
           
            dados_previsao = previsao.json()
         

            lista_dias = dados_previsao['forecast'] ['forecastday']

            for i in range(days):
                print('-=' * 25)

                print(f"Cidade: {dados_previsao['location']['name']}")
                print(f"Data: {lista_dias[i]['date']}")
                print(f"Clima: {lista_dias[i]['day']['condition']['text']}")
                print(f"Temperatura maxima: {lista_dias[i]['day']['maxtemp_c']}°C")
                print(f"Temperatura minima: {lista_dias[i]['day']['mintemp_c']}°C")
                print(f"Chance de chuva: {lista_dias[i]['day']['daily_chance_of_rain']}%")

                print('-=' * 25)

        d=input('pressione (f) para terminar. Aperte qualquer coisa para continuar: ')
        if d == 'f':
            break
        else:
            os.system('cls')
clima()