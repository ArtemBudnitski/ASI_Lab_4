## Dokumentacja dla Lab4 jest dostępna pod nazwą: Documentation_Lab4.pdf, a plik main.py zawiera skrypt dla tworzenia modelu.


# Lab4-Analizator_wynikow
Zadanie 2: Implementacja i publikacja modelu w Dockerze (20 punktów) Cel: W tym zadaniu studenci mają za zadanie stworzyć aplikację, która uruchomi model predykcyjny w kontenerze Docker. Następnie muszą opublikować ten kontener na platformie Docker Hub oraz stworzyć plik README.md na GitHubie, który wyjaśni proces uruchamiania aplikacji.

Etapy: Implementacja API lub skryptu przewidywania (5 punktów)

Stworzenie skryptu (np. w Pythonie z wykorzystaniem Flask, FastAPI lub CLI), który pozwoli na przewidywanie na podstawie dostarczonych danych. Skrypt powinien przyjmować dane w formacie JSON lub CSV i zwracać przewidywany wynik. Ocena: 5 punktów za poprawną implementację przewidywania.

Dockerfile (5 punktów)

Stworzenie poprawnego pliku Dockerfile, który umożliwia uruchomienie aplikacji w kontenerze. Obraz powinien być zoptymalizowany pod kątem wielkości oraz zawierać wszystkie potrzebne zależności. Ocena: 5 punktów za poprawny Dockerfile oraz uruchomienie aplikacji w kontenerze.

Publikacja w Docker Hub (5 punktów)

Stworzenie konta na Docker Hub. Opublikowanie obrazu Dockera z aplikacją na Docker Hub. Ocena: 5 punktów za poprawną publikację obrazu na Docker Hub.

README.md i dokumentacja (5 punktów)

Stworzenie repozytorium na GitHubie, które zawiera pliki projektu, w tym model oraz skrypt. Przygotowanie szczegółowego pliku README.md, który wyjaśnia kroki: a) Jak sklonować repozytorium. b) Jak uruchomić aplikację lokalnie. c) Jak uruchomić aplikację z wykorzystaniem Dockera. d) Instrukcje dotyczące korzystania z obrazu Docker z Docker Huba (jak go pobrać i uruchomić). Ocena: 5 punktów za kompletny i czytelny plik README.md oraz poprawną dokumentację.


# Lab3-Analizator_wynikow

https://vincentarelbundock.github.io/Rdatasets/csv/AER/CollegeDistance.csv

Proszę o wykorzystanie już zdobytej wiedzy i zautomatyzowanie procesów w GitHub Action.

Zadanie 1: Budowa modelu predykcyjnego (20 punktów)
Cel:
Na podstawie dostarczonego datasetu studenci mają za zadanie zbudować model predykcyjny, który będzie przewidywał zmienną score. Powinni wybrać odpowiedni algorytm, przeprowadzić analizę danych i ocenić jakość modelu. Do całej pracy ma zostać stworzona dokumentacja, może być w formie Readme.pdf i tam zamieszczone wykresy, albo można użyć bardziej profesjonalnego oprogramowania do tworzenia dokumentacji IT.

Etapy:
Eksploracja i wstępna analiza danych (5 punktów)

Wczytanie i zapoznanie się z danymi.
Sprawdzenie brakujących wartości oraz ich odpowiednia obsługa (np. imputacja lub usunięcie).
Analiza statystyczna zmiennych.
Ocena: 5 punktów za pełną eksplorację danych, w tym wykresy i opisy zmiennych.

Inżynieria cech i przygotowanie danych (5 punktów)

Przeprowadzenie odpowiedniej inżynierii cech (np. kategoryzacja, standaryzacja, normalizacja, tworzenie nowych zmiennych, jeśli konieczne).
Podział danych na zbiór treningowy i testowy.
Ocena: 5 punktów za poprawne przygotowanie danych, z wyjaśnieniem wszystkich kroków.

Wybór i trenowanie modelu (5 punktów)

Wybór odpowiedniego algorytmu (np. regresja liniowa, lasy losowe, regresja logistyczna, sieci neuronowe itp.).
Wytrenowanie modelu na zbiorze treningowym.
Wyjaśnienie, dlaczego wybrano dany model.
Ocena: 5 punktów za wybór odpowiedniego modelu i poprawne przeszkolenie modelu.

Ocena i optymalizacja modelu (5 punktów)

Ocena jakości modelu na zbiorze testowym (np. przy użyciu metryk takich jak R², MAE, MSE).
Jeśli wyniki nie są satysfakcjonujące, należy przeprowadzić optymalizację (np. tunowanie hiperparametrów, walidacja krzyżowa).
Ocena: 5 punktów za ocenę modelu i ewentualną optymalizację.

