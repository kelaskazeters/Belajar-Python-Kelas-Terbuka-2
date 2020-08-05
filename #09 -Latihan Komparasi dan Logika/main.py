# Latihan logika dan komparasi

# Membuat gabungan area rentang dari angka

# ++++++3--------10+++++++

inputUser = float(input("Masukkan Angka Bernilai\nKurang Dari 3 \nAtau \nLebih Besar Dari 10 : "))
# ++++++3----------------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang Dari 3 =",isKurangDari)

# ---------------10++++++++
isLebihDari = (inputUser > 10)
print("Lebih Dari 10 =",isLebihDari)

# ++++++3--------10+++++++
isCorrect = isKurangDari or isLebihDari
print("Angka Yang Anda Masukkan :",isCorrect)

# ------3++++++++10-------
# Kasus irisan
print("\n",39*"=","\n")
inputUser = float(input("\nMasukkan Angka Bernilai\nLebih Dari 3 \nDan \nKurang Dari 10 : "))

# -----3++++++++++++++++++
# Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =",isLebihDari)

# +++++++++++++=+10-------
# Kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 =",isKurangDari)

# ------3++++++++10-------
isCorrect = isKurangDari and isLebihDari
print("Angka Yang Anda Masukkan :",isCorrect)