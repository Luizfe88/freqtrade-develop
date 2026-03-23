# Polymarket Edge Strategy 🚀🤖

Este repositório contém a estratégia **Polymarket Edge** desenvolvida para o [Freqtrade](https://www.freqtrade.io).

---

## 🇧🇷 Português

### Descrição

Esta estratégia foi otimizada para operar no mercado de criptomoedas (Binance) usando uma abordagem baseada em indicadores técnicos personalizados e machine learning (FreqAI).

### Requisitos

- Python 3.11+
- Freqtrade (Desenvolvimento)
- Bibliotecas listadas em `requirements.txt`

### Como Iniciar

1.  **Configuração**:
    - Copie `user_data/config.json.example` para `user_data/config.json`.
    - Insira seus tokens do Telegram e chaves da API (se necessário).
    - **NUNCA** commite seu arquivo `config.json` real.

2.  **Execução**:
    - Use o arquivo `run_bot.bat` (Windows) para iniciar o robô em modo Dry-Run.

3.  **Otimização**:
    - O script `user_data/hyperopt_monthly.sh` está configurado para rodar a otimização mensalmente.

---

## 🇺🇸 English

### Description

The **Polymarket Edge Strategy** is designed for the Freqtrade bot, utilizing technical analysis and FreqAI for prediction.

### Quick Start

1.  **Configuration**:
    - Copy `user_data/config.json.example` to `user_data/config.json`.
    - Fill in your Telegram tokens and API keys.
    - **SECURITY**: `user_data/config.json` is ignored by git to protect your credentials.

2.  **Run**:
    - Execute `run_bot.bat` to start the bot in Dry-Run mode.

### Project Structure

- `user_data/strategies/`: Contains the core trading logic.
- `user_data/config.json`: Private configuration (ignored by git).
- `run_bot.bat`: Helper script to launch the bot.
- `simulacao_sniper_v46.py`: Quantitative simulation tool.

---

## 🛡️ Security

This project uses a `.gitignore` file to ensure that sensitive information like API keys and Telegram tokens are not exposed. Always use the `.example` files as templates.
