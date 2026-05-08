import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Wczytanie i czyszczenie
print("Wczytuję dane... (cierpliwości)")
df = pd.read_excel('Online Retail.xlsx')
df = df.dropna(subset=['CustomerID'])
df = df[~df['InvoiceNo'].astype(str).str.contains('C')]
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df['TotalSum'] = df['Quantity'] * df['UnitPrice']

# 2. Obliczanie RFM
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'count',
    'TotalSum': 'sum'
})
rfm.rename(columns={'InvoiceDate': 'Recency', 'InvoiceNo': 'Frequency', 'TotalSum': 'Monetary'}, inplace=True)

# 3. Segmentacja (Podział na 4 grupy)
r_labels = range(4, 0, -1)
f_labels = range(1, 5)
m_labels = range(1, 5)

rfm['R'] = pd.qcut(rfm['Recency'], q=4, labels=r_labels)
rfm['F'] = pd.qcut(rfm['Frequency'], q=4, labels=f_labels)
rfm['M'] = pd.qcut(rfm['Monetary'], q=4, labels=m_labels)

def assign_segment(row):
    if row['R'] == 4 and row['F'] == 4:
        return 'VIP'
    elif row['R'] <= 2:
        return 'Churn Risk'
    else:
        return 'Low Value'

rfm['Segment'] = rfm.apply(assign_segment, axis=1)

# 4. WYŚWIETLENIE WYNIKÓW
print("\n=== WYNIKI SEGMENTACJI ===")
print(rfm['Segment'].value_counts())
print("\n=== PODSUMOWANIE DLA ZARZĄDU ===")
print(rfm.groupby('Segment').agg({'Recency': 'mean', 'Frequency': 'mean', 'Monetary': 'mean'}).round(1))

# 5. Wykres
plt.figure(figsize=(10, 6))
sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Segment', palette='Set1')
plt.title('Segmentacja RFM - Wizualizacja')
plt.show()