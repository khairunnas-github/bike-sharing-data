import streamlit as st
import pandas as pd
import plotly.express as px

# Fungsi untuk memuat dataset dari GitHub
@st.cache_data
def load_data():
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
st.title("Dashboard Analisis Data Rentals")
st.write("Dashboard ini menampilkan analisis interaktif berdasarkan dataset rental sepeda dari GitHub.")

# Visualisasi 1: Distribusi Total Rentals
st.subheader("Distribusi Total Rentals")
fig1 = px.histogram(
    filtered_data,
    x='cnt',
    nbins=30,
    title="Distribusi Total Rentals",
    labels={'cnt': 'Total Rentals'},
    color_discrete_sequence=['blue']
)
st.plotly_chart(fig1)

# Visualisasi 2: Hubungan Temperatur dengan Total Rentals
st.subheader("Hubungan Temperatur dengan Total Rentals")
fig2 = px.scatter(
    filtered_data,
    x='temp',
    y='cnt',
    color='season',
    title="Hubungan Temperatur dan Total Rentals",
    labels={'temp': 'Temperatur', 'cnt': 'Total Rentals', 'season': 'Musim'},
    color_discrete_sequence=px.colors.qualitative.Set1
)
st.plotly_chart(fig2)

# Visualisasi 3: Tren Rentals Harian
st.subheader("Tren Rentals Harian")
fig3 = px.line(
    filtered_data.sort_values('date'),
    x='date',
    y='cnt',
    title="Tren Total Rentals Harian",
    labels={'date': 'Tanggal', 'cnt': 'Total Rentals'},
    line_shape='spline'
)
st.plotly_chart(fig3)

# Tampilkan Data Filtered
st.subheader("Data yang Difilter")
st.write("Berikut adalah data yang telah difilter berdasarkan pilihan:")
st.dataframe(filtered_data)
