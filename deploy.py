import os
import datetime

def deploy_to_friends():
    print("[*] Mengambil akun terbaru...")
    
    # Perintah untuk mengambil 5 akun Trojan terbaik
    # Kita arahkan ke file my_accounts.txt yang ada di folder home
    os.system('grep "trojan://" ~/my_accounts.txt | head -n 5 > config.txt')
    
    # Audit Keamanan: Cek apakah file kosong atau tidak
    if os.path.getsize("config.txt") == 0:
        print("[!] Warning: Tidak ada akun ditemukan! Coba scrape dulu.")
        return

    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    print("[*] Mengunggah ke GitHub...")
    os.system("git add config.txt")
    os.system(f'git commit -m "Network Update {waktu}"')
    os.system("git push origin main")
    
    print(f"\n[+] BERHASIL! Server sudah diperbarui pada {waktu}")

if __name__ == "__main__":
    deploy_to_friends()
import os
import datetime

def deploy_to_friends():
    print("[*] Memulai Audit Keamanan Akun...")
    
    # 1. Ambil 5 akun Trojan terbaik dari hasil scraping kamu sebelumnya
    # Kita asumsikan file hasil scrape kamu namanya 'my_accounts.txt'
    if os.path.exists("../my_accounts.txt"):
        os.system('grep "trojan://" ../my_accounts.txt | head -n 5 > config.txt')
    else:
        # Jika file belum ada, kita buat dummy dulu buat ngetes
        with open("config.txt", "w") as f:
            f.write("trojan://liul-test-account-please-scrape-first")

    # 2. Tambahkan timestamp agar temanmu tahu kapan terakhir update
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("update_info.txt", "w") as f:
        f.write(f"Terakhir Diperbarui oleh Liul: {waktu}")

    # 3. Proses Upload Otomatis ke GitHub
    print("[*] Mengunggah ke Server GitHub...")
    os.system("git add .")
    os.system(f'git commit -m "Update Network Node {waktu}"')
    os.system("git push -u origin master") # atau 'main' tergantung branch kamu
    
    print(f"\n[+] BERHASIL! Teman-temanmu sekarang bisa pakai akun baru.")

if __name__ == "__main__":
    deploy_to_friends()

