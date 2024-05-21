#tabel kebenaran(logika bolean)
# and or not xor

# Not 1
x = False
y = not x

print("nilai dari x =", x)
print("nilai dari y =", y)

# and (akan bernilai false, selama ada satu aja yang true,)
# bernilai salah, ketika keduanya salah
print("\n**********Logika AND***********")
x = False 
y = False
z = x and y
print(x, "and", y, "=", z)

x = False 
y = True
z = x and y
print(x, "and", y, "=", z)

x = True
y = False
z = x and y
print(x, "and", y, "=", z)

x =True 
y = True
z = x and y
print(x, "and", y, "=", z)

# OR (akan bernilai true, selama ada satu aja yang true,)
# bernilai salah, ketika keduanya salah
print("\n**********Logika OR***********")
x = False 
y = False
z = x and y
print(x, "or", y, "=", z)

x = False 
y = True
z = x and y
print(x, "or", y, "=", z)

x = True
y = False
z = x and y
print(x, "or", y, "=", z)

x =True 
y = True
z = x and y
print(x, "or", y, "=", z)

#NOT

print("\n**********Logika NOT***********")
x = False 
y = False
z = x and y
print(x, "not", y, "=", z)

x = False 
y = True
z = x and y
print(x, "not", y, "=", z)

x = True
y = False
z = x and y
print(x, "not", y, "=", z)

x =True 
y = True
z = x and y
print(x, "not", y, "=", z)

#XOR

print("\n**********Logika XOR***********")
x = False 
y = False
z = x and y
print(x, "xor", y, "=", z)

x = False 
y = True
z = x and y
print(x, "xor", y, "=", z)

x = True
y = False
z = x and y
print(x, "xor", y, "=", z)

x =True 
y = True
z = x and y
print(x, "xor", y, "=", z)

