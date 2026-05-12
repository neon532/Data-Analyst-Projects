import pandas as pd
import numpy as np

# Ustawiamy ziarno dla powtarzalności wyników
np.random.seed(47)

# Liczba użytkowników biorących udział w teście
n_users = 3000

# Tworzymy bazę użytkowników i przypisujemy ich losowo do grup
data = pd.DataFrame({
    'user_id': range(1, n_users + 1),
    'group': np.random.choice(['A', 'B'], size=n_users),
})

"""
WYJAŚNIENIE WARTOŚCI KONWERSJI:
Wartości zostały dobrane na podstawie średnich rynkowych dla sektora e-commerce.
Według raportów (np. Adobe Digital Index czy Wolfgang Digital), 
średnia konwersja w handlu online oscyluje wokół 2-5%, jednak dla landing page'y 
o wysokiej optymalizacji (tzw. 'High Performance') standardem jest ok. 10%.

- 10.0% (Wariant A): Przyjęty jako 'Baseline' (obecna wersja strony).
- 13.2% (Wariant B): Symulowany wzrost o 3.2 p.p. wynikający z nowej szaty graficznej.
Dobrana różnica pozwala uzyskać istotność statystyczną (p-value < 0.05) przy próbie 2000 osób.
"""

def simulate_purchase(group):
    if group == 'A':
        # Symulujemy konwersję 10% dla starej wersji strony
        return np.random.binomial(1, 0.10)
    else:
        # Symulujemy konwersję 13.2% dla nowej wersji strony
        return np.random.binomial(1, 0.132)

data['purchase'] = data['group'].apply(simulate_purchase)

# Zapis do CSV
data.to_csv('ab_test_results.csv', index=False)
print("Plik ab_test_results.csv został wygenerowany z uwzględnieniem parametrów rynkowych.")