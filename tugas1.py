nama = input("Masukkan namamu : ")
m = input("Masukkan nilai m : ")
n = input("Masukkan nilai n : ")

def funcMat(m,n):
    res = []
    matrix = []
    for i in range(1, int(m) + 1):
        arr = 0
        resArr = []
        for x in range(1, int(n) + 1):
            q = input("Masukkan elemen matriks baris ke " + str(i) + " kolom " + str(x) + " : ")
            arr += int(q)
            resArr.append(int(q))
        res.append(arr)
        matrix.append(resArr)

    valid = True
    # print(res)

    for i in range(len(res)):
        if i > 0 and i != len(res) - 1:
            if res[i - 1] == 0:
                valid = False
        elif i == len(res) - 1:
            if res[i - 1] == 0 and res[i] > 0:
                valid = False
        # print(str(i) + " " + str(res[i]))

    if valid:
        print("Matriks sudah sesuai dengan matriks yang diinginkan")
    else:
        print("Matriks tidak sesuai dengan matriks yang diinginkan")

    for x in range(len(matrix)):
        print(matrix[x])

funcMat(m,n)