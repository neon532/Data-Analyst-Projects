import os
import csv
from openai import OpenAI
from dotenv import load_dotenv

# wczytanie klucza API z pliku o nazwie "open_ai__api_key" - między " "wpisz nazwę swojego pliku z API key
load_dotenv(dotenv_path="open_ai__api_key")
# przypisanie klucza API do zmiennej
api_key = os.getenv("OPENAI_API_KEY")

# stworzenie klienta OpenAI
client = OpenAI(api_key=api_key)

def analyze_opinion(opinion_text):
    # prosta obsługa błędów, aby program nie padł przy braku środków
    try:
        # wywołanie modelu językowego
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an analyst. Please respond only in JSON format."},
                {"role": "user", "content": f"Rate the sentiment and summarize it in 1 sentence: {opinion_text}"}
            ],
            response_format={ "type": "json_object" }
        )
        # zwrot treści odpowiedzi
        return response.choices[0].message.content
    except Exception as e:
        # zwrot komunikatu o błędzie
        return f"Error: {e}"

# proces czytania pliku i analiza
# inicjalizacja pustej listy na wyniki
results_to_save = []

# wyświetlenie nagłówka tabeli w konsoli
print(f"{'ID':<4} | {'OPINION':<40} | {'RESULT'}")
# wyświetlenie linii oddzielającej
print("-" * 100)

# otwarcie pliku do odczytu
with open("opinion_base.txt", "r", encoding="utf-8") as file:
    # wczytanie wszystkich linii z pliku
    lines = file.readlines()
    
    # licznik porządkowy id
    id_number = 1
    for line in lines:
        # usunięcie pustych znaków i wierszy
        clean_line = line.strip()
        
        # pominięcie instrukcji w pliku txt oraz pustej linii
        if not clean_line or clean_line.startswith("Instruction:"):
            continue
            
        # wywołanie analizy
        analysis_result = analyze_opinion(clean_line)
        
        # dodanie słownika z danymi do listy wyników
        results_to_save.append({
            "id": id_number,
            "opinion": clean_line,
            "result": analysis_result
        })
        
        # generowanie tabeli z wynikami w konsoli
        # :<40 oznacza, że opinia zajmie 40 znaków szerokości (skrócona dla czytelności)
        short_opinion = (clean_line[:37] + '..') if len(clean_line) > 37 else clean_line
        # wyświetlenie wiersza danych
        print(f"{id_number:<4} | {short_opinion:<40} | {analysis_result}")
        
        # inkrementacja numeru id
        id_number += 1

# generowanie pliku csv z tabelą z opiniami
# nazwa pliku wynikowego
csv_file = "analysis_results.csv"
# używam utf-8-sig aby , jeśli są polskie znaki były poprawnie wyświetlane

with open(csv_file, mode="w", newline="", encoding="utf-8-sig") as f:
    # definicje nazw kolumn
    fieldnames = ["id", "opinion", "result"]

    # używam średnika, żeby Excel w PL dobrze oddzielił od siebie kolumny
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
    
    # zapis nagłówków kolumn
    writer.writeheader()
    # zapis wszystkich zebranych wierszy danych
    writer.writerows(results_to_save)

# wyświetlenie komunikatu o sukcesie zapisu pliku
print(f"\nWyniki zostały zapisane do pliku: {csv_file}")