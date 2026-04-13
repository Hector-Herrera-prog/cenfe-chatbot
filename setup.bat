@echo off
python -m venv venv
call venv\Scripts\activate
pip install -r backend\requirements.txt
copy .env.example .env
echo Edita .env con tu GROQ_API_KEY
