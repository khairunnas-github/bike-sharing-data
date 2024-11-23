import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Bike Sharing Analysis Dashboard")
st.markdown("""
Selamat datang di dashboard analisis data Bike Sharing!  
Dashboard ini menampilkan hasil analisis terkait pola peminjaman sepeda berdasarkan cuaca dan musim.
""")

# Load Dataset from URL
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/khairunnas-khai/bike-sharing-dataset/main/day.csv"
    data = pd.read_csv(url)
    # Konversi kolom 'dteday' ke format datetime
    data['dteday'] = pd.to_datetime(data['dteday'])
    return data

data = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
weather_filter = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca:",
    options=data['weathersit'].unique(),
    default=data['weathersit'].unique()
)
month_filter = st.sidebar.slider(
    "Pilih Rentang Bulan:",
    min_value=1,
    max_value=12,
    value=(1, 12)
)

# Filter Data
filtered_data = data[
    (data['weathersit'].isin(weather_filter)) &
    (data['dteday'].dt.month.between(*month_filter))
]

# Visualization 1: Pengaruh Cuaca terhadap Rentals
st.subheader("Pengaruh Cuaca terhadap Rentals")
weather_rentals = filtered_data.groupby('weathersit')['cnt'].mean()

fig, ax = plt.subplots()
weather_rentals.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title("Rata-rata Rentals Berdasarkan Cuaca")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Rentals")
st.pyplot(fig)

# Visualization 2: Pola Musiman Rentals
st.subheader("Pola Musiman Rentals")
filtered_data['month'] = filtered_data['dteday'].dt.month
monthly_rentals = filtered_data.groupby('month')['cnt'].sum()

fig, ax = plt.subplots()
monthly_rentals.plot(kind='line', marker='o', color='green', ax=ax)
ax.set_title("Total Rentals per Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Rentals")
ax.grid(True)
st.pyplot(fig)

# Insight
st.markdown("""
### Kesimpulan:
- Cuaca buruk cenderung menurunkan jumlah peminjaman sepeda.
- Musim panas (bulan 6-8) menunjukkan peningkatan jumlah peminjaman yang signifikan.
""")
