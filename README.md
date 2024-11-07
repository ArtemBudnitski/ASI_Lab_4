# Analizator Wyników s22402 - Dokumentacja

## 1. Opis projektu

Analizator Wyników to aplikacja FastAPI, która wykorzystuje model uczenia maszynowego do przewidywania wyników na podstawie danych wejściowych. Model został opublikowany w kontenerze Docker, co umożliwia łatwe wdrożenie i użytkowanie aplikacji. Obraz jest dostępny na Docker Hub.

---

## 2. Klonowanie repozytorium

Aby uzyskać dostęp do kodu projektu i wszystkich plików:

1. Otwórz terminal lub wiersz poleceń.
2. Wykonaj poniższą komendę, aby skopiować repozytorium do lokalnego folderu:

   ```bash
   git clone https://github.com/ArtemBudnitski/ASI_Lab_4.git
   cd ASI_Lab_4
   ```

---

## 3. Uruchamianie aplikacji lokalnie

Jeśli chcesz uruchomić aplikację na lokalnym serwerze, wykonaj poniższe kroki.

### Krok 1: Utworzenie i aktywacja środowiska wirtualnego (opcjonalnie)

Aby zapewnić izolację zależności:

Utwórz środowisko wirtualne:

```bash
python3 -m venv venv
```

Aktywuj środowisko:

- **Linux / macOS**:
  ```bash
  source venv/bin/activate
  ```

### Krok 2: Instalacja zależności

Zainstaluj wszystkie wymagane pakiety z pliku `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Krok 3: Uruchomienie serwera FastAPI

Aby uruchomić serwer Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Po uruchomieniu serwera aplikacja będzie dostępna pod adresem [http://localhost:8000](http://localhost:8000).

---

## 4. Uruchamianie aplikacji za pomocą Dockera

Aplikacja jest skonteneryzowana, co pozwala na uruchomienie jej w Dockerze.

### Budowanie obrazu Docker (lokalnie)

Jeśli chcesz zbudować obraz Docker na podstawie `Dockerfile`:

```bash
docker build -t analizator_wynikow_s22402_lab4 .
```

### Uruchomienie kontenera lokalnie

Po zbudowaniu obrazu możesz uruchomić kontener Docker:

```bash
docker run -p 8000:8000 analizator_wynikow_s22402_lab4
```

Aplikacja będzie dostępna pod adresem [http://localhost:8000](http://localhost:8000).

---

## 5. Korzystanie z obrazu Docker na Docker Hub

Obraz aplikacji jest dostępny na Docker Hub, co pozwala na pobranie i uruchomienie go bezpośrednio z repozytorium.

### Krok 1: Pobierz obraz

Aby pobrać obraz z Docker Hub:

```bash
docker pull artemik007/analizator_wynikow_s22402_lab4
```

### Krok 2: Uruchom obraz

Aby uruchomić pobrany obraz:

```bash
docker run -p 8000:8000 artemik007/analizator_wynikow_s22402_lab4
```

Aplikacja będzie dostępna pod adresem [http://localhost:8000](http://localhost:8000).

---

## 6. Korzystanie z API

Po uruchomieniu aplikacji (lokalnie lub w Dockerze) możesz uzyskać dostęp do endpointu `/predict`, który umożliwia przewidywanie wyniku na podstawie danych wejściowych.

### Endpoint

- **Metoda HTTP**: `POST`
- **URL**: `/predict`
- **Opis**: Endpoint przyjmuje dane wejściowe w formacie JSON i zwraca przewidywaną wartość `score`.

### Przykładowe dane wejściowe

API przyjmuje dane wejściowe w formacie **JSON**. Wymagane pola to:

- `unemp`: Wskaźnik bezrobocia (typ: liczba zmiennoprzecinkowa)
- `wage`: Średnie wynagrodzenie (typ: liczba zmiennoprzecinkowa)
- `distance`: Odległość (typ: liczba zmiennoprzecinkowa)
- `tuition`: Koszt nauki (typ: liczba zmiennoprzecinkowa)
- `education`: Poziom edukacji (typ: liczba zmiennoprzecinkowa)

**Przykładowe dane wejściowe JSON**:

```json
{
  "unemp": 5.2,
  "wage": 7.5,
  "distance": 10.3,
  "tuition": 2000.0,
  "education": 3.0
}
```

### Przesyłanie danych do API

#### Curl

Możesz użyć polecenia `curl` w terminalu, aby wysłać żądanie POST do API z danymi w formacie JSON.

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"unemp": 5.2, "wage": 7.5, "distance": 10.3, "tuition": 2000.0, "education": 3.0}'
```

#### Postman

Możesz użyć narzędzia Postman, aby przetestować API.

1. Otwórz Postmana i utwórz nowe żądanie.
2. Ustaw metodę na `POST` i URL na `http://localhost:8000/predict`.
3. Przejdź do zakładki **Body**, wybierz **raw** i ustaw typ na **JSON**.
4. Wklej przykładowe dane wejściowe JSON i kliknij **Send**.

### Przykładowa odpowiedź

Po przesłaniu poprawnych danych aplikacja zwróci przewidywany wynik w formacie JSON:

```json
{
  "predicted_score": 85.4
}
```

--- 

**Przykładowe dane wejściowe i odpowiedź z aplikacji Postman:**

1. **Dane wejściowe**:
   ```json
   {
     "unemp": 5.2,
     "wage": 7.5,
     "distance": 10.3,
     "tuition": 2000.0,
     "education": 3.0
   }
   ```

2. **Odpowiedź**:
   ```json
   {
     "predicted_score": 85.4
   }
   ```