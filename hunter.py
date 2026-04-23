import requests
import re
import base64

# Sumber yang lebih gacor dan update
sources = [
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config",
    "https://raw.githubusercontent.com/Pawdroid/Free-Servers/main/sub"
]

def decode_base64(data):
    try:
        # Tambahkan padding jika kurang agar tidak error saat decode
        missing_padding = len(data) % 4
        if missing_padding:
            data += '=' * (4 - missing_padding)
        return base64.b64decode(data).decode('utf-8')
    except:
        return data

def scrape_accounts():
    print("[*] Melakukan Brute-Force Scrape & Decoding...")
    all_accounts = []
    
    for url in sources:
        try:
            r = requests.get(url, timeout=15)
            # Coba decode dulu karena biasanya isinya base64 mentah
            decoded_text = decode_base64(r.text)
            
            # Cari trojan dan vless
            found = re.findall(r'(trojan://[^\s]+|vless://[^\s]+)', decoded_text)
            all_accounts.extend(found)
            print(f"[+] Berhasil membongkar {len(found)} akun dari: {url[:30]}...")
        except Exception as e:
            print(f"[!] Gagal di sumber ini.")

    # Simpan ke file
    with open("../my_accounts.txt", "w") as f:
        for acc in list(set(all_accounts)): # set() untuk hapus duplikat
            f.write(acc + "\n")
    
    print(f"\n[DONE] TOTAL: {len(all_accounts)} akun siap tempur!")

if __name__ == "__main__":
    scrape_accounts()
import requests
import re

# Daftar sumber akun gratisan yang update setiap jam
sources = [
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt"
]

def scrape_accounts():
    print("[*] Mencari akun Trojan/VLESS di awan...")
    all_accounts = []
    
    for url in sources:
        try:
            response = requests.get(url, timeout=10)
            # Mencari pola trojan:// atau vless://
            found = re.findall(r'(trojan://[^\s]+|vless://[^\s]+)', response.text)
            all_accounts.extend(found)
            print(f"[+] Berhasil mengambil {len(found)} akun dari sumber.")
        except:
            print(f"[!] Gagal akses sumber: {url}")

    # Simpan hasil ke file my_accounts.txt di folder home
    with open("../my_accounts.txt", "w") as f:
        for acc in all_accounts:
            f.write(acc + "\n")
    
    print(f"\n[DONE] {len(all_accounts)} akun disimpan di ~/my_accounts.txt")

if __name__ == "__main__":
    scrape_accounts()

