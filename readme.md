# 🌤️ CLI de Previsão do Tempo em Python

Este é um projeto simples de **linha de comando (CLI)** desenvolvido em **Python** que consulta a previsão do tempo de uma cidade utilizando a **WeatherAPI**.

O programa permite ao usuário digitar o nome de uma cidade e escolher quantos dias de previsão deseja visualizar.

---

## 🚀 Funcionalidades

* Consultar previsão do tempo por cidade
* Mostrar previsão de **1 a 3 dias**
* Exibir:

  * Cidade
  * Data
  * Condição do clima
  * Temperatura máxima
  * Temperatura mínima
  * Chance de chuva
* Limpeza automática do terminal entre consultas
* Uso de **variáveis de ambiente para segurança da API Key**

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Requests
* Python-dotenv
* WeatherAPI

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/api-clima-python.git
```

Entre na pasta do projeto:

```bash
cd api-clima-python
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

### Windows (PowerShell)

```bash
.\venv\Scripts\Activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install requests python-dotenv
```

---

## 🔑 Configuração da API

Crie um arquivo `.env` na raiz do projeto:

```
KEY=sua_api_key_aqui
```

Você pode obter uma API Key gratuita em:

https://www.weatherapi.com/

---

## ▶️ Como executar

Execute o programa com:

```bash
python main.py
```

O terminal irá pedir:

```
Digite uma cidade:
Você quer saber a previsão de quantos dias (1-3):
```

---

## 💻 Exemplo de uso

```
Digite uma cidade: Sao Paulo
Você quer saber a previsão de quantos dias (1-3): 2

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Cidade: São Paulo
Data: 2026-03-11
Clima: Parcialmente nublado
Temperatura máxima: 28°C
Temperatura mínima: 19°C
Chance de chuva: 40%
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
```

---

## 📂 Estrutura do projeto

```
API.Clima
│
├── main.py
├── .env
├── venv/
└── README.md
```

---

## 📚 Aprendizados

Este projeto foi desenvolvido para praticar:

* Consumo de APIs REST
* Manipulação de JSON
* Uso de variáveis de ambiente
* Criação de aplicações CLI
* Tratamento de erros em Python

---

## 👨‍💻 Autor

Hudson Alves

* GitHub: https://github.com/hudalves

---

## 📜 Licença

Este projeto é apenas para fins de estudo.
