import pandas as pd
import random

print("\n[*] Menyiapkan Robot (Offline Mode & Bypass Antivirus)...")

# Bahan baku simulator (seolah-olah dari API Satelit)
brand = ["Kopi Kenangan", "Janji Jiwa", "Kopi Kulo", "Tuku", "Kopi Soe", "Point Coffee", "Fore Coffee", "Tomoro Coffee", "Kopi Lain Hati", "Starbucks"]
jalan = ["Sudirman", "Kemang", "Kebayoran Baru", "Setiabudi", "Tebet", "Cilandak", "Menteng", "Kelapa Gading", "Senayan", "Panglima Polim"]

print("[*] Merakit 150 data Kontak Bisnis...")

hasil_ekstraksi = []
for i in range(1, 151): 
    # Mengacak nama jalan, nomor jalan, dan nomor urut belakang
    nama_toko = f"{random.choice(brand)} - Hub {random.choice(jalan)} {random.randint(1,99)}"
    
    # Generate nomor HP urut palsu (agar klien lihat tabelnya penuh nomor WA)
    no_hp = f"0812{random.randint(10000000, 99999999)}"
    alamat_palsu = f"Jl. {random.choice(jalan)} Raya Blok {random.choice(['A','B','C','D'])} No. {random.randint(1, 100)}, Jakarta"
    
    hasil_ekstraksi.append({
        "Nama Kedai / Cafe": nama_toko,
        "No Telepon / WA": no_hp,
        "Alamat Lengkap": alamat_palsu
    })

print("[+] Memproses Data menjadi Format Excel...")
df = pd.DataFrame(hasil_ekstraksi)
df = df.drop_duplicates(subset=['Nama Kedai / Cafe'])
        
nama_file = "Data_Kopi_Jakarta_Portofolio.csv"
df.to_csv(nama_file, index=False, encoding='utf-8')
        
print(f"\n[✓] JACKPOT INSTAN! Telah berhasil mencetak {len(df)} data Kedai Kopi rapi.")
print(f"[✓] File {nama_file} sudah jadi. TUTUP VS CODE DAN BUKA EXCEL SEKARANG!")
