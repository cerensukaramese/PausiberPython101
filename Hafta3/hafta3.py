a = 50
b = 70
# a += 5 # a= a + 5
# a -= 5
# a *= 1
# a /= 1
# a %= 1
# a //= 1

# result = [(a==b),(a!=b),(a<=b),(a>=b)] #a<b a>b

# print(result)

# if a < b:
#     print("a b'den büyüktür.")
# elif a == b:
#     print("a b'ye eşittir.")
# elif a > b:
#     print("büyük")
#     if a != b:
#         print("eşit değildir.")
# else:
#     print("a b'den büyük değildir.")

# if a > b:
#     print("a b'den küçük")
#     if a > 100:
#         print("a 100'den küçük")
#     else:
#         print("a 100'den küçük değil")    
# else:
#     print("koşul sağlanmadı")

# if a > b: 
#     pass
# elif a < b:
#     print("a<b")

# i = 0
# while True:
#     i += 1
#     print(i)
#     if i == 5:
#         break

# print(type(isimler))
# if "ahmet" in isimler:
#    print("true")

# for isim in isimler:
#     print(isim)
 
# a = "Veli"
# for i in a :
#     print(i)
# isimler = ["ahmet","mehmet","ali","zeynep"]
# for isim in isimler:
#     for i in isim:
#         print(i)

# a = [*"range(2,10)"]
# print(a)

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

liste = [1,2,3,4]
for i in liste:
    if i == 5:
        print("Öğe bulundu")
        break
    print(i)
else:
    print("Öğe bulunamadı")