import time
import itertools

# Algoritma Brute Force
def brute_force_password(password_length, charset, target_password):
    start_time = time.time()  # Catat waktu awal
    combinations = itertools.product(charset, repeat=password_length)
    for attempt in combinations:
        password = ''.join(attempt)
        if password == target_password:
            end_time = time.time()  # Catat waktu akhir
            return password, end_time - start_time  # Kembalikan password dan waktu eksekusi
    return None, None

# Algoritma Backtracking
def backtrack_password(password_length, charset, target_password, password=''):
    start_time = time.time()  # Catat waktu awal
    if len(password) == password_length:
        if password == target_password:
            end_time = time.time()  # Catat waktu akhir
            return password, end_time - start_time  # Kembalikan password dan waktu eksekusi
        else:
            return None, None
    for char in charset:
        result, exec_time = backtrack_password(password_length, charset, target_password, password + char)
        if result:
            return result, exec_time
    return None, None

def main():
    # Input panjang kata sandi dari pengguna
    while True:
        try:
            password_length = int(input("Masukkan panjang kata sandi yang ingin diuji: "))
            if password_length <= 0:
                raise ValueError("Panjang kata sandi harus merupakan bilangan bulat positif.")
            break
        except ValueError as e:
            print(e)

    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    target_password = 'password123'  # Kata sandi target untuk dicari

    # Variabel untuk menyimpan total waktu eksekusi untuk setiap algoritma
    total_brute_force_time = 0
    total_backtrack_time = 0

    # Analisis efisiensi algoritma dan statistik waktu rata-rata
    num_trials = 5  # Jumlah percobaan untuk setiap ukuran input
    for _ in range(num_trials):
        # Analisis algoritma brute force
        brute_force_result, brute_force_time = brute_force_password(password_length, charset, target_password)
        total_brute_force_time += brute_force_time
        
        # Analisis algoritma backtracking
        backtrack_result, backtrack_time = backtrack_password(password_length, charset, target_password)
        total_backtrack_time += backtrack_time

    # Hitung statistik waktu rata-rata
    avg_brute_force_time = total_brute_force_time / num_trials
    avg_backtrack_time = total_backtrack_time / num_trials

    # Tampilkan hasil
    print("\nStatistik Waktu Rata-rata:")
    print(f"Brute Force | Execution Time: {avg_brute_force_time:.6f} seconds")
    print(f"Backtracking | Execution Time: {avg_backtrack_time:.6f} seconds")

    # Tampilkan password jika ditemukan
    if brute_force_result:
        print("\nPassword ditemukan dengan Brute Force:", brute_force_result)
    else:
        print("\nPassword tidak ditemukan dengan Brute Force.")
    if backtrack_result:
        print("Password ditemukan dengan Backtracking:", backtrack_result)
    else:
        print("Password tidak ditemukan dengan Backtracking.")

if __name__ == "__main__":
    main()