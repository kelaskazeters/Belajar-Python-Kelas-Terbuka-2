inputUser = float(input("Masukkan Angka \nLebih Dari 0, Kurang Dari 5\nAtau\nLebih Dari 8, Kurang Dari 11\n: "))
# Lebih dari 0
jwb1 = (inputUser > 0)
print("Lebih Dari  0  :",jwb1)

# Kurang dari lima
jwb2 = (inputUser < 5)
print("Kurang Dari 5  :",jwb2)

# Lebih dari 8
jwb3 = (inputUser > 8)
print("Lebih Dari  8  :",jwb3)

# Kurang dari 11
jwb4 = (inputUser < 11)
print("Kurang Dari 11 :",jwb4)

# ------0+++++5------8+++++11------
jawabanUtama = (jwb1 and jwb2) or (jwb3 and jwb4)
print("Angka Yang Anda Masukkan :",jawabanUtama)