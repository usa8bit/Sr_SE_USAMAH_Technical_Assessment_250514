def kemahiran_maksimal(N, M, A, B):
    lawan = list(zip(A, B))
    while True:
        kandidat_lawan = [x for x in lawan if x[0] <= M]
        if not kandidat_lawan:
            break
        lawan_terbaik = max(kandidat_lawan, key = lambda x: x[1])
        M += lawan_terbaik[1]
        lawan.remove(lawan_terbaik)
    return M

# ====== MAIN PROGRAM ======
def main():
    # Input N dan M
    N, M = map(int, input("Masukkan N dan M (dipisahkan spasi): ").split())

    # Input Ai
    A = list(map(int, input(f"Masukkan {N} angka Ai (dipisahkan spasi): ").split()))

    # Input Bi
    B = list(map(int, input(f"Masukkan {N} angka Bi (dipisahkan spasi): ").split()))

    # Validasi panjang input
    if len(A) != N or len(B) != N:
        print("Jumlah input Ai dan Bi harus sama dengan N!")
        return

    # Hitung hasil
    hasil = kemahiran_maksimal(N, M, A, B)

    # Output hasil
    print("Tingkat kemahiran maksimal yang dicapai:", hasil)

# Jalankan program
if __name__ == "__main__":
    main()
