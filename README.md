# 📈 Forex Signal Scraper

Um script automatizado em Python que utiliza Selenium para fazer web scraping de sinais de Forex em um site privado e envia os dados para um webhook via POST.

## 🚀 Visão Geral

Este projeto realiza:

- Login automático em um site de sinais Forex
- Extração de dados como símbolo, horários, preço, lucro e perda
- Envio automatizado desses dados para um endpoint configurável (webhook)
- Acesso em loop com delays aleatórios para simular comportamento humano

## ⚙️ Instalação

```bash
git clone https://github.com/seu-usuario/forex-signal-scraper.git
cd forex-signal-scraper
pip install -r requirements.txt
```

Edite `main.py` com suas credenciais e URLs.

## ▶️ Como usar

```bash
python src/main.py
```

## 📦 Requisitos

- Python 3.8+
- Google Chrome
- ChromeDriver compatível

## 🛡️ Aviso de uso

Certifique-se de estar em conformidade com os Termos de Uso do site de origem.

## 📄 Licença

MIT License
