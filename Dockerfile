# Wybierz oficjalny obraz Python jako bazowy
FROM python:3.9-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj plik requirements.txt do obrazu i zainstaluj zależności
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Skopiuj kod aplikacji oraz model ONNX do obrazu
COPY main.py best_model.onnx /app/

# Wystaw port 8000
EXPOSE 8000

# Uruchom aplikację FastAPI za pomocą Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]