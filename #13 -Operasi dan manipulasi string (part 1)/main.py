# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Rafliano"
nama_tengah = "Ziyad"
nama_akhir = "Adzani"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator pada string

# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))\

D = "D"
status = d not in nama_lengkap
print(D + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulangan string
print("wk"*10)
print(15*"awok")

# indexing
print("index ke 0 : " + nama_lengkap[0])
print("index ke 6 : " + nama_lengkap[6])
print("index ke (-1) : " + nama_lengkap[-1])
print("index ke (-2) : " + nama_lengkap[-2])
print("index ke [0:4] : " + nama_lengkap[0:5])
print("index ke [0,2,4,6,8,10] : " + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("ASCII code untuk 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "Ucup Markucup"
jumlah = data.count("u")
print("jumlah u pada " + data + " = " + str(jumlah))