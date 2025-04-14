# 📈 Forex Signal Scraper

Um script automatizado em Python que utiliza Selenium para fazer web scraping de sinais de Forex em um site privado e envia os dados para um webhook via POST.

## 🚀 Visão Geral

Este projeto realiza:

- Login automático em um site de sinais Forex
- Extração de dados como símbolo, horários, preço, take profit e stop loss
- Envio automatizado desses dados para um endpoint configurável (webhook)
- Acesso em loop com delays aleatórios para simular comportamento humano

Ideal para traders que querem integrar sinais externos em sistemas próprios de automação ou alertas.


## ⚙️ Instalação

```bash
git clone https://github.com/rudineialves/forex-signal-scraper.git
cd forex-signal-scraper
pip install -r requirements.txt
```

Edite `main.py` com suas credenciais e URLs.

## ▶️ Como usar

```bash
python src/main.py
```
O script irá iniciar o Chrome via Selenium, logar no site, coletar os sinais e enviá-los periodicamente para o seu webhook.

## 📦 Requisitos

- Python 3.8+
- Google Chrome
- ChromeDriver compatível com sua versão do Chrome

## 🛡️ Aviso de uso

Este script simula ações humanas em um site protegido. Certifique-se de estar em conformidade com os Termos de Uso da plataforma da qual você está extraindo dados. O uso indevido pode levar ao banimento ou ações legais.

## 🧩 Exemplo de Payload enviado ao Webhook

```json
[
  {
    "symbol": "EURUSD",
    "timeAgo": "2 minutes ago",
    "timeFrom": "09:00",
    "timeTill": "11:00",
    "signalStatus": "Active",
    "dealPrice": "1.0830",
    "profit": "1.0880",
    "loss": "1.0800"
  }
]
```

## 📄 Licença

MIT License
