import requests
import random
import time

# URL target
url = "https://dizepsz.assimilationeject.top/#4C7s6W2t"  # Ganti dengan URL endpoint yang sesuai

# User-Agent list yang akan dipilih secara acak
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
]

# Fungsi untuk menghasilkan nomor telepon 12 digit yang tidak diawali dengan "08" atau "62"
def generate_random_phone_number():
    prefix = ""
    while prefix.startswith("08") or prefix.startswith("62") or len(prefix) != 3:
        prefix = str(random.randint(100, 999))  # 3 digit acak
    suffix = str(random.randint(100000000, 999999999))  # 9 digit acak
    return prefix + suffix

# Fungsi untuk mengatur cookie di Python
def set_cookie(name, value):
    cookie_string = f"{name}={value}; Path=/; Max-Age=2592000;"  # Expiry time is set to 30 days
    return cookie_string

# Fungsi untuk mendapatkan cookie yang sudah ada (simulasi get_cookie)
def get_cookie(name, cookies):
    return cookies.get(name, '')

# Fungsi untuk mengirim data ke server menggunakan form dinamis
def send_phone_number():
    phone_number = generate_random_phone_number()
    payload = {
        'num': phone_number
    }

    # Menyiapkan cookie yang dibutuhkan (misalnya "d", "e" untuk status)
    cookies = {
        'd': str(random.randint(1, 12)),  # Cookie "d" dengan nilai acak antara 1 hingga 12
        'e': str(random.randint(50, 100)),  # Cookie "e" dengan nilai acak antara 50 hingga 100
    }

    # Dapatkan cookie yang sudah ada (untuk simulasi get_cookie)
    existing_cookie = get_cookie('e', cookies)
    
    # Jika cookie 'e' ada, set cookie dengan nilai yang ada
    if existing_cookie:
        cookies['e'] = existing_cookie

    # Memilih user-agent secara acak
    headers = {
        'User-Agent': random.choice(user_agents)
    }

    try:
        # Mengirim POST request
        response = requests.post(url, data=payload, cookies=cookies, headers=headers)
        
        # Cek status respons
        if response.status_code == 200:
            log_message(f"Berhasil mengirim nomor: {phone_number}", 'success')
        else:
            log_message(f"Gagal mengirim nomor: {phone_number} (Status: {response.status_code})", 'error')
    except Exception as e:
        log_message(f"Kesalahan: {e}", 'error')

# Fungsi untuk mencatat log
def log_message(message, type):
    color = "green" if type == 'success' else "red"
    print(f"\033[1;{32 if color == 'green' else 31}m{message}\033[0m")

# Fungsi untuk memulai pengiriman dengan interval acak
def start_sending():
    while True:
        send_phone_number()
        # Interval acak antara 0.1 dan 3 detik
        time.sleep(random.uniform(0.1, 3))

# Fungsi untuk menghentikan pengiriman
def stop_sending():
    print("Pengiriman dihentikan.")
    exit()

# Mulai pengiriman
if __name__ == "__main__":
    try:
        start_sending()  # Mulai pengiriman nomor
    except KeyboardInterrupt:
        stop_sending()  # Hentikan pengiriman dengan Ctrl+C
