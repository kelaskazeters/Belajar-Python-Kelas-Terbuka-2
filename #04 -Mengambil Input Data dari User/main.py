# Episode input user

# Data yang dimasukkan adalah string
data = input("Masukkan data : ")

print("data =",data,"type :",type(data))

# Jika kalian ingin mengambil int, maka
data_float = float(input("Masukkan Angka : "))
data_int   = int(input("Masukkan Angka : "))

print("data =",data_int,"type :",type(data_int)) # jika yang dimasukkan text, make dia akan error

# Bagaimana dengan boolean
binary = bool(int(input("Masukkan nilai boolean : ")))

print("data =",binary,"type :",type(binary))