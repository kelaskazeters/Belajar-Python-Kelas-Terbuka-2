# Operasi komparasi

# Setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih besar dari >
print("\n~~~~~LEBIH BESAR DARI(>)~~~~~")
hasil = a > 3
print(a,">",3,"=",hasil)

hasil = b > 3
print(b,">",3,"=",hasil)

hasil = b > 2
print(b,">",2,"=",hasil)

# Kurang dari <
print("\n~~~~~KURANG DARI(<)~~~~~")
hasil = a < 3
print(a,"<",3,"=",hasil)

hasil = b < 3
print(b,"<",3,"=",hasil)

hasil = b < 2
print(b,"<",2,"=",hasil)

# Lebih dari sama dengan >=
print("\n~~~~~LEBIH DARI SAMA DENGAN(>=)~~~~~")
hasil = a >= 3
print(a,">=",3,"=",hasil)

hasil = b >= 3
print(b,">=",3,"=",hasil)

hasil = b >= 2
print(b,">=",2,"=",hasil)

# Kurang dari sama dengan <=
print("\n~~~~~KURANG DARI SAMA DENGAN(<=)~~~~~")
hasil = a <= 3
print(a,"<=",3,"=",hasil)

hasil = b <= 3
print(b,"<=",3,"=",hasil)

hasil = b <= 2
print(b,"<=",2,"=",hasil)

# Sama dengan (==)
print("\n~~~~~Sama Dengan(==)~~~~~")
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = b == 4
print(b,"==",4,"=",hasil)

# Tidak sama dengan (==)
print("\n~~~~~Sama Dengan(!=)~~~~~")
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = b != 4
print(b,"!=",4,"=",hasil)

# Is sebagai komparasi object identity
print("~~~~~OBJECT IDENTIFY(IS)~~~~~")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai x =",y,"id = ",hex(id(y)))
hasil = x is y
print("x is y =",hasil)

# Is sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 6
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai x =",y,"id = ",hex(id(y)))
hasil = x is y
print("x is y =",hasil)

print("~~~~~OBJECT IDENTIFY(IS NOT)~~~~~")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai x =",y,"id = ",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai x =",y,"id = ",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)
