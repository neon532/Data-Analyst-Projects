import pandas as pd # Import biblioteki do manipulacji tabelami danych
from statsmodels.stats.proportion import proportions_ztest # Import narzędzia do obliczeń statystycznych

# 1. Wczytanie danych
# Odczyt pliku tekstowego CSV i zamiana go na tabelę w pamięci komputera
df = pd.read_csv('ab_test_results.csv')

# 2. Agregacja wyników
# Grupowanie rekordów według przypisanej grupy (A lub B) oraz zliczanie zakupów i wszystkich wejść
results = df.groupby('group')['purchase'].agg(['sum', 'count'])

# Nadanie czytelnych nazw kolumnom: suma zakupów oraz całkowita liczba użytkowników
results.columns = ['purchases', 'total_users']

# Obliczenie wskaźnika konwersji (iloraz liczby zakupów przez liczbę osób) dla każdego wariantu
results['conversion_rate'] = results['purchases'] / results['total_users']

# Wyświetlenie tabeli z podsumowaniem liczbowym na ekranie
print("--- Podsumowanie Grup ---")
print(results)

# 3. Przygotowanie danych do testu Z (proportions_ztest)
# Wyodrębnienie samych liczb dotyczących zakupów i odwrócenie ich kolejności (format wymagany przez test: najpierw B, potem A)
count = results['purchases'].values[::-1] 

# Wyodrębnienie całkowitej liczby użytkowników w tym samym formacie (B, A)
nobs = results['total_users'].values[::-1]

# Realizacja testu statystycznego - generowanie wyniku siły różnicy (z_score) oraz prawdopodobieństwa błędu (p_value)
z_score, p_value = proportions_ztest(count, nobs)

# 4. Interpretacja
# Wyliczenie czystej różnicy w konwersji między grupą nową (B) a starą (A) i zamiana na punkty procentowe
diff = (results.loc['B', 'conversion_rate'] - results.loc['A', 'conversion_rate']) * 100

# Wyświetlenie nagłówka końcowego
print(f"\n--- Wyniki Analizy ---")

# Prezentacja różnicy w konwersji z zaokrągleniem do dwóch miejsc po przecinku
print(f"Różnica w konwersji: {diff:.2f} punktów procentowych")

# Prezentacja wartości p-value - kluczowego wskaźnika wiarygodności wyniku
print(f"p-value: {p_value:.4f}")

# Warunek logiczny: sprawdzenie, czy p-value jest mniejsze niż standardowy próg 0,05
if p_value < 0.05:
    # Komunikat o sukcesie: różnica jest na tyle duża, że nie może być dziełem przypadku
    print("Wynik jest ISTOTNY statystycznie. Wariant B działa lepiej!")
else:
    # Komunikat o braku pewności: różnica może wynikać z losowego szumu w danych
    print("Brak podstaw do odrzucenia hipotezy zerowej - wynik może być przypadkowy.")