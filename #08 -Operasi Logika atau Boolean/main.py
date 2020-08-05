# Operasi Logika atau Boolean

# not, or, and, xor

# NOT 
print("~~~~~NOT~~~~~")
a = True
c = not a
print("Data a =",a)
print("-------------- NOT")
print("Data c =",c)

# OR (Jika salah satu true, maka hasilnya adalah true)
print("\n~~~~~OR~~~~~")
a = False
b = False
c = a or b
print("\n",a,"OR",b,"=",c)
a = False
b = True
c = a or b
print("\n",a,"OR",b," =",c)

a = True
b = False
c = a or b
print("\n",a,"OR",b," =",c)

a = True
b = True
c = a or b
print("\n",a,"OR",b,"  =",c)

# AND(Jika dua buah nilai true, maka hasil true)
print("\n~~~~~AND~~~~~")
a = False
b = False
c = a and b
print("\n",a,"AND",b,"=",c)
a = False
b = True
c = a and b
print("\n",a,"AND",b," =",c)

a = True
b = False
c = a and b
print("\n",a,"AND",b," =",c)

a = True
b = True
c = a and b
print("\n",a,"AND",b,"  =",c)

# XOR (Akan true jika salah satu true, sisanya false)
print("\n~~~~~XOR~~~~~")
a = False
b = False
c = a ^ b
print("\n",a,"XOR",b,"=",c)
a = False
b = True
c = a ^ b
print("\n",a,"XOR",b," =",c)

a = True
b = False
c = a ^ b
print("\n",a,"XOR",b," =",c)

a = True
b = True
c = a ^ b
print("\n",a,"XOR",b,"  =",c)
