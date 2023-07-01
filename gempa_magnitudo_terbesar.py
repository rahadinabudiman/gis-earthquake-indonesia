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

# Menampilkan gempa dengan magnitudo paling besar dan provinsi tempat terjadinya
gempa_terbesar_index = df_gempa["mag"].idxmax()
gempa_terbesar_magnitudo = df_gempa.at[gempa_terbesar_index, "mag"]
gempa_terbesar_lat = df_gempa.at[gempa_terbesar_index, "latitude"]
gempa_terbesar_lon = df_gempa.at[gempa_terbesar_index, "longitude"]
gempa_terbesar_time = df_gempa.at[gempa_terbesar_index, "time"]

# Mencari provinsi tempat terjadinya gempa dengan menggunakan Haversine
distances_gempa_terbesar = df_provinsi.apply(
    lambda provinsi: haversine(
        gempa_terbesar_lat,
        gempa_terbesar_lon,
        provinsi["latitude"],
        provinsi["longitude"],
    ),
    axis=1,
)
nearest_provinsi_gempa_terbesar_index = distances_gempa_terbesar.idxmin()
provinsi_gempa_terbesar = df_provinsi.at[nearest_provinsi_gempa_terbesar_index, "name"]

print("Gempa dengan magnitudo paling besar:")
print("Magnitudo: {:.2f} SR".format(gempa_terbesar_magnitudo))
print("Provinsi: {}".format(provinsi_gempa_terbesar))
print("Latitude: {:.2f}".format(gempa_terbesar_lat))
print("Longitude: {:.2f}".format(gempa_terbesar_lon))
print("Waktu: {}".format(gempa_terbesar_time))
