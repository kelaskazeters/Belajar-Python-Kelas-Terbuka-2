# Kita belajar casting
# Merubah dari tipe data ke tipe data yang lain
# Tipe data = int, float, string, boolean

# Int
print("=====Int=====")
data_int = 9
print("data =",data_int,",tipe data =",type(data_int))

data_float    = float(data_int)
data_string   = str(data_int)
data_boolean  = bool(data_int) # Akan false jika nilai int = 0

print("data =",data_float,",tipe data =",type(data_float))
print("data =",data_string,",tipe data =",type(data_string))
print("data =",data_boolean,",tipe data =",type(data_boolean))

# Float
print("=====Float=====")
data_float = 9.9
print("data =",data_float,",tipe data =",type(data_float))

data_int      = int(data_float) # Akan dibulatkan kebawah
data_string   = str(data_float)
data_boolean  = bool(data_float) # Akan false jika nilai float = 0

print("data =",data_int,",tipe data =",type(data_int))
print("data =",data_string,",tipe data =",type(data_string))
print("data =",data_boolean,",tipe data =",type(data_boolean))

# Boolean
print("=====Boolean=====")
data_boolean = True
print("data =",data_boolean,",tipe data =",type(data_boolean))

data_int      = int(data_boolean) # Akan dibulatkan kebawah
data_string   = str(data_boolean)
data_float    = float(data_boolean) # Akan false jika nilai float = 0

print("data =",data_int,",tipe data =",type(data_int))
print("data =",data_string,",tipe data =",type(data_string))
print("data =",data_float,",tipe data =",type(data_float))

# string
print("=====String=====")
data_string = ""
print("data =",data_string,",tipe data =",type(data_string))

data_int        = int(data_string) # String harus angka
data_float      = float(data_string) # String harus angka
data_boolean    = bool(data_string) # Akan false jika string kosong

print("data =",data_int,",tipe data =",type(data_int))
print("data =",data_float,",tipe data =",type(data_float))
print("data =",data_boolean,",tipe data =",type(data_boolean))