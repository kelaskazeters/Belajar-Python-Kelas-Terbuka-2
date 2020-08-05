# Latihan konversi satuan temperature

# Program konvesi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("Suhu adalah",celcius,"celcius")

# Reamur
reamur = (4 / 5) * celcius
print("Suhu dalam reamur adalah",reamur,"reamur")

# Fahrenhait
fahrenhait = ((9 / 7) * celcius) + 32
print("Suhu dalam fahrenhait adalah",fahrenhait,"fahrenhait")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah",kelvin,"kelvin")
