import pandas as pd
import numpy as np

# Membaca data provinsi dan data gempa dari file CSV
df_provinsi = pd.read_csv("provinsi.csv", nrows=34)
total_provinsi = len(df_provinsi)
df_gempa = pd.read_csv("Gempa.csv")

# Menampilkan rata-rata gempa yang terjadi di Indonesia
rata2_sr = df_gempa["mag"].mean()

print("Rata-rata magnitudo gempa di Indonesia: {:.2f} SR".format(rata2_sr))
