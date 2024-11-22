# -*- coding: utf-8 -*-
##Proyek Analisis Data.ipynb

# Proyek Analisis Data: [Input Nama Dataset]
# **Nama:** Khairunnas
# **Email:** khairunnas.alghifary@gmail.com
# **ID Dicoding:** khairunnas

## Menentukan Pertanyaan Bisnis
#- Apa faktor-faktor yang mempengaruhi jumlah peminjaman sepeda di berbagai bulan sepanjang tahun?
#- Bagaimana perbandingan peminjaman sepeda antara pengguna terdaftar dan pengguna tidak terdaftar?

## Import Semua Packages/Library yang Digunakan"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # Importing the seaborn library and assigning it to the alias "sns"

## Data Wrangling

### Gathering Data

# URL mentah dataset dari GitHub
url = 'https://raw.githubusercontent.com/khairunnas-khai/bike-sharing-dataset/main/day.csv'

# Mengunduh dan membaca dataset
df = pd.read_csv(url)

### Insight:
#- Data berhasil diambil dari sumber GitHub menggunakan URL mentah, memastikan dataset yang digunakan adalah versi terbaru dan sesuai dengan kebutuhan analisis.
#- Dataset mencakup informasi terkait peminjaman sepeda harian, faktor cuaca, dan kondisi musim, yang relevan untuk menjawab pertanyaan bisnis.
#- Format data adalah CSV, sehingga mudah dibaca dan diproses menggunakan pustaka Python seperti pandas.

### Assessing Data

# Melihat informasi dasar dari dataset
df.info()
df.describe()
df.head()

###"""**Insight:**
#- Dataset terdiri dari 16 kolom dan lebih dari 700 baris data, dengan tipe data yang beragam seperti numerik dan kategori.
#- Tidak ada nilai missing dalam dataset, sehingga data sudah lengkap dan siap untuk dianalisis.
#- Kolom seperti instant, dteday, dan yr merupakan data identifikasi dan tanggal yang tidak akan langsung digunakan dalam analisis prediktif.
#- Variabel seperti temp, hum, dan windspeed menunjukkan variasi yang sesuai dengan data cuaca.

### Cleaning Data

# Menghapus kolom yang tidak relevan untuk analisis
df.drop(['instant', 'casual', 'registered'], axis=1, inplace=True)

# Mengonversi kolom `season` dan `weathersit` ke tipe kategori
df['season'] = df['season'].astype('category')
df['weathersit'] = df['weathersit'].astype('category')

###"""**Insight:**
#- Kolom instant, casual, dan registered dihapus karena tidak relevan untuk analisis keseluruhan jumlah peminjaman sepeda (cnt).
#- Kolom season dan weathersit diubah menjadi tipe data kategori untuk mempermudah analisis dan visualisasi.
#- Tidak ditemukan nilai missing dalam dataset, sehingga tidak perlu penanganan tambahan terkait data yang hilang.

## Exploratory Data Analysis (EDA)

### Explore ...

season_usage = df.groupby('season')['cnt'].mean()
season_usage.plot(kind='bar', title='Rata-rata Penyewaan Sepeda per Musim')
plt.xlabel('Season')
plt.ylabel('Rata-rata Penyewaan')
plt.show()


## Visualization & Explanatory Analysis

### Pertanyaan 1:

plt.figure(figsize=(10, 5))
sns.lineplot(x=df['dteday'], y=df['cnt'])
plt.title('Pola Penyewaan Sepeda Harian')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewaan')
plt.show()

### Pertanyaan 2:

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
#- Dari analisis pola harian, terlihat bahwa jumlah peminjaman sepeda menunjukkan tren musiman. Peminjaman lebih tinggi pada bulan-bulan musim panas dibandingkan musim dingin. Hal ini menunjukkan bahwa cuaca dan musim memainkan peran penting dalam meningkatkan aktivitas peminjaman sepeda.
#- Korelasi antar variabel menunjukkan bahwa variabel seperti suhu (temp) memiliki hubungan positif yang signifikan terhadap jumlah peminjaman sepeda. Sebaliknya, kondisi cuaca yang buruk (seperti hujan atau salju) cenderung menurunkan jumlah peminjaman.
