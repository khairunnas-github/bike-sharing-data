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

# Exploratory Data Analysis
season_usage = df.groupby('season')['cnt'].mean()
weather_counts = df.groupby('weathersit')['cnt'].mean()

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

# Visualisasi: Jumlah Penyewaan per Musim
st.subheader("Rata-rata Penyewaan Sepeda per Musim")
season_usage = df.groupby('season')['cnt'].mean()
fig1, ax1 = plt.subplots()
season_usage.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title("Rata-rata Penyewaan Sepeda per Musim")
ax1.set_xlabel("Musim")
ax1.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig1)

# Visualisasi: Penyewaan Berdasarkan Cuaca
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
weather_counts = df.groupby('weathersit')['cnt'].mean()
fig2, ax2 = plt.subplots()
weather_counts.plot(kind='bar', ax=ax2, color='orange')
ax2.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
ax2.set_xlabel("Cuaca")
ax2.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig2)

# Opsi filter data berdasarkan Musim
st.subheader("Filter Data Berdasarkan Musim")
season = st.selectbox("Pilih Musim", df['season'].unique())
filtered_data = df[df['season'] == season]
st.write(f"Data untuk Musim: {season}")
st.dataframe(filtered_data)

# Filter berdasarkan cuaca
st.subheader("Filter Data Berdasarkan Cuaca")
weather = st.selectbox("Pilih Cuaca", df['weathersit'].unique())
filtered_weather = df[df['weathersit'] == weather]
st.write(f"Data untuk Cuaca: {weather}")
st.dataframe(filtered_weather)

# Menampilkan Deskripsi Statistik
st.subheader("Deskripsi Statistik")
st.write(df.describe())