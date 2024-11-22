import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
url = "https://raw.githubusercontent.com/khairunnas-khai/bike-sharing-dataset/main/day.csv"
df = pd.read_csv(url)

# Data Cleaning
df.drop(['instant', 'casual', 'registered'], axis=1, inplace=True)
df['season'] = df['season'].astype('category')
df['weathersit'] = df['weathersit'].astype('category')

# Menambahkan kolom untuk analisis tambahan
df['dteday'] = pd.to_datetime(df['dteday'])
df['month'] = df['dteday'].dt.month
df['year'] = df['dteday'].dt.year

# Save cleaned data for dashboard
df.to_csv("cleaned_bike_data.csv", index=False)

# Load cleaned data from the file
df = pd.read_csv("cleaned_bike_data.csv")

# Streamlit App
st.title("Dashboard Penyewaan Sepeda")
st.write("Analisis Data Penyewaan Sepeda Harian Berdasarkan Cuaca dan Musim")

# Menampilkan Dataframe yang telah dibersihkan
st.subheader("Data Penyewaan Sepeda")
st.dataframe(df.head())

# EDA Univariate: Distribusi Penyewaan
st.subheader("Distribusi Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots()
sns.histplot(df['cnt'], bins=20, kde=True, ax=ax, color='green')
ax.set_title("Distribusi Penyewaan Sepeda")
ax.set_xlabel("Jumlah Penyewaan")
st.pyplot(fig)

# EDA Bivariate: Hubungan Suhu dan Penyewaan
st.subheader("Hubungan Suhu dan Jumlah Penyewaan")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='temp', y='cnt', ax=ax, color='blue')
ax.set_title("Hubungan Suhu dan Jumlah Penyewaan")
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Visualisasi: Jumlah Penyewaan per Musim
st.subheader("Rata-rata Penyewaan Sepeda per Musim")
season_usage = df.groupby('season')['cnt'].mean()
fig1, ax1 = plt.subplots()
season_usage.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title("Rata-rata Penyewaan Sepeda per Musim")
ax1.set_xlabel("Musim")
ax1.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig1)

# Visualisasi: Rata-rata Penyewaan Berdasarkan Cuaca
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
weather_counts = df.groupby('weathersit')['cnt'].mean()
fig2, ax2 = plt.subplots()
weather_counts.plot(kind='bar', ax=ax2, color='orange')
ax2.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
ax2.set_xlabel("Cuaca")
ax2.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig2)

# Visualisasi: Tren Penyewaan Sepanjang Tahun
st.subheader("Tren Penyewaan Sepanjang Tahun")
monthly_usage = df.groupby('month')['cnt'].mean()
fig3, ax3 = plt.subplots()
monthly_usage.plot(ax=ax3, marker='o', color='purple')
ax3.set_title("Rata-rata Penyewaan Sepeda Per Bulan")
ax3.set_xlabel("Bulan")
ax3.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig3)

# Filter Data Berdasarkan Musim
st.subheader("Filter Data Berdasarkan Musim")
season = st.selectbox("Pilih Musim", df['season'].unique())
filtered_data = df[df['season'] == season]
st.write(f"Data untuk Musim: {season}")
st.dataframe(filtered_data)

# Filter Data Berdasarkan Cuaca
st.subheader("Filter Data Berdasarkan Cuaca")
weather = st.selectbox("Pilih Cuaca", df['weathersit'].unique())
filtered_weather = df[df['weathersit'] == weather]
st.write(f"Data untuk Cuaca: {weather}")
st.dataframe(filtered_weather)

# Deskripsi Statistik
st.subheader("Deskripsi Statistik")
st.write(df.describe())
