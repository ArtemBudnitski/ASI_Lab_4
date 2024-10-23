import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# 1. Wczytanie danych
file_path = 'CollegeDistance.csv'  # Ścieżka do pliku
data = pd.read_csv(file_path)

# 2. Sprawdzenie brakujących wartości
print("Informacje o danych:")
print(data.info())
print("\nBrakujące wartości:")
print(data.isnull().sum())

# 3. Statystyczna analiza zmiennych liczbowych
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
print("\nStatystyki opisowe zmiennych liczbowych:")
print(data[numeric_columns].describe())

# Wykresy przed zakodowaniem zmiennych kategorycznych

# 4. Wykres rozkładu zmiennej 'score'
plt.figure(figsize=(8, 6))
plt.hist(data['score'], bins=30, color='blue', edgecolor='black')
plt.title('Rozkład zmiennej "score"')
plt.xlabel('Score')
plt.ylabel('Częstość')
plt.grid(True)
plt.savefig('charts/score_distribution.png')  # Zapisanie wykresu
plt.show()

# 5. Wykres pudełkowy dla zmiennej 'gender' a 'score'
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='score', data=data)
plt.title('Rozkład wyników w zależności od płci')
plt.xlabel('Gender')
plt.ylabel('Score')
plt.savefig('charts/gender_score_boxplot.png')  # Zapisanie wykresu
plt.show()

# 6. Wykres rozproszenia dla zmiennej 'distance' a 'score'
plt.figure(figsize=(8, 6))
plt.scatter(data['distance'], data['score'], color='purple', alpha=0.6)
plt.title('Wyniki w zależności od odległości od uczelni')
plt.xlabel('Odległość (mile)')
plt.ylabel('Score')
plt.grid(True)
plt.savefig('charts/distance_score_scatter.png')  # Zapisanie wykresu
plt.show()

# 7. Wykres słupkowy dla zmiennej 'income' a 'score'
plt.figure(figsize=(8, 6))
sns.barplot(x='income', y='score', data=data)
plt.title('Średni wynik w zależności od poziomu dochodów')
plt.xlabel('Income')
plt.ylabel('Średni wynik (Score)')
plt.savefig('charts/income_score_barchart.png')  # Zapisanie wykresu
plt.show()

# 8. Korelacja między zmiennymi liczbowymi
plt.figure(figsize=(10, 8))
correlation_matrix = data[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Macierz korelacji zmiennych liczbowych')
plt.savefig('charts/correlation_matrix.png')  # Zapisanie wykresu
plt.show()

# --- Dopiero teraz kodowanie zmiennych kategorycznych i modelowanie ---

# 9. Zakodowanie zmiennych kategorycznych
data_encoded = pd.get_dummies(data, drop_first=True)

# 10. Inżynieria cech: Standaryzacja wartości liczbowych
features_to_scale = ['unemp', 'wage', 'distance', 'tuition', 'education']
scaler = StandardScaler()
data_encoded[features_to_scale] = scaler.fit_transform(data_encoded[features_to_scale])

print("Standaryzacja cech liczbowych zakończona.")

# 11. Podział danych na cechy i zmienną docelową
X = data_encoded.drop(columns=['score'])
y = data_encoded['score']

# 12. Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 13. Trenowanie modelu Gradient Boosting
gbr = GradientBoostingRegressor(random_state=42)
gbr.fit(X_train, y_train)

# 14. Przewidywanie wartości
y_pred = gbr.predict(X_test)

# 15. Wykres porównania przewidywanych i rzeczywistych wartości 'score'
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', edgecolor='black', alpha=0.6)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')  # Linia idealnego dopasowania
plt.title('Porównanie przewidywanych i rzeczywistych wartości "score"')
plt.xlabel('Rzeczywiste wartości "score"')
plt.ylabel('Przewidywane wartości "score"')
plt.grid(True)
plt.savefig('charts/pred_vs_real_score.png')  # Zapisanie wykresu
plt.show()

# 16. Ocena modelu
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'R² (Współczynnik determinacji): {r2}')
