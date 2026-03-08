import click
import requests
import pprint
import os

@click.command(help = 'Ferramenta de linha de comando para consultar previsão do tempo.')
def clima():
    api_key = os.getenv("KEY")

    while True:
        city= click.prompt('digite uma cidade ', type= str)
        days = click.prompt('Você quer saber a previsão de quantos dias ', type= click.IntRange(1, 3))

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
                click.echo('-=' * 25)

                click.echo(f"Cidade: {dados_previsao['location']['name']}")
                click.echo(f"Data: {lista_dias[i]['date']}")
                click.echo(f"Clima: {lista_dias[i]['day']['condition']['text']}")
                click.echo(f"Temperatura maxima: {lista_dias[i]['day']['maxtemp_c']}°C")
                click.echo(f"Temperatura minima: {lista_dias[i]['day']['mintemp_c']}°C")
                click.echo(f"Chance de chuva: {lista_dias[i]['day']['daily_chance_of_rain']}%")

                click.echo('-=' * 25)
        else:
            click.echo("Erro ao buscar previsão.")

        d= click.prompt('pressione (f) para terminar. Aperte qualquer coisa para continuar ', type= str)
        if d == 'f':
            break
        else:
            if os.name == 'nt':
                os.system('cls')
                
            else:
                os.system('clear')

if __name__ == "__main__":
    clima()