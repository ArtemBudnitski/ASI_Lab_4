import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import pickle
import skl2onnx
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# Wczytanie danych
file_path = 'CollegeDistance.csv'  # Zamień na odpowiednią ścieżkę
data = pd.read_csv(file_path)

# Eksploracja danych
print("Podstawowe informacje o danych:")
data.info()

# Sprawdzenie brakujących wartości
missing_values = data.isnull().sum()
if missing_values.any():
    print("Plik zawiera puste dane w następujących kolumnach:")
    print(missing_values[missing_values > 0])
else:
    print("Plik nie zawiera pustych danych. Dane są kompletne.")

# Usunięcie kolumny 'rownames' (jeśli istnieje, inaczej pomiń)
if 'rownames' in data.columns:
    data.drop(columns=['rownames'], inplace=True)

# Statystyki opisowe dla zmiennych liczbowych
print("Statystyki opisowe dla zmiennych liczbowych:")
print(data.describe())

# Inżynieria cech: Standaryzacja cech liczbowych
features_to_scale = ['unemp', 'wage', 'distance', 'tuition', 'education']
scaler = StandardScaler()
data_scaled = data.copy()
data_scaled[features_to_scale] = scaler.fit_transform(data_scaled[features_to_scale])

# Kodowanie zmiennych kategorycznych (One-Hot Encoding)
data_encoded = pd.get_dummies(data_scaled, drop_first=True)

# Podział danych na cechy (X) i zmienną docelową (y)
X = data_encoded.drop(columns=['score'])  # Usunięcie kolumny docelowej 'score'
y = data_encoded['score']

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definicja funkcji do oceny modeli
def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'Wyniki modelu {model_name}:')
    print(f'MSE: {mse}')
    print(f'MAE: {mae}')
    print(f'R²: {r2}\n')
    return mse, mae, r2

# 1. Model Gradient Boosting Regressor bez optymalizacji
gbr = GradientBoostingRegressor(random_state=42)
gbr.fit(X_train, y_train)
evaluate_model(gbr, X_test, y_test, 'Gradient Boosting Regressor (bez optymalizacji)')

# 2. Model Random Forest bez optymalizacji
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)
evaluate_model(rf, X_test, y_test, 'Random Forest (bez optymalizacji)')

# 3. Optymalizacja hiperparametrów dla Gradient Boosting Regressor
param_grid_gbr = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 4, 5],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

grid_search_gbr = GridSearchCV(
    estimator=GradientBoostingRegressor(random_state=42),
    param_grid=param_grid_gbr,
    cv=5,
    n_jobs=-1,
    scoring='r2'
)

grid_search_gbr.fit(X_train, y_train)
best_gbr = grid_search_gbr.best_estimator_
print("Najlepsze parametry dla Gradient Boosting Regressor:")
print(grid_search_gbr.best_params_)

# Ocena najlepszego modelu Gradient Boosting
evaluate_model(best_gbr, X_test, y_test, 'Gradient Boosting Regressor (po optymalizacji)')

# 4. Optymalizacja hiperparametrów dla Random Forest
param_grid_rf = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

grid_search_rf = GridSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    param_grid=param_grid_rf,
    cv=5,
    n_jobs=-1,
    scoring='r2'
)

grid_search_rf.fit(X_train, y_train)
best_rf = grid_search_rf.best_estimator_
print("Najlepsze parametry dla Random Forest:")
print(grid_search_rf.best_params_)

# Ocena najlepszego modelu Random Forest
evaluate_model(best_rf, X_test, y_test, 'Random Forest (po optymalizacji)')


# Porównanie wyników przed i po optymalizacji
print(f"Regresja Gradient Boosting (bez optymalizacji) - R²: {r2_score(y_test, gbr.predict(X_test))}")
print(f"Regresja Gradient Boosting (po optymalizacji) - R²: {r2_score(y_test, best_gbr.predict(X_test))}")
print(f"Random Forest (bez optymalizacji) - R²: {r2_score(y_test, rf.predict(X_test))}")
print(f"Random Forest (po optymalizacji) - R²: {r2_score(y_test, best_rf.predict(X_test))}")

initial_type = [('float_input', FloatTensorType([None, X_train.shape[1]]))]

# Konwersja modelu do formatu ONNX
onnx_model = convert_sklearn(best_gbr, initial_types=initial_type)

# Zapisanie modelu ONNX
with open("best_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

with open('model_evaluation.txt', 'w') as f:
    f.write("Wyniki przed optymalizacją:\n")
    f.write(f"Regresja Gradient Boosting (bez optymalizacji) - R²: {r2_score(y_test, gbr.predict(X_test))}\n")
    f.write(f"Random Forest (bez optymalizacji) - R²: {r2_score(y_test, rf.predict(X_test))}\n\n")

    f.write("Wyniki po optymalizacji:\n")
    f.write(f"Regresja Gradient Boosting (po optymalizacji) - R²: {r2_score(y_test, best_gbr.predict(X_test))}\n")
    f.write(f"Random Forest (po optymalizacji) - R²: {r2_score(y_test, best_rf.predict(X_test))}")