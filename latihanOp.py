#oprator

a =10
b =9
c =12
penjumlahan = a + b + c
sisabagi = a % b
perkalian = a * b * c
pembagian = a / b 
pengurangan = a - b - c
pembagianbulat = a // b
perpangkatan = a ** b
print(f"hasil penjumlahan {a} + {b} + {c} = {penjumlahan}")
print(f"hasil sisabagi {a} % {b} = {sisabagi}")
print(f"hasil perkalian {a} * {b} * {c} = {perkalian}")
print(f"hasil prmbagian {a} // {b} = {pembagian}")
print(f"hasil pengurangan {a} - {b} - {c} = {pengurangan}")
print(f"hasil pembagianbulat {a} // {b} = {pembagianbulat}")
print(f"hasil perpangkatan {a} ** {b} = {perpangkatan}")

#oprator assigment

a += 9 #19 a = 10 + 9
a **= 9 #361 a = 19 ** 9
print(a)

#oprator perbandingan
perbandingan = a >= b #361 >= 2 true

x = 6
y = 3
banding = x <= y 

print(x !=y)
print(perbandingan)

#oprator logika
opAnd = a >= b and x !=y
opOR = perbandingan or banding or x != y
opNOT = not opOR
print(opAnd)
print(opOR)
print(opNOT)