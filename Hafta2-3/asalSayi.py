# for sayi in range(1,101):
#     if sayi > 2:
#         for i in range(2,sayi):
#             if(sayi % i) == 0:
#                 break
#         else:
#             print(f"{sayi} asal sayıdır")

#FAKTÖRİYEL:

num = int(input("Bir sayı girin:"))
faktoriyel = 1

for i in range(1,num+1):
    faktoriyel *= i

print(f"{num}! = {faktoriyel}")