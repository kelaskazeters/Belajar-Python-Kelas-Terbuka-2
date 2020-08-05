# Operasi matematika

a = 10
b = 3

# Operasi penjumlahan +
print("Penjumlahan")
hasil = a + b
print(a,'+',b,'=',hasil)

# Operasi pengurangan -
print("Pengurangan")
hasil = a - b
print(a,'-',b,'=',hasil)

# Operasi perkalian *
print("Perkalian")
hasil = a * b
print(a,'*',b,'=',hasil)

# Operasi pembagian /
print("Pembagian")
hasil = a / b
print(a,'/',b,'=',hasil)

# Operasi pangkat **
print("Pangkat")
hasil = a ** b
print(a,'**',b,'=',hasil)

# Operasi modulus %
print("Modulus")
hasil = a % b
print(a,'%',b,'=',hasil)

# Operasi floor division //
print("Floor Division")
hasil = a // b
print(a,'//',b,'=',hasil)

# Operasi prioritas, operational presedence

"""
    Operasi yang diprioritaskan :
    1. ()
    2. *,/,**,%,//
    3. +,-
"""

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=',hasil)