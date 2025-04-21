import pandas as pd 
import os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

url = "https://docs.google.com/spreadsheets/d/17ru4XAU2NloE9Dfxr2PC1BVcsYkLLT5r7nPSsiOFlvQ/export?format=csv&gid=743838712"
df = pd.read_csv(url)

for kolom in ['Judul Paper', 'Tahun Terbit', 'Nama Penulis', 'Abstrak (langusung copas dari paper)', 'Kesimpulan (Langusung copas dari paper)']:
    df[kolom] = df[kolom].astype(str)

df['Tahun Terbit'] = df['Tahun Terbit'].str.replace('.0', '', regex=False)

def linear_search(df, key, value):
    return df[df[key].str.lower() == value.lower()]

def binary_search(df, key, value):
    df_sorted = df.sort_values(by=key, key=lambda x: x.str.lower()).reset_index(drop=True)
    low, high = 0, len(df_sorted) - 1
    value = value.lower()

    while low <= high:
        mid = (low + high) // 2
        mid_value = df_sorted.loc[mid, key].lower()

        if mid_value == value:
            return df_sorted.loc[[mid]]
        elif value < mid_value:
            high = mid - 1
        else:
            low = mid + 1

    return pd.DataFrame()

def tampilkan_hasil(hasil):
    if hasil.empty:
        print("Data tidak ditemukan, coba lagi.")
    else:
        for i, (index, row) in enumerate(hasil.iterrows(), start=1):
            print(f"Judul     : {row['Judul Paper']}")
            print(f"Tahun     : {row['Tahun Terbit']}")
            print(f"Penulis   : {row['Nama Penulis']}")
            print(f"Abstract  : {row['Abstrak (langusung copas dari paper)'][:200]}...") 
            print(f"Kesimpulan: {row['Kesimpulan (Langusung copas dari paper)'][:200]}...")
            print("-" * 50)

while True:
    clear_screen()  

    print("Menu:")
    print("1. Cari berdasarkan Judul Paper")
    print("2. Cari berdasarkan Nama Penulis")
    print("3. Cari berdasarkan Tahun Terbit")
    print("4. Keluar")
    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        kolom = "Judul Paper"
        nilai = input("Masukkan Judul Paper: ")
    elif pilihan == "2":
        kolom = "Nama Penulis"
        nilai = input("Masukkan Nama Penulis: ")
    elif pilihan == "3":
        kolom = "Tahun Terbit"
        nilai = input("Masukkan Tahun Terbit: ")
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Menu tidak ada, coba lagi.") 
        continue

    print("\n=== Linear Search ===")
    tampilkan_hasil(linear_search(df, kolom, nilai))

    print("\n=== Binary Search ===")
    tampilkan_hasil(binary_search(df, kolom, nilai))

    ulang = input("\nKembali ke menu awal? (y/n): ").lower()
    if ulang == "n":
        print("Program selesai.")
        break
    elif ulang != "y":
        print("Input tidak dikenali, program akan keluar.")
        break
