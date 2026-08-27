import pandas as pd

# Örnek Veri Setimiz
df = pd.DataFrame({
    'Dep': ['Web', 'Web', 'Web', 'Mobil', 'Mobil', 'Veri', 'Veri'],
    'Calisan': ['Ahmet', 'Mehmet', 'Ayşe', 'Can', 'Deniz', 'Ece', 'Kaan'],
    'Dil': ['Python', 'Python', 'Java', 'Java', 'Kotlin', 'Python', 'R'],
    'Maas': [100, 110, 90, 95, 105, 120, 115],
    'Tecrube': [5, 6, 3, 4, 5, 7, 6],
    'Proje_Sayisi': [12, 15, 8, 10, 11, 18, 14]
})


# --------------------------------------------------
# Soru 1: Temel Ortalama
# --------------------------------------------------
print("--- Soru 1 ---")
q1 = df.groupby('Dep')['Maas'].mean()
print(q1)
print("\n")


# --------------------------------------------------
# Soru 2: Çoklu Kategori Gruplama
# --------------------------------------------------
print("--- Soru 2 ---")
q2 = df.groupby(['Dep', 'Dil'])['Proje_Sayisi'].sum()
print(q2)
print("\n")


# --------------------------------------------------
# Soru 3: Çoklu Metrik İnceleme
# --------------------------------------------------
print("--- Soru 3 ---")
q3 = df.groupby('Dep')['Maas'].agg(['min', 'max', 'mean'])
print(q3)
print("\n")


# --------------------------------------------------
# Soru 4: Sütuna Özel Toplulaştırma
# --------------------------------------------------
print("--- Soru 4 ---")
q4 = df.groupby('Dep').agg({
    'Maas': 'mean',
    'Tecrube': 'max',
    'Proje_Sayisi': 'sum'
})
print(q4)
print("\n")


# --------------------------------------------------
# Soru 5: Sütun İsimlerini Düzenleme (Named Aggregation)
# --------------------------------------------------
print("--- Soru 5 ---")
q5 = df.groupby('Dep').agg(
    Ortalama_Maas=('Maas', 'mean'),
    Kisi_Sayisi=('Calisan', 'count')
)
print(q5)
print("\n")


# --------------------------------------------------
# Soru 6: Kendi Mantığını Uygulama (Custom Lambda)
# --------------------------------------------------
print("--- Soru 6 ---")
q6 = df.groupby('Dep')['Tecrube'].agg(lambda x: x.max() - x.min())
print(q6)
print("\n")


# --------------------------------------------------
# Soru 7: Orijinal Satır Sayısını Koruma (transform)
# --------------------------------------------------
print("--- Soru 7 ---")
df['Dep_Ort_Maas'] = df.groupby('Dep')['Maas'].transform('mean')
df['Fark'] = df['Maas'] - df['Dep_Ort_Maas']
print(df[['Calisan', 'Dep', 'Maas', 'Dep_Ort_Maas', 'Fark']])
print("\n")


# --------------------------------------------------
# Soru 8: Koşula Göre Grup Eleme (filter)
# --------------------------------------------------
print("--- Soru 8 ---")
q8 = df.groupby('Dep').filter(lambda x: x['Proje_Sayisi'].sum() > 25)
print(q8)
print("\n")


# --------------------------------------------------
# Soru 9: 2 Boyutlu Rapor Oluşturma (pivot_table)
# --------------------------------------------------
print("--- Soru 9 ---")
q9 = pd.pivot_table(
    df,
    index='Dep',
    columns='Dil',
    values='Maas',
    aggfunc='sum',
    fill_value=0,
    margins=True
)
print(q9)
print("\n")


# --------------------------------------------------
# Soru 10: İndeks Düzleştirme (reset_index)
# --------------------------------------------------
print("--- Soru 10 ---")
q10 = df.groupby('Dep')['Tecrube'].mean().reset_index()
print(q10)