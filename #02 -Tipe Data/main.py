# a = 10, a adalah variable dengan nilai 10

# tipe data : Angka bulat (int)
data_int = 1
print("data :",data_int)
print("bertipe data :",type(data_int))

# tipe data : Angka decimal (float)
data_float = 1.5
print("data :",data_float)
print("bertipe data :",type(data_float))

# tipe data : Kumpulan character (string)
data_string = "Ucup 10"
print("data :",data_string)
print("bertipe data :",type(data_string))

# tipe data : Kumpulan character (boolean)
data_boolean = False
print("data :",data_boolean)
print("bertipe data :",type(data_boolean))

# Tipe data khusus

# Bilangan complex 
data_complex = complex(5,6)
print("data :",data_complex)
print("bertipe data :",type(data_complex))

# Tipe data dari bahasa c

from ctypes import c_double

data_c_double = c_double(10.5)
print("data :",data_c_double)
print("bertipe data :",type(data_c_double))