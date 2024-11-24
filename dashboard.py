import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Bike Sharing Analysis Dashboard")
st.markdown("""
Selamat datang di dashboard analisis data Bike Sharing!  
Dashboard ini membantu menjawab pertanyaan bisnis terkait pola peminjaman sepeda.
""")

# Fungsi Memuat Data dari GitHub
@st.cache_data
def load_data_from_github(url):
    try:
        data = pd.read_csv(url)
        data['dteday'] = pd.to_datetime(data['dteday'], errors='coerce')
        return data
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat data: {e}")
        return pd.DataFrame()

# URL Dataset GitHub
github_url = "https://raw.githubusercontent.com/khairunnas-khai/bike-sharing-dataset/main/day.csv"

# Memuat Dataset
data = load_data_from_github(github_url)

# Validasi Dataset
if data.empty:
    st.stop()

# Sidebar Filters
st.sidebar.header("Filters")
date_filter = st.sidebar.date_input(
    "Pilih Rentang Tanggal:",
    value=(data['dteday'].min(), data['dteday'].max())
)
weather_filter = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca:",
    options=data['weathersit'].unique(),
    default=data['weathersit'].unique()
)

# Filter Data
data_filtered = data[
    (data['dteday'] >= pd.Timestamp(date_filter[0])) &
    (data['dteday'] <= pd.Timestamp(date_filter[1])) &
    (data['weathersit'].isin(weather_filter))
]

# Menampilkan Data
st.subheader("Data yang Difilter")
st.write(data_filtered.head())

# Visualisasi 1: Pengaruh Cuaca terhadap Rentals
st.subheader("Pengaruh Cuaca terhadap Rentals")
if not data_filtered.empty:
    weather_rentals = data_filtered.groupby('weathersit')['cnt'].mean()

    fig, ax = plt.subplots()
    weather_rentals.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title("Rata-rata Rentals Berdasarkan Kondisi Cuaca")
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Rata-rata Rentals")
    st.pyplot(fig)
else:
    st.info("Tidak ada data yang sesuai dengan filter cuaca dan tanggal yang dipilih.")

# Visualisasi 2: Pola Musiman Rentals
st.subheader("Pola Musiman Rentals")
if not data_filtered.empty:
    data_filtered['month'] = data_filtered['dteday'].dt.month
    monthly_rentals = data_filtered.groupby('month')['cnt'].sum()

    fig, ax = plt.subplots()
    monthly_rentals.plot(kind='line', marker='o', color='green', ax=ax)
    ax.set_title("Total Rentals per Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Total Rentals")
    ax.grid(True)
    st.pyplot(fig)
else:
    st.info("Tidak ada data yang sesuai dengan filter bulan dan tanggal yang dipilih.")

# Insight dan Visualisasi
st.subheader("Insight dan Kesimpulan")
st.markdown("""
### Insight:
1. Kondisi cuaca memengaruhi jumlah peminjaman sepeda, dengan cuaca baik meningkatkan jumlah peminjaman.
2. Musim panas menunjukkan peningkatan peminjaman sepeda.
3. Korelasi positif ditemukan antara suhu dan jumlah peminjaman sepeda.
""")

# Footer
st.markdown("""
Dashboard ini dibuat menggunakan **Streamlit**.  
Dataset diunduh langsung dari **GitHub** untuk memastikan selalu menggunakan data terbaru.
""")
