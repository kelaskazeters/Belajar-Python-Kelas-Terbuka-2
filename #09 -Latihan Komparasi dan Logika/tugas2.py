inputUser = float(input("Masukkan Angka \nKurang Dari 0, Lebih Dari 5\nAtau\nKurang Dari 8, Lebih Dari 11\n: "))
# Kurang dari 0
jwb1 = (inputUser < 0)
print("Kurang Dari 0 :",jwb1)

# Lebih dari lima
jwb2 = (inputUser > 5)
print("Lebih Dari  5 :",jwb2)

# Kurang dari 8
jwb3 = (inputUser < 8)
print("Kurang Dari 8 :",jwb3)

# Lebih dari 11
jwb4 = (inputUser > 11)
print("Lebih Dari 11 :",jwb4)

# ------0+++++5------8+++++11------
jawabanUtama = (jwb1 and jwb2) or (jwb3 and jwb4)
print("Angka Yang Anda Masukkan :",jawabanUtama)