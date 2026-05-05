Analiza Sprzedaży i Rentowności Global Superstore


Przegląd Projektu

Ten projekt stanowi kompleksową, opartą na danych analizę zbioru danych "Global Superstore". Wykorzystując ekosystem data science języka Python, przekształciłem surowe rekordy transakcyjne w konkretne wnioski biznesowe, skupiając się na trendach sprzedaży, wyciekach rentowności oraz retencji klientów.


Dlaczego Ten Projekt?

Po wcześniejszym rozwijaniu narzędzi opartych na LLM (dużych modelach językowych), zdecydowałem się przenieść punkt ciężkości na Inżynierię Danych i Analitykę. Moim celem było wykazanie, że choć modele AI są potężne, ich wartość jest tak duża, jak wgląd w dane, na których bazują. Ten projekt służy jako most łączący moje doświadczenie w rozwoju technicznym z rosnącą wiedzą w zakresie wydobywania strategicznej wartości z rzłożonych zbiorów danych.


Proces

Aby dogłębnie zrozumieć kondycję biznesową przedsiębiorstwa, postępowałem zgodnie ze strukturalnym cyklem pracy analitycznej:
- Czyszczenie i Przetwarzanie Danych: Zarządzanie formatowaniem dat i lokalnymi typami danych w celu zapewnienia dokładności czasowej.
- Eksploracyjna Analiza Danych (EDA): Analiza rozkładu sprzedaży w różnych kategoriach produktów.
- Głęboka Analiza Rentowności: Identyfikacja produktów generujących straty poprzez obliczenie marż na poziomie podkategorii.
- Analiza Geoprzestrzenna: Mapowanie zysków na rynkach globalnych (APAC, EU, US itd.) w celu znalezienia anomalii regionalnych.
- Modelowanie Retencji: Obliczenie wskaźnika powracających klientów ("Repeat Customer Rate") w celu oceny lojalności wobec marki.


Kluczowe Wnioski

Analiza ujawniła kilka krytycznych obserwacji, które mogłyby zdefiniować na nowo strategię firmy:

- Pułapka "Stołów" (Tables): Pomimo wygenerowania ponad 750 000 sprzedaży, podkategoria Stoły przyniosła stratę netto w wysokości ponad 64 000, prawdopodobnie z powodu wysokich kosztów wysyłki lub nadmiernego udzielania rabatów.
- Wysokomarżowe "Drobne Towary": Papier i Etykiety okazały się najbardziej dochodowymi produktami pod względem marży, przy czym Papier osiągnął marżę zysku na poziomie 24,2%.
- Wyjątkowa Lojalność: Sklep szczyci się wskaźnikiem powracających klientów na poziomie 91,26%, co wskazuje na bardzo stabilną i lojalną bazę klientów, która wymaga mniejszych nakładów marketingowych na pozyskanie.
- Dysproporcje Regionalne: Kategoria Technologia jest głównym motorem zysku w regionie APAC (ponad 204 000), podczas gdy kategoria Meble (Furniture) zmaga się ze znacznymi trudnościami na rynku amerykańskim.


Technologia

- Python 3.12
- Pandas: Do manipulacji i agregacji danych.
- Matplotlib & Seaborn: Do zaawansowanej wizualizacji danych i map ciepła.
- Jupyter Notebook: Do interaktywnego programowania i dokumentacji.


Podsumowanie

Ten projekt dowodzi, że wysoki wolumen sprzedaży nie zawsze oznacza sukces biznesowy. Poprzez identyfikację konkretnych nierentownych produktów oraz regionów o wysokiej wydajności, stworzyłem mapę drogową dla optymalizacji wyniku finansowego Global Superstore.
