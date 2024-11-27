import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk memuat dataset
@st.cache_data
def load_data():
    # URL GitHub Dataset
    github_url = "https://raw.githubusercontent.com/khairunnas-khai/bike-sharing-dataset/main/day.csv"
    data = pd.read_csv(github_url)
    
    # Rename kolom 'dteday' menjadi 'date' dan ubah ke format datetime
    data.rename(columns={'dteday': 'date'}, inplace=True)
    data['date'] = pd.to_datetime(data['date'])
    
    # Mapping kolom kategorikal
    weather_labels = {1: 'Cerah', 2: 'Berawan', 3: 'Hujan', 4: 'Sangat Hujan'}
    season_labels = {1: 'Musim Dingin', 2: 'Musim Semi', 3: 'Musim Panas', 4: 'Musim Gugur'}
    data['weathersit'] = data['weathersit'].map(weather_labels)
    data['season'] = data['season'].map(season_labels)
    
    return data

# Load data
data = load_data()

# Sidebar untuk Filter
st.sidebar.header("Filter Data")
season_filter = st.sidebar.multiselect(
    "Pilih Musim (Season):",
    options=data['season'].unique(),
    default=data['season'].unique()
)
weather_filter = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca (Weather Situation):",
    options=data['weathersit'].unique(),
    default=data['weathersit'].unique()
)
date_filter = st.sidebar.date_input(
    "Rentang Tanggal:",
    value=(data['date'].min(), data['date'].max())
)

# Filter data berdasarkan input pengguna
filtered_data = data[
    (data['season'].isin(season_filter)) &
    (data['weathersit'].isin(weather_filter)) &
    (data['date'] >= pd.Timestamp(date_filter[0])) &
    (data['date'] <= pd.Timestamp(date_filter[1]))
]

# Judul Utama
st.title("Dashboard Analisis Bike Sharing")
st.markdown("""
Dashboard ini dirancang untuk menganalisis data peminjaman sepeda berdasarkan berbagai faktor seperti cuaca, musim, dan pola musiman. Data bersumber dari [GitHub Repository](https://github.com/khairunnas-khai/bike-sharing-dataset).
""")

# Visualisasi 1: Distribusi Total Rentals
st.subheader("Distribusi Jumlah Peminjaman Sepeda")
plt.figure(figsize=(10, 5))
sns.histplot(filtered_data['cnt'], kde=True, color='blue', bins=30)
plt.title("Distribusi Total Peminjaman Sepeda")
plt.xlabel("Jumlah Peminjaman")
plt.ylabel("Frekuensi")
st.pyplot(plt)

# Visualisasi 2: Pengaruh Cuaca terhadap Rentals
st.subheader("Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda")
weather_rentals = filtered_data.groupby('weathersit')['cnt'].mean()
plt.figure(figsize=(8, 5))
weather_rentals.plot(kind='bar', color=['lightblue', 'lightgreen', 'yellow', 'gray'])
plt.title("Rata-rata Peminjaman Berdasarkan Kondisi Cuaca")
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Rata-rata Jumlah Peminjaman")
plt.xticks(rotation=0)
st.pyplot(plt)

# Visualisasi 3: Pola Musiman
st.subheader("Pola Musiman dalam Peminjaman Sepeda")
monthly_rentals = filtered_data.groupby(filtered_data['date'].dt.month)['cnt'].sum()
plt.figure(figsize=(10, 5))
monthly_rentals.plot(kind='line', marker='o', color='green')
plt.title("Total Peminjaman Sepeda per Bulan")
plt.xlabel("Bulan")
plt.ylabel("Total Jumlah Peminjaman")
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
st.pyplot(plt)

# Menampilkan Data Filtered
st.subheader("Data yang Difilter")
st.write("Berikut adalah data yang difilter berdasarkan pilihan Anda:")
st.dataframe(filtered_data)
