@echo off
echo.
echo ========================================================
echo   FREQTRADE — POLYMARKET EDGE STRATEGY (v15) 🚀🤖
echo ========================================================
echo   Timeframe: 1h
echo   Config: user_data/config.json
echo   Modo: Dry Run (Simulado)
echo ========================================================
echo.
freqtrade trade --strategy PolymarketEdgeStrategy -c user_data/config.json
echo.
echo O robô foi interrompido.
pause
