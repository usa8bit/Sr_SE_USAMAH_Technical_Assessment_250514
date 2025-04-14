def tingkat_kemahiran_maksimal(N, A, B, M):
    lawan = list(zip(A, B))
    while True:
        kandidat_lawan = [x for x in lawan if x[0] <= M]
        if not kandidat_lawan:
            break
        tambah_kekuatan = kandidat_lawan[0]
        M += tambah_kekuatan[1]
        lawan.remove(kandidat_lawan[0])
    return M
    print("Tingkat kemahiran maksimal yang akan di dapat", str(M))

# N = 5
# M = 9
# A = [2, 3, 6, 7, 8]
# B = [3, 4, 2, 2, 3]
# print(tingkat_kemahiran_maksimal(N, A, B, M))

N = input("Baris pertama dua buah bilangan N dan M (1<=N, M<= 100): ")
M = input()
A = list(input("Baris kedua N buah bilangan Ai (1<=Ai<=1000): ").split(","))
B = list(input("Baris ketiga N buah bilangan Ai (1<=Ai<=1000): ").split(","))

tingkat_kemahiran_maksimal(N, A, B, M)
