nama = input("Masukkan nama pengguna:")
countFav = input("Masukkan banyaknya makanan favorit : ")

def funcFood(nama, countFav):
    makanan = []
    
    for i in range(1, int(countFav) + 1):
        x = input("Makanan favorit no " + str(i) + " : ")
        makanan.append(x)

    print("Nama pengguna:" + nama)
    print("Makanan favorit " + nama + " adalah :")
    for i in range(1, int(countFav) + 1):
        print(str(i) + ". " + makanan[i - 1])


funcFood(nama, countFav)