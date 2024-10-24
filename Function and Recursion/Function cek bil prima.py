#Deklarasi sebuah fungsi bernama "cekprima" untuk mengecek apakah dia bilangan prima atau tidak
def cekprima(N):
    not_prima = 0
    for a in range(1, int((N**0.5) + 1)):
        if N % a == 0 and a != 1:
            not_prima += 1
            break
    if not_prima == 1:
        print(f"{N} bukan bilangan prima")
    else:
        print(f"{N} bilangan prima")
            
#Input nilai N yang merupakan bilangan bulat
N = int(input())
#Panggil fungsi cek prima yang telah dibuat di atas agar mengecek apakah N prima atau tidak.
cekprima(N)

        