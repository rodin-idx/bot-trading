import pandas as pd

# Warna terminal
WHITE = "\033[97m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Load file CSV
df = pd.read_csv("kombinasi_trading_1320.csv")

# Input user
input_a = input("Masukkan urutan warna EMA/SMA (pisahkan dengan koma, contoh: hijau,biru,merah,oranye,ungu): ")
input_b = int(input("Masukkan RSI (angka): "))

# Format string input
formatted_a = str([w.strip() for w in input_a.split(',')])

# Filter data
hasil = df[(df['Urutan_EMA_SMA'] == formatted_a) & (df['RSI'] == input_b)]

# Tampilkan hasil
if not hasil.empty:
    prediksi = hasil.iloc[0]['Prediksi']
    akurasi = int(hasil.iloc[0]['Akurasi (%)'])

    # Warna untuk prediksi
    pred_color = GREEN if prediksi.lower() == "buy" else RED

    # Warna untuk akurasi
    acc_color = GREEN if akurasi > 50 else RED

    # Tampilkan
    print(f"\n{WHITE}Prediksi: {pred_color}{prediksi}{RESET}")
    print(f"{WHITE}Akurasi: {acc_color}{akurasi}%{RESET}")
else:
    print(f"\n{RED}Data tidak ditemukan.{RESET}")
