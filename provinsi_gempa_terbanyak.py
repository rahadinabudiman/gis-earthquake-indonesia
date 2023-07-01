import pandas as pd
import numpy as np


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1_rad = np.radians(lat1)
    lon1_rad = np.radians(lon1)
    lat2_rad = np.radians(lat2)
    lon2_rad = np.radians(lon2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2) ** 2
    )
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c

    return distance


# Membaca data provinsi dan data gempa dari file CSV
df_provinsi = pd.read_csv("provinsi.csv", nrows=34)
df_gempa = pd.read_csv("Gempa.csv")

# Inisialisasi kolom 'Jumlah Gempa' pada dataframe provinsi
df_provinsi["Jumlah Gempa"] = 0
df_provinsi["Total Magnitudo"] = 0

# Mengiterasi setiap gempa
for index, row in df_gempa.iterrows():
    gempa_lat = row["latitude"]
    gempa_lon = row["longitude"]
    gempa_magnitude = row["mag"]

    # Menghitung jarak antara gempa dan setiap provinsi menggunakan Haversine
    distances = df_provinsi.apply(
        lambda provinsi: haversine(
            gempa_lat,
            gempa_lon,
            provinsi["latitude"],
            provinsi["longitude"],
        ),
        axis=1,
    )

    # Mencari indeks provinsi dengan jarak terdekat
    nearest_provinsi_index = distances.idxmin()

    # Menambahkan jumlah gempa pada provinsi terdekat
    df_provinsi.at[nearest_provinsi_index, "Jumlah Gempa"] += 1

    # Menambahkan magnitudo gempa pada provinsi terdekat
    df_provinsi.at[nearest_provinsi_index, "Total Magnitudo"] += gempa_magnitude

# Mengurutkan provinsi berdasarkan jumlah gempa secara menurun
df_provinsi_terbanyak = df_provinsi.sort_values(
    by="Jumlah Gempa", ascending=False
).head(1)

# Menghitung rata-rata magnitudo gempa di provinsi terbanyak
provinsi_terbanyak_index = df_provinsi_terbanyak.index[0]
total_gempa_terbanyak = df_provinsi_terbanyak.at[
    provinsi_terbanyak_index, "Jumlah Gempa"
]
total_magnitudo_terbanyak = df_provinsi_terbanyak.at[
    provinsi_terbanyak_index, "Total Magnitudo"
]
rata_rata_magnitudo = total_magnitudo_terbanyak / total_gempa_terbanyak

# Menampilkan provinsi dengan jumlah gempa terbanyak dan rata-rata magnitudo gempa
print("Provinsi dengan jumlah gempa terbanyak:")
print(df_provinsi_terbanyak[["name", "Jumlah Gempa"]])
print(
    "Rata-rata magnitudo gempa di provinsi tersebut: {:.2f} SR".format(
        rata_rata_magnitudo
    )
)
