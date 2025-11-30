
#! Lists
#Farklı veri tiplerini tek bir yerde tutar
#Listeler verileri kalıcı olarak depolamazlar
#Listeler RAM'de (geçiçi) verileri tutar, heap alanında referansları saklanıyor.
#Index mantığı, 0. indexten başlayıp pozitif yönde ilerler

#todo Listelerde metot kullanımı: 
#region boxers 
boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewix', "Evander Holyfiled", "George Foreman"]

#? Listenin sonuna "Rocky Marciano"
boxers.append("Rocky Marciano") #Listenin sonuna ekler
#nokta notasyonu = bir objenin sonuna nokta konulduğunda ona ait features/functions gelir.
print(boxers)

#? Kullanıcıdan alınan boksör ismini yine kullanıcıdan alınan index değerine yazdıralım
boxer_name = input("Name: ")
index_value = int(input("Index: "))
boxers.insert(index_value, boxer_name)
print(boxers)

#? Merge Two Lists 
royal_division = ["Antorny Jasua", "Tyson Fury", "Deantony Wilder"]
boxers.extend(royal_division)
print(boxers)

#? Read an Item
print(boxers[2])

#? 5. indexte bulunan itemı "Joe Frazeir" ile değiştirin.
boxers[5] = "Joe Frazeir"
print(boxers)

#? 0. Indexteki elemanı silelim
boxers.pop(0)
print(boxers)

#veya

boxers.remove("Lenox Lewix")
print(boxers)

#? Listedeki içindeki itemları alıp işleme sokulması, yani teker teker sırayla dolaşılması
for boxer in boxers: #boxer geçiçi bir isim olarak verildi burada.
    print(boxer)

for i in range(len(boxers)): #boxers listesinin uzunluğu kadar
    print(boxers[i])

for ch in 'adal su': #"adal su" kısım da string aslında liste mantığı gibi çalışabilir.
    print(ch,end='-') #bundaki her karakteri de teker teker dolaşabiliyorum.

#endregion

#region Formula 1 Drivers
drivers = [
    "Oscar Piastri", "Lando Norris", 
    "George Russell", "Kimi Antonelli",
    "Max Verstappen", "Yuki Tsunoda",
    "Charles Leclerc", "Lewis Hamilton"]
print(drivers) #buraya herhangi bir şey eklemedik yani albon'u görmeyeceğiz.

drivers.append("Alexander Albon") #Append metodu ile albonu liste sonuna ekledik
print(drivers) #burada ise albonu görürüz

drivers.insert(1,  "Carlos Sainz") #Insert metodu ile 1. index değerine "Carlos Sainz"'i sıkıştırdık.
print(drivers) #Burada 1. indexte sainzi görürüz

last_drivers = [
    "Liam Lawson", "Isack Hadjar",
    "Esteban Ocon", "Oliver Bearman",
    "Lance Stroll", "Fernando Alonso", 
    "Nico Hulkenberg", "Gabriel Bortoleto"
    "Pierre Gasly", "Franco Colapinto"
] #yeni bir liste tanımladık ve burada kalan diğer driverları yazdık.

drivers.extend(last_drivers) #drivers listesine last_drivers listesini ekledik
print(drivers) #burada iki listenin birleşmiş halini görürüz

print(drivers[2]) #Bu 2. indexteki değeri çekiyor, print fonksiyonu ile de yazdırdık.

drivers[4] = "DUTDUT DURUT" #MAX VERSTAPPEEEEN!
print(drivers) #4. Indexteki değeri (Kimi Antonelli) "DUTDUT DURUT" ile değiştirdik.

drivers.pop(4) #burda da DUTDUR DURUT" ifadesini index'i ile sildik.
print(drivers)
#buraya veya gelmeli
drivers.remove("DUTDUT DURUT") #burada da içeriğini girdik, ilk denk geldiğini siler.
print(drivers)

for driver in drivers:
    print(driver)

#endregion




# #! users = ["Burak Yılmaz", "Rana Nur Ceylan", "İpek Yılmaz", "Kerim Abdurrahman Burak Yılmaz"]
# #? kurumsal mail adresi craft edicez
# #? sample --- rana.ceylan@outlook.com yani: ilkisim.soyidim@outlook.com
# #? craft edilen mail adresleri maid_adress listesine eklenerek ekrana basılacak
# #? ipucu: split() fonksiyonu, bir listenin uzunluğu ne olursa olsun son elemanına nasıl ulaşırım? 

# #region Kendi denemem

# # users = ["Burak Yılmaz", "Rana Nur Ceylan", "İpek Yılmaz", "Kerim Abdurrahman Burak Yılmaz"]

# # users_splited = users.split(" ")

# # mail_adress = []

# # for user in users:
# #     user = user.lower()
# #     name_piece = user.split(" ")
# #     first_name = name_piece[0]
# #     last_name = name_piece[1]
# #     mail_adress.__add__

# #endregion

# #region Hocanın çözümü

# # users = ['Burak Yılmaz', 'Rana Nur Ceylan', 'İpek Yılmaz', 'kerim Abdurrahman Burak Yılmaz']
# # mail_addresses = []
# # domain_name = "@outlook.com"
# # for user in users:
# #     user_names = user.lower().split(" ")
# #     mail_address = (f"{user_names[0]}.{user_names[-1]}{domain_name}")
# #     mail_addresses.append(mail_address)
# # print(mail_addresses)

# #endregion

# #region hocanın örnek ödevi
# #! end userdan bir söz öbeği alalım mesela anladım hocam teşekkür ederim gibi
# #! sample = buRa1k _Ayi?Lm2aZu
# #! sesli harfleri sesli_harfler[] (listesine)
# #! sessiz harfleri ---- sessiz_harfler[]
# #! yazım hatalarını ---- typo_characters = []
# #! space karakteri ignore
# #! ilgili listelerdeki hiçbir eleman tekrar etmeyecek. Hep küçük harflerden devam 

# # sesli_harfler = []
# # sessiz_harfler = []
# # typo_characters = []

# # word = input("Type something: ")

# # for ch in word.lower():
# #     if ch.isalpha(): #karakter alfabetik mi diye bakıyoruz.
# #         if ch not in sesli_harfler and ch not in sessiz_harfler:
# #             if ch in "aeıioöuü":
# #                 sesli_harfler.append(ch)
# #             else:
# #                 sessiz_harfler.append(ch)
# #     else:
# #         if ch == " ":
# #             continue
# #         typo_characters.append(ch)

# # print(sesli_harfler)
# # print(sessiz_harfler)
# # print(typo_characters)

# #endregion

# #region ders örneği 
# #lst1 ve lst2 içerisine rastgele 10 tane sayı üretip doldurun
# #doldurma işlemini index mantığına göre yapın
# #örneğin list[0] + lst[0] toplanarak lst 3'ün indexine yazılacak, append yok

# #region kendi çözümüm
# # lst_1 = []
# # lst_2 = []
# # lst_3 = []

# # from random import randint

# # for i in range(10):
# #     sayi_1 = randint(a=0,b=100)
# #     lst_1.insert(i, sayi_1)
# #     sayi_2 = randint(a=0,b=100)
# #     lst_2.insert(i, sayi_2)
# #     lst_3.insert(i, sayi_1+sayi_2)

# # print(lst_1)
# # print(lst_2)
# # print(lst_3)

# #endregion

# #region hocanın çözümü
# # lst_1 = []
# # lst_2 = []
# # lst_3 = []

# # from random import randint

# # for i in range(10):

# # #    print(randint(a=0,b=100)) #1. adım, ürettik evet 10 tane
# #     lst_1.insert(i, randint(a=0,b=100)) #2. adım ooh hemen üretilen kodla lst_1'e ekleyek
# #     lst_2.insert(i, randint(a=0, b=100)) #4. adım, bak bunu da ürettik hatta test edelim yine.

# #     lst_3.insert(i, lst_1[i]+lst_2[i]) #6. adım, oh misler gibi çalıştı bak, bir deyazdıralım da görelim
# # #print(lst_1) #3. test adımı, ee düzgün çalışıyor demekki o zaman lst_2'ye de aynı şekilde ekleyek
# # #print(lst_2) #5. adım, çözdük, o zaman devamke
# # print(f"{lst_1}\n{lst_2}\n{lst_3}")
# #endregion
# #endregion

# #region nested list

# # ilceler = [
# #     ["Sarıyer"],
# #     ["Etiler", "Nispetiye", "Ulus"],
# #     ["Suadiye", ["Feneryolu", "Erenköy"]],
# #     [["Beşiktaş", "Maçka"], "Harbiye", ["Nişantaşı"]]
# # ]

# # #ana listenin 4 elemanı var ama ilceler listesinin elemanlarının içerisinde de listeler var
# # #matriks gibi düşün matematikteki

# # print(ilceler[3][0][0])

# #endregion

# #region Slicing (Dilimleme)
# #Pandas (veri analizinde de yani) kullanılır, çok önemli

# # fruits = [
# #     "Apple", "Banana", "Orange", "Mango", "Pineapple",
# #     "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
# #     "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
# #     "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
# # ]

# #dilimleme mevzuda: iki nokta üst üste özel karakter yani her şey bunun altından çıkıyor

# # print(fruits[2:7]) #birinci değer başlangıç indexi, ikinci değer n-1 olacak şekilde kapanış indexi
# # print(fruits[:3]) #burada başlangıç belirtilmedi yani başlangıç 0 ve burada : ile 3.ye kadar diyoruz
# # print(fruits[1::2]) #birden başla, iki iki zıplayarak git demek çift iki nokta ile 
# #print(fruits[::4]) #gene başlangıvı vermedi ama 4er 4er zıplayarak git 

# #print(fruits[::-1]) #0dan başla, -1 -1 git dedik ve aslında listeyi tersine çevirmiş olduk. 
# # eksi koyunca reverse ediliyor gibi düşün, 0. eleman direkt son eleman gibi düşün
# # print(fruits[10::-3]) #başlangıç verdik diye burda reverse düşünme, 10. elemandan başla geriye doğru 3er adımla git

# # print(fruits[::-2])

# #endregion

# #region Unpacking - unboxing

# # my_family = [
# #     ["Adal Su Uygur", 29, "Analyst"],
# #     ["Yasemin Uygur Erdem", 33, "Teacher"],
# #     ["Abdülfettah Uygur", 37, "Engineer"],
# #     ["Süreyya Uygur", 61, "Retired"],
# #     ["Abdülrezzak Uygur", 67, "Old? :D"]
# # ]

# # for item in my_family:
# #     print(item)


# # for name, age, occupation in my_family: #myfamilyden bana gelen bilgileri öyle bir karşılayayım ki tık tık tık eşleşsin
# #     print(
# #         f"Full name: {name}\n"
# #         f"Age: {age}\n"
# #         f"Occupation: {occupation}"
# #     )
# # #Unpacking yaparken karşılaması gereken valueların tam olması lazım, eksik veya fazla olursa patlar

# #endregion


# #region örnek
# #login istedik, kullanici adi ve sifre iste listeyi mi kontrol et
# #bütün ürünlerin toplam fiyatı nedir
# #ürün adı laptop olan ürünlerin fiyatlarını toplayalım
# #kullanıcı ürün search edebilsin, yani ürün search etti monitör yazdı varsa fiyatını verdi
# #fiyatı 200 tl altında olan ürünler listelensin
# #register olsun, yani kayıt da olsun; username varsa hali hazırda ekleyemesin

# users = [
#     ["beast", "123"],
#     ["bear", "456"],
#     ["keko", "789"]
# ]

# products = [
#     ["Laptop", 850],
#     ["Smartphone", 499],
#     ["Headphones", 79],
#     ["Keyboard", 45],
#     ["Monitor", 220],
#     ["Mouse", 25],
#     ["Smartwatch", 150],
#     ["Tablet", 310],
#     ["External Hard Drive", 95],
#     ["Webcam", 60],
#     ["Laptop", 850]
# ]

# username = input("username: ").lower()
# password = input("password")

# for user, parola in users: #döngüdeki her bir girdiyi user ve parola değişkenlerine atadık.
#     if user == username and parola == password: #eğer user ve pasaport inputlarla eşleşiyorsa sağlıklı giriş sağlandı.
#         print("Login successful")
#         break
#     else: #eşleşmiyorsa 
#         new_user = bool(input("Giriş başarısız, yeni bir üyelik açmak ister misiniz? (1/0)")) #yeni bir üyelik ister miyiz dedik
#         if new_user == True: #evet derse
#             new_username = input("Username: ") #username istedik
#             if new_username == user: #ve username bizim tanımladığımız userlarda varsa
#                 while True:
#                     print("Username already taken, pick another one.")
#                     new_username = input("Username: ")
#                     if new_username != user:
#                     break

#         #Buraya kod bloğu gelecek.
# print("Giriş başarısız.")




#         # new_login = input("Yeni hesap açmak ister misiniz?")
#         # if new_login == True:
#         #     new_username = input("username: ").lower()
#         #     if new_username == user:
#         #         print("Aynı giriş kabul edilemez, farklı bir giriş deneyin.")
#         #     new_password = input("Password: ")



