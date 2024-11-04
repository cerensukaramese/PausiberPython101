
# - Liste(List)

# liste = [1,2,3,4,5]
# print(type(liste))
# print(liste)

# liste = [1,2,'Ali','Ayşe',3.61,True]
# print(liste)
# print(type(liste))

# liste = [1,2,3,[2,3,4],[10,45]]
# print(liste)

# liste = [1,2,'Ali','Ayşe',3.61,True]

# print(f"Listenin birinci elemanının tipi : {type(liste[0])} ve elaman : {liste[0]}")

# liste = [1,2,3,4]

# liste = liste + [10]
# liste = liste + ["11"]
# print(type(liste[5]))
# print(liste)

# cumle = "PauSiber Python Eğitimi"
# #ayriCumle = cumle.split() #deafult değeri boşluklara göre ayırır 
# ayriCumle = cumle.split("i") #parametreye göre ayırır 
# print(ayriCumle)

# liste = [1,2,3]
# print(liste[1]) #index ile elemanlara ulaşılır. Liste 0.indexten başlar 


#liste = [1,2,3,4,5,6,7]
# son indexe ulaşmak istiyoruz 

# liste = [1,2,3]
# #print(liste[-1])
# print(liste)
# print(liste[::-1])
# print(liste[::-2])

# liste = [1,2,3,4]
# liste[0] = 5
# print(liste)

# --- Liste Metodları ---

# liste = ["Ahmet","Mehmet",1,2,True,3.45,2]

# liste.append(1)
# liste.append("Veli")
# liste.reverse()
# liste.remove(2)
# liste.clear()
# print(liste.count(2))
# print(liste.index("Ahmet"))
# liste.pop(0)  --> default hali son eleman 
# liste.insert(0,"Musa") --> istediğimiz indexe eleman ekleme 

# print(liste)

# --- set() Metodu --- 

# liste = [1,2,3,3,4,5]

# setted_liste = set(liste)
# print(liste)
# print(setted_liste)

# set() metodu birden fazla aynı olan elemanları teke indirger 

# Tuple (Demet) 

'''
    list    --> [] --> mutable
    set     --> {} aynı elemanarı teke indirger --> mutable
    tuple   --> () değiştirlemez yapar  --> immutable
'''


# liste = [1,2,3]
# # print(liste)

# # liste[0] = "Ali"
# # print(liste)

# tuple_list = tuple(liste)

# print(tuple_list)

# tuple_list[0] = "Mehmet"

# --- Dictionary (Sözlük) --- 

# sözlük --> anahtar == değer 
# dictironary --> key == value 

# benim_sozlugum = {'isim' : 'Ali', 'soyiyim' : 'Veli', 'yas' : 18}
# print(benim_sozlugum) 

# dict = {
#     'isim' : 'mehmet',
#     'soyiyim' : 'çakır',
#     'memleket' : 'istanbul',
#     'yas' : 18,
#     10 : 'on'
# }

'''
     key      value 
    -----     ----- 
    isim      mehmet
    soyiyim   çakır 
    memleket  istanbul 

'''

#print(dict["soyisim"])

# dict = {
#     'isim' : 'Mehmet',
#     'soyisim' : 'Mutlu',
#     'sehirler' : {
#         'memleket' : 'Ankara',
#         'yasadigi_sehir' : 'Denizli',
#         'calistigi_yer' : 'Burdur',
#         'gezmelik_yer' : 'İzmir',
#     },
#     'yas' : 40
# }

# print(dict['sehirler']['gezmelik_yer'])
#print(dict)

# dict = {
#     'isim' : 'mehmet',
#     'soyisim' : 'çakır',
#     'memleket' : 'istanbul',
#     'yas' : 18,
#     }

# # print(dict.get('isim'))

# # dict['isim'] = 'Mustafa'

# # print(dict)

# dict['okul'] = 'Pamukkale Üniversitesi'
# print(dict)

# personel = {
#     'Mehmet Bey' : 'AR-GE Müdürü', # ---> her biri bir item 
#     'Selin Hanım' : 'Takım Kaptanı',
#     'Ali Bey' : 'Departman Sorumlusu'
# }
# personel['Fatmanur Hanım'] = 'Mühendis'

# #print(personel)

# print(personel.keys())
# print(personel.values())
# print(personel.items()) # --> items = key + value 



