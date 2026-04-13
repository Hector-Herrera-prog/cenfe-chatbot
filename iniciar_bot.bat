@echo off
title FitBot - Gym CENFE
color 0C
echo.
echo  ========================================
echo   FITBOT - GYM CENFE
echo   Iniciando tu asistente virtual...
echo  ========================================
echo.

cd /d C:\Users\hecto\Documents\Kiro\cenfe-chatbot

echo  [1/3] Activando entorno virtual...
call venv\Scripts\activate

echo  [2/3] Iniciando servidor backend...
echo.
echo  El bot estara listo en unos segundos.
echo  NO cierres esta ventana mientras uses el chat.
echo  Para detener el bot presiona CTRL+C
echo.

echo  [3/3] Abriendo chat en el navegador...
start "" "frontend\index.html"

cd backend
uvicorn main:app --port 8000
