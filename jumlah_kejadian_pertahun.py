import pandas as pd

# Membaca data provinsi dan data gempa dari file CSV
df_provinsi = pd.read_csv("provinsi.csv", nrows=34)
df_gempa = pd.read_csv("Gempa.csv")

df_gempa["time"] = pd.to_datetime(df_gempa["time"]).dt.tz_localize(None)

# Filter data gempa berdasarkan rentang waktu
start_date = pd.to_datetime("2018-01-01").tz_localize(None)
end_date = pd.to_datetime("2023-12-31").tz_localize(None)
df_gempa_filtered = df_gempa.loc[
    (df_gempa["time"] >= start_date) & (df_gempa["time"] <= end_date)
]

# Menghitung jumlah kejadian gempa per tahun
gempa_per_tahun = df_gempa_filtered["time"].dt.year.value_counts()

# Menampilkan jumlah kejadian gempa per tahun
print("Jumlah kejadian gempa per tahun:")
print(gempa_per_tahun)
print()

# Menampilkan rata-rata gempa per tahun
print("Rata-rata gempa per tahun:")
print(gempa_per_tahun.mean())
