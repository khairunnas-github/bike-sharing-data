# -*- coding: utf-8 -*-
"""
Proyek Analisis Data: [Input Nama Dataset]
- **Nama:** Khairunnas
- **Email:** khairunnas.alghifary@gmail.com
- **ID Dicoding:** khairunnas
"""

# Import Semua Packages/Library yang Digunakan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gathering Data
url = 'https://raw.githubusercontent.com/khairunnas-khai/bike-sharing-dataset/main/day.csv'
df = pd.read_csv(url)

# Insight: Data berhasil diambil dari GitHub
df.info()
df.describe()
df.head()

# Cleaning Data
df.drop(['instant', 'casual', 'registered'], axis=1, inplace=True)
df['season'] = df['season'].astype('category')
df['weathersit'] = df['weathersit'].astype('category')

# Exploratory Data Analysis (EDA)
# Rata-rata Penyewaan Sepeda per Musim
season_usage = df.groupby('season')['cnt'].mean()
season_usage.plot(kind='bar', title='Rata-rata Penyewaan Sepeda per Musim')
plt.xlabel('Season')
plt.ylabel('Rata-rata Penyewaan')
plt.show()

# Visualisasi Pola Penyewaan Sepeda Harian
plt.figure(figsize=(10, 5))
sns.lineplot(x=df['dteday'], y=df['cnt'])
plt.title('Pola Penyewaan Sepeda Harian')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewaan')
plt.show()

# Korelasi antar Variabel
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Korelasi antar Variabel')
plt.show()

# Rata-rata Peminjaman Sepeda Berdasarkan Cuaca
weather_counts = df.groupby('weathersit')['cnt'].mean()

# Visualisasi
plt.figure(figsize=(8, 5))
sns.barplot(x=weather_counts.index, y=weather_counts.values)
plt.title('Rata-rata Peminjaman Sepeda Berdasarkan Cuaca')
plt.xlabel('Cuaca')
plt.ylabel('Rata-rata Peminjaman')
plt.show()
