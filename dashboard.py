import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# URL mentah dataset dari GitHub
url = 'https://raw.githubusercontent.com/khairunnas-khai/bike-sharing-dataset/main/day.csv'

# Mengunduh dan membaca dataset
df = pd.read_csv(url)


# Melihat informasi dasar dari dataset
df.info()
df.describe()
df.head()


# Menghapus kolom yang tidak relevan untuk analisis
df.drop(['instant', 'casual', 'registered'], axis=1, inplace=True)

# Mengonversi kolom `season` dan `weathersit` ke tipe kategori
df['season'] = df['season'].astype('category')
df['weathersit'] = df['weathersit'].astype('category')


import matplotlib.pyplot as plt # Importing the matplotlib library and assigning it to the alias "plt"

season_usage = df.groupby('season')['cnt'].mean()
season_usage.plot(kind='bar', title='Rata-rata Penyewaan Sepeda per Musim')
plt.xlabel('Season')
plt.ylabel('Rata-rata Penyewaan')
plt.show()

### Pertanyaan 1:

import matplotlib.pyplot as plt # Importing the matplotlib library and assigning it to the alias "plt"
import seaborn as sns # Importing the seaborn library and assigning it to the alias "sns"

plt.figure(figsize=(10, 5))
sns.lineplot(x=df['dteday'], y=df['cnt'])
plt.title('Pola Penyewaan Sepeda Harian')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewaan')
plt.show()

# Calculate correlations only for numerical columns by setting numeric_only=True
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Korelasi antar Variabel')
plt.show()

## Analisis Lanjutan (Opsional)

# Rata-rata Peminjaman Sepeda Berdasarkan Cuaca
weather_counts = df.groupby('weathersit')['cnt'].mean()

# Visualisasi
plt.figure(figsize=(8, 5))
sns.barplot(x=weather_counts.index, y=weather_counts.values)
plt.title('Rata-rata Peminjaman Sepeda Berdasarkan Cuaca')
plt.xlabel('Cuaca')
plt.ylabel('Rata-rata Peminjaman')
plt.show()

## Conclusion

##- Dari analisis pola harian, terlihat bahwa jumlah peminjaman sepeda menunjukkan tren musiman. Peminjaman lebih tinggi pada bulan-bulan musim panas dibandingkan musim dingin. Hal ini menunjukkan bahwa cuaca dan musim memainkan peran penting dalam meningkatkan aktivitas peminjaman sepeda.
##- Korelasi antar variabel menunjukkan bahwa variabel seperti suhu (temp) memiliki hubungan positif yang signifikan terhadap jumlah peminjaman sepeda. Sebaliknya, kondisi cuaca yang buruk (seperti hujan atau salju) cenderung menurunkan jumlah peminjaman.

##