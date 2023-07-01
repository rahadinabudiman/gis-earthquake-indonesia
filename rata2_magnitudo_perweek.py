import pandas as pd

# Membaca data provinsi dan data gempa dari file CSV
df_provinsi = pd.read_csv("provinsi.csv", nrows=34)
df_gempa = pd.read_csv("Gempa.csv")

# Mengubah kolom 'time' menjadi tipe data datetime
df_gempa["time"] = pd.to_datetime(df_gempa["time"])

# Menghitung rata-rata gempa per minggu
df_gempa["week"] = df_gempa["time"].apply(lambda x: x.isocalendar()[1])
rata2_gempa_per_minggu = df_gempa.groupby("week")["mag"].mean()

print("Rata-rata gempa per minggu:")
print(rata2_gempa_per_minggu)
