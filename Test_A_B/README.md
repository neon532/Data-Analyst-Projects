Analiza A/B Testu: Optymalizacja Konwersji Sprzedażowej


Opis Projektu

Projekt ten przedstawia pełny proces analizy testu A/B – od wygenerowania syntetycznych danych zakupowych, przez ich agregację, aż po weryfikację hipotez statystycznych. Celem było sprawdzenie, czy nowa szata graficzna strony (Wariant B) istotnie wpływa na zwiększenie współczynnika konwersji w porównaniu do wersji obecnej (Wariant A).


Metodologia

W projekcie wykorzystano język Python oraz biblioteki Pandas (do manipulacji danymi) i Statsmodels (do obliczeń statystycznych).

Proces analityczny:
1. Generowanie danych: Stworzenie zbioru 3000 użytkowników z losowym przydziałem do grup.
2. Parametry bazowe: Ustawienie prawdopodobieństwa zakupu na poziomie 10% dla grupy kontrolnej (A) oraz 13,2% dla grupy testowej (B).
3. Test statystyczny: Wykorzystanie testu Z dla proporcji (proportions_ztest), który jest standardem przy porównywaniu współczynników konwersji.
4. Powtarzalność: Zastosowanie ziarna losowości (seed), co gwarantuje powtarzalność wyników przy każdym uruchomieniu kodu.


Ewolucja Projektu i Porównanie Wyników

W trakcie prac nad projektem dokonano kluczowej zmiany parametrów, aby zwiększyć wiarygodność analizy:

Pierwsza faza (Próba 2000 osób, Seed 42):
-  Różnica w konwersji wyniosła około 3.07 punktu procentowego.
-  Wartość p-value oscylowała w okolicy 0.03.
-  Wynik był istotny, ale margines błędu był większy.

Druga faza (Próba 3000 osób, Seed 47):
-  Zwiększono liczbę użytkowników do 3000, aby uzyskać "gęstsze" dane.
-  Różnica w konwersji wzrosła do 4.00 punktów procentowych.
-  Wartość p-value spadła drastycznie do poziomu 0.0007.


Dlaczego zmieniliśmy dane?

Zwiększenie liczby użytkowników (wielkości próby) pozwoliło na uzyskanie znacznie silniejszego dowodu statystycznego. W analityce danych większa próba zazwyczaj oznacza mniejsze ryzyko błędu i większą pewność co do podjęcia decyzji biznesowej.


Interpretacja Wyników

Co oznacza wynik p-value (0.0007)?
Jest to kluczowy wskaźnik wiarygodności. Wynik ten mówi nam, że istnieje zaledwie 0,07% szansy na to, że zaobserwowany wzrost konwersji jest dziełem czystego przypadku. W standardach rynkowych każdy wynik poniżej 5% (0.05) uznaje się za istotny, więc nasz wynik jest ekstremalnie silny.


Wniosek Biznesowy:

Wariant B (nowa szata graficzna) zwiększa konwersję o 4 punkty procentowe. Przy skali tysięcy użytkowników taka zmiana przekłada się na realny i wysoki wzrost przychodów firmy. Rekomendowane jest wdrożenie Wariantu B na stałe.
