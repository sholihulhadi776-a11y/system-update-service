import requests
import re
import base64

# Sumber yang lebih banyak (Total 5 sumber)
sources = [
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config",
    "https://raw.githubusercontent.com/Pawdroid/Free-Servers/main/sub",
    "https://raw.githubusercontent.com/m-reza-k/v2ray-free/main/v2ray",
    "https://raw.githubusercontent.com/vfarid/v2ray-share/main/configs"
]

def decode_base64(data):
    try:
        missing_padding = len(data) % 4
        if missing_padding: data += '=' * (4 - missing_padding)
        return base64.b64decode(data).decode('utf-8', errors='ignore')
    except: return data

def scrape():
    print("[*] Memulai Liul-Hunter v2.5...")
    all_acc = []
    
    for url in sources:
        try:
            r = requests.get(url, timeout=10)
            text = decode_base64(r.text)
            # Ambil semua vless dan trojan
            found = re.findall(r'(vless://[^\s]+|trojan://[^\s]+)', text)
            all_acc.extend(found)
            print(f"[+] {url[:35]}... -> Dapat {len(found)}")
        except:
            print(f"[!] Skip sumber bermasalah")

    # Hapus duplikat dan simpan
    clean_acc = list(set(all_acc))
    with open("../my_accounts.txt", "w") as f:
        for a in clean_acc:
            f.write(a + "\n")
    
    print(f"\n[DONE] {len(clean_acc)} akun siap tempur di ~/my_accounts.txt")

if __name__ == "__main__":
    scrape()

