import requests
import json
import pandas as pd

def scrape_kopi_jakarta():
    print("Mulai mengambil data ASLI kedai kopi di Jakarta...")
    
    url = "https://nominatim.openstreetmap.org/search"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    # Kita ubah target ke wilayah Jakarta sesuai permintaan!
    q = "cafe in jakarta"
    print(f"Mencari kata kunci: '{q}'...\n")
    
    params = {
        'q': q,
        'format': 'json',
        'limit': 50,
        'addressdetails': 1,
        'extratags': 1 
    }
    
    semua_data = []
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        print(f" -> Mendapatkan {len(data)} baris data.\n")
        
        for item in data:
            nama = item.get('name', '')
            if not nama:
                continue
            
            # --- 1. SETTING ALAMAT ---
            address = item.get('address', {})
            jalan = address.get('road', '')
            kecamatan = address.get('subdistrict', address.get('village', ''))
            kota = address.get('city', 'Jakarta')
            kodepos = address.get('postcode', '')
            
            alamat_lengkap = f"{jalan}, {kecamatan}, {kota} {kodepos}".replace(" ,", ",").strip(", ")
            if len(alamat_lengkap) < 10:
                alamat_lengkap = item.get('display_name', 'Alamat detail tidak tercatat')
                
            # --- 2. BUG FIX: MENGATASI EXTRATAGS KOSONG ---
            extratags = item.get('extratags')
            if extratags is None:
                extratags = {}
            
            no_telp = extratags.get('phone', extratags.get('contact:phone', extratags.get('contact:whatsapp', '')))
            
            if not no_telp:
                # Mengubah teks supaya tidak salah paham seolah cafenya tutup!
                no_telp = "Nomor Tidak Terdaftar di Maps (Cek IG/Gofood)"
                
            semua_data.append({
                'Nama Kedai': nama,
                'Alamat Lengkap': alamat_lengkap,
                'Nomor Handphone': no_telp
            })
            
    except Exception as e:
        print(f"Error: {e}")
        
    if len(semua_data) > 0:
        print(f"Berhasil menyusun {len(semua_data)} data dengan detail yang lengkap.")
        print("Menyimpan ke Format Excel / CSV...")
        df = pd.DataFrame(semua_data)
        
        # Nama file kita sesuaikan jadi Jakarta
        filename = "Data_Asli_Kopi_Jakarta_Portfolio.csv"
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"\nSELESAI! File '{filename}' sudah berisi Nomor HP dan Alamat Lengkap!")
    else:
        print("Gagal mengambil data.")

if __name__ == "__main__":
    scrape_kopi_jakarta()
