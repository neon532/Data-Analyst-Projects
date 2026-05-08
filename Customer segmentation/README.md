Segmentacja klientów sklepu internetowego na podstawie analizy RFM


Opis projektu

W tym projekcie przeanalizowano zachowania klientów brytyjskiego sklepu internetowego na podstawie modelu RFM (Recency, Frequency, Monetary). Analiza została wykonana na zbiorze „Online Retail Dataset”, który zawiera ponad 540 tysięcy transakcji.
Głównym celem było sprawdzenie, jakie grupy klientów można wyróżnić oraz w jaki sposób firma może lepiej dopasować działania marketingowe do konkretnych odbiorców, zamiast stosować jedną komunikację dla wszystkich.


Wykorzystane technologie

Projekt został wykonany w Pythonie 3.12 z użyciem następujących bibliotek:
-  Pandas — czyszczenie danych i przygotowanie agregacji
-  Matplotlib oraz Seaborn — tworzenie wykresów i wizualizacji
-  Scikit-learn — przygotowanie danych pod modele uczenia maszynowego, m.in. K-Means
-  Openpyxl — obsługa dużych plików Excel


Na czym polega analiza RFM

Każdy klient został oceniony w trzech obszarach:
-  Recency — ile dni minęło od ostatniego zakupu,
-  Frequency — jak często klient składał zamówienia,
-  Monetary — ile pieniędzy łącznie wydał w sklepie.

Dzięki temu możliwe było podzielenie klientów na grupy o podobnych zachowaniach zakupowych.


Najważniejsze wnioski z analizy

Klienci VIP (Champions):
To najbardziej wartościowa grupa klientów. Zakupy wykonywali bardzo niedawno — średnio około 7 dni przed datą analizy. Wyróżniają się również bardzo wysoką liczbą zamówień oraz zdecydowanie większymi wydatkami niż pozostali klienci.
To właśnie ta grupa generuje dużą część przychodów firmy i ma największe znaczenie dla stabilności biznesu.

Klienci aktywni o niższej wartości (Low Value):
Są to osoby, które nadal regularnie kupują w sklepie, jednak ich średnia wartość zakupów pozostaje umiarkowana. Ostatni zakup wykonywali średnio około 24 dni wcześniej.
Ta grupa ma potencjał do dalszego rozwoju, ale wymaga odpowiednich działań marketingowych i budowania większej lojalności wobec marki.

Klienci zagrożeni odejściem (Churn Risk):
W tej grupie znalazły się osoby, które nie wracały do sklepu od ponad 160 dni. Ich wydatki były najniższe spośród wszystkich segmentów.
Może to oznaczać, że przeszli do konkurencji albo dokonali jednorazowych zakupów wyłącznie podczas promocji.


Propozycje działań biznesowych

-  Utrzymanie klientów VIP
   W przypadku najbardziej wartościowych klientów lepszym rozwiązaniem niż standardowe rabaty może być program lojalnościowy oparty na dodatkowych korzyściach.
   Przykładowo:
   -  wcześniejszy dostęp do nowych produktów,
   -  priorytetowa obsługa,
   -  oferty dostępne wyłącznie dla stałych klientów.
   Takie działania pomagają budować długoterminową relację z marką bez konieczności ciągłego obniżania marży.

-  Reaktywacja klientów zagrożonych odejściem
   Dla klientów z segmentu Churn Risk warto przygotować kampanie przypominające o sklepie, np. wiadomości typu „wróć do nas”.
   Dobrym rozwiązaniem może być ograniczony czasowo kod rabatowy lub spersonalizowana oferta przygotowana na podstawie wcześniejszych zakupów.

-  Zwiększanie wartości koszyka
   W grupie Low Value można skupić się na rekomendacjach produktów powiązanych z wcześniejszymi zakupami klienta.
   Mechanizmy typu:
   -  „inni kupili również…”,
   -  „do tego produktu pasuje…”,
   mogą pomóc zwiększyć wartość pojedynczego zamówienia i stopniowo przesuwać klientów do segmentu VIP.

-  Lepsze wykorzystanie budżetu marketingowego
   Analiza pokazała również, że nie każda grupa klientów wymaga takiego samego poziomu inwestycji marketingowych.
   W praktyce bardziej opłacalne może być skupienie większej części budżetu na utrzymaniu klientów o wysokiej wartości zakupowej niż na kosztownych kampaniach remarketingowych kierowanych do osób o niskim potencjale zakupowym.
