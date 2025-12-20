
#! Variables (Değişkenler)
#* Programlamada değişken (variable), verileri geçici olarak saklamak için kullanılan, isimlendirilmiş bir bellek alanıdır.
#* Değişkenin adı, programda runtime'da çalıştırılır.
#* Python özelinde: Değişkenler içerisine atılan değerin tipine bürünürler, önceden tanımlama gerektirmez.

#? SYNTAX
x = 10 #integer
y = 3.14 #float
is_active = True #boolean
isim = "Su" #string

#todo Matematiksel işlemler
number_1 = 2 #Dümmmmdüz tanımladık
number_2 = input("Type a number: ") #Kullanıcıdan isteyerek tanımladık ama baktık ki input metodu ile bize string geliyor
number_3 = int(input("Type a number: ")) #Bu sebeple burda int metodu içine alarak gelen ifadeyi integer'a çevirdik.

print(number_1 + number_3) #Bu şekilde iki değerin toplamını yazdırabiliriz ancak
addition = number_1 + number_3 #Best practice olarak (DRY Prensibine de uyması açısından)
print(addition) #bu şekilde yazdırılması daha sağlıklı

subtraction = number_1 - number_3
#Neden number_2 değişkenini almıyoruz? Çünkü o string bir ifade, ve integer + string ifadesi hata verir program patlar.
print(subtraction)

#region Examples

#todo Kullanıcıdan kenar bilgisi alınarak kare alan&çevre hesabı
edge = float(input("Edge: "))
square_area = edge * edge
square_perimeter = 4* edge

print(f'Square perimeter: {square_perimeter} - Square area: {square_area}') #f string ile değişkenleri de burada yazdırdık.
#f string best practice olarak oldukça işimize yarar, çünkü dinamik olarak gerekli olan ifadeyi çağırır.

#todo Kullanıcıdan kısa ve uzun kenar bilgisi alınarak dikdörtgenin alan&çevre hesabı
short_edge = float(input("Edge 1: "))
long_edge = float(input("Edge 2: "))
rectangle_area = short_edge * long_edge
rectangle_perimeter = 2 * (short_edge + long_edge) #kodlamada matematiksel işlem önceliği aynen geçerli olduğu için paranteze aldık.
print(f'Rectangle perimeter: {rectangle_perimeter} - Rectangle area: {rectangle_area}')

#todo Kullanıcıdan taban ve yükseklik bilgisi alınarak üçgenin alan&çevre hesabı
taban = int(input("Üçgenin tabanı: "))
h = int(input("Üçgenin yüksekliği: "))
ucgen_alani = h * taban / 2
print(f'Üçgenin alanı: {ucgen_alani}')

#todo Kullanıcıdan yarıçap alınarak dairenin alan&çevre hesabı
r = float(input("Dairenin yarıçapı: "))
import math
alan = math.pi * (r ** 2)
cevre = 2 * math.pi * r
print(f"Dairenin alanı {alan:.2f} birim ve çevresi {cevre:.2f} birimdir.") #:.2f ifadesi ondalıktan sonraki 2 basamağı göster anlamına geliyor.

#todo Kullanıcıdan tabanlar ve yükseklik bilgisi alınarak yamuğun alan hesabı
alt_taban = int(input("Yamuk alt kenarı: "))
ust_taban = int(input("Yamuk üst kenar: "))
h = int(input("Yamuk yükseklik: "))
print(f"Yamuğun alanı {(alt_taban + ust_taban) * h / 2:.2f} kadardır.")

#todo Ürünün adı ve fiyatını kullanıcıdan alıp fstring ile yazdırılması
urun_adi = input("Ürünün adı: ")
fiyat = input("Ürünün fiyatı: ")
print(f"Ürünün adı {urun_adi}'dır ve fiyatı {fiyat}'tır.")

#todo Kenarını kullanıcının verdiği karenin alanını f-string içerisinde hesaplayıp yazdırdık.
#burda f-string içerisindeki {} içerisinde işlem yapılabildiğini öğrendik.
kenar = int(input("Karenin kenarı = "))
print(f"Karenin alanı = {kenar * kenar}")

#endregion

#! Operatörler
#* Bir veya daha fazla işlenen, operand adı verilen değer üzerinde belirli bir matematiksel, mantıksal veya atama eylemini gerçekleştiren mekanizmalardır.

#? in operatörü
print('s' in 'su') #su içinde s varsa true döner
print('a' in 'su') #içinde mi diye sorar
#? not in operatörü
print('s' not in 'su') #su içinde s yoksa true döner
print('a' not in 'su') #içinde değil mi

#todo Girilen 3 sayıdan büyük olanın ekrana yazdılması (and & or operatörlerinin kullanılması)
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))
max_number = 0 #Maximum sayımıza atamak üzere bir değişken tanımladık

#burada hep matematikteki mantık ifadelerini düşün, çünkü aynı şekilde çalışıyor.
#Lisedeki ilk sınavında matematik sınavına girip mantık çözmüştün
#Hiç çalışmamıştın ve 30 bekliyordun, sınıf birincisi oldun ve 80 aldın.
#Daha sonra hiç çalışmayarak tüm liseyi geçeceğini sandın ama çok yanıldın :D Yine de bu güzel bir anı olarak kaldı. :)

#and için: 
# 1 1 = 1
# 1 0 = 0
# 0 1 = 0
# 0 0 = 0

#or için:
# 1 1 = 1
# 1 0 = 1
# 0 1 = 1
# 0 0 = 0
if n1 > n2 and n1 > n3: 
    max_number = n1
elif n2 > n1 and n2 > n3:
    max_number = n2
elif n3 > n1 and n3 > n2:
    max_number = n3
else:
    print(f'The given numbers could be same.')
    exit()
print(f'The maximum number is : {max_number}')

#! Control Flow Statements / Karar Mekanizmaları (If-Else, Match-Case)
#* Belirli bir koşulun sağlanıp sağlanmamasına göre farklı kod bloklarının çalıştırılmasının standart yoludur.

#region If - Elif - Else
#? If - Elif - Else SYNTAX
#* if - elif - else bloğunda herhangi bir şart tutarsa diğer şartlara bakılmaz.
#* Mantıksal operatörler (and, or, not) kullanarak birden fazla karmaşık koşulu aynı anda kontrol etmeye olanak tanır.
kosul_1 = ""
kosul_2 = ""
if kosul_1:
    # Koşul_1 doğru ise bu blok çalışır
    print("Koşul 1 Doğru")
elif kosul_2:
    # Koşul_1 yanlış VE Koşul_2 doğru ise bu blok çalışır
    print("Koşul 2 Doğru")
else:
    # Yukarıdaki koşulların hiçbiri doğru değilse bu blok çalışır
    print("Hiçbiri Doğru Değil")

#todo Kullanıcıdan alınan 2 tane tam sayının büyük olanının hesabı
number_1 = int(input("Birinci sayı: "))
number_2 = int(input("İkinci sayı: "))

if number_1 > number_2 :
    print(f'{number_1} daha büyüktür {number_2}')
elif number_1 == number_2: 
    print("Her ikisi birbirlerine eşittir.")
else:
    print(f'{number_2} daha büyüktür {number_1}')

#todo Girilen sayının tek mi çift mi
#* Kendi çözümüm ^^ (Mod ifadesini bilmiyordum, bu şekilde çözdüm. BU KOD BLOĞU sana workaround'un her zaman olduğunu göstersin!)
#* GO GIRLLLLL!!!!!
number = float(input("Sayıyı giriniz: "))
sonuc = number / 2
if sonuc.is_integer() == True:
    print("Sayı çifttir")
else:
    print("Sayı tektir.")

#Mod ifadesi ile kolay çözümü :)
sayi = int(input('Bir sayi giriniz :'))
if sayi %2 == 0:
    print(f'{sayi} çift')
else:
    print(f'{sayi} tek')
#endregion

#region Ternary If (Tek satır if)
#? Ternary If (Tek satır if) SYNTAX
#* Tek satırda if-else gibi düşün. Tek mi çift mi gibi tek şart olan durumlarda kullanılır.

#değişken = [True ise atanacak değer] if [koşul] else [False ise atanacak değer]
sayi = 0
sonuc = "Pozitif" if sayi > 0 else "Pozitif Değil (Sıfır veya Negatif)"

#todo Yaşını giren kullanıcının reşit olup olmaması durumunu kontrol eden ternary if
age = int(input("Your age: "))
status = "adult" if age >= 18 else "child"
print(status)

#todo Girilen sayının negatif mi pozitif mi olduğunu kontrol eden ternary if
number = int(input("Number: "))
print(f"Status {'positive' if number > 0 else 'negative'}") #f-string fonksiyonu içinde yazdık.

#todo Girilen sayının negatif mi pozitif mi olduğunu kontrol eden If-Elif-Else bloğu
number = int(input("Sayıyı giriniz: "))
if number > 0:
    print(f'Sayınız pozitiftir.')
elif number == 0:
    print("Sayınız nötrdür.")
else: 
    print("Sayınız negatiftir.")

#endregion

#region Match-case yapısı:
#? Match-case yapısı:
#* if else'e alternatif olarak gelen bir yapı. (C ailesindeki switch-case) match-case status kontrolü için sıklıkla tercih edilir ancak case'de and/or kullanmak daha zor.
#* Genel olarak birebir uyum (==) sağlandığında case ifadesi daha tercih edilir.

#todo Subscription yapılan üyeliklerdeki statusu beliren uygulama
boxing_gloves_status = "passive"
match boxing_gloves_status:
    case "passive":
        pass
    case "active":
        pass
    case "modified":
        pass
    case _:
        print("None")

#todo Match case'te and ifadesinin kullanımı (ÇOK ZOR SAÇMA SAPAN SYNTAX)
kitap = 5
adet_kitap = int(input('Satın Alınan Kitap Sayısı: '))
if adet_kitap <= 0:
    print('Eksi kitap sayısı olamaz.')
else:
    match adet_kitap:
        case n if 1 <= adet_kitap <= 5: #if ile iç içe kullanıyoruz :)
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.95}')
        case n if 5 <= adet_kitap <= 10:
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.90}')
        case n if 10 <= adet_kitap <= 15:
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.85}')
        case n if 15 <= adet_kitap <= 20:
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.80}')
        case _:
            print('En fazla 20 kitap satın alabilirsiniz.')
#endregion

#region examples

#region IF-ELIF-ELSE KULLANIMI

#todo Kenar uzunlukları girilen üçgenin eşkenar, ikizkenar, çeşitkenar olduğunu yazdıran uygulama
# kenar_1 = int(input("Kenar 1: "))
# kenar_2 = int(input("Kenar 2: "))
# kenar_3 = int(input("Kenar 3: "))
# if kenar_1 == kenar_2 and kenar_1 == kenar_3:
#     print("eşkenar")
# elif kenar_1 != kenar_2 and kenar_1 != kenar_3 and kenar_2 != kenar_3:
#     print("çeşitkenar")
# else:
#     print("ikizkenar")

#todo Karakterin sesli harf mi sessiz harf mi olduğunu bulan uygulama
# karakter = input("Karakter: ")
# if karakter.isalpha():
#     if karakter in "aeıioöuü":
#         print("sesli harf")
#     else:
#         print("sessiz harf")
# else:
#     print("girilen karakter alfabetik değil.")

#todo Girilen sayının +, 0, - olduğunu yazdıran uygulama
# sayi = int(input("Sayıyı giriniz: "))
# sayi_durumu = ""
# if sayi < 0:
#     sayi_durumu = "Negatif"
# elif sayi == 0:
#     sayi_durumu = "Nötr"
# elif sayi > 0:
#     sayi_durumu = "Pozitif"
# else:
#     print("İlginç bir deneme.")
#     exit()
# print(f'Girilen sayı {sayi}, {sayi_durumu} bir değerdedir.')

#todo Girilen sayılardan büyük olanın ekrana yazdırılması
# n1 = int(input("First number: "))
# n2 = int(input("Second number: "))

# if n1 > n2:
#     gross_n = n1
# elif n2 > n1:
#     gross_n = n2
# else:
#     print("Sayılar birbirlerine eşit.")
#     exit()
# print(f'Greater number between given numbers is {gross_n}')

#todo elif ve else ile Tam Karar Zinciri
# sepet_tutari = float(input("Total sepet miktarı: "))
# if (sepet_tutari >= 1000):
#     indirim = 0.2
# elif (sepet_tutari >= 500):
#     indirim = 0.1
# elif (sepet_tutari >= 250):
#     indirim = 0.05
# else:
#     indirim = 0
# odenecek_toplam = sepet_tutari - (sepet_tutari * indirim)
# print(f'Total ödenmesi gereken miktar {odenecek_toplam} kadardır')

#todo Kullanıcı etkinliğe katılma şartlarını yerine getiriyor mu? (Nested if örneği)
#* Şartlar: Kullanıcının yaşı 18 ve üzeri olmalı VE Giriş kodu doğru olmalı (1234)
# yas = int(input("Yaşınızı giriniz: "))
# sifre = int(input("Şifreyi giriniz: "))

# if (yas >= 18): #Eğer yaşı 18e eşit veya büyükse
#     if (sifre == 1234): #şifre sorduk ve 1234'e eşit mi diye kontrol ettik
#         print("İçeri girebilirsiniz.") #eşitse de giriş sağlam.
#     else: #şifre 1234 değilse
#         print("Şifre yanlış.") #şifre yanlış dedik
# else: #Eğer yaşı 18den küçükse (yani diğer tüm şartlar)
#     print("Yaşınız tutmuyor.") #yaşı tutmuyor dedik.

#* YA DA

# if (yas >= 18 and sifre == 1234): #Tek satırda da bu kod bloğunu çözebiliriz. 
#     #* ÖNEMLİ: "and" operatörü ile mantıksal ifade kurduk.
#     print("İçeri girebilirsiniz.")
# else:
#     print("İçeri giremezsiniz.")

#todo If-Elif-Else ve f-string kullanarak basit bir not ortalama hesaplayıcı yapmak.
#* Kullanıcıdan 3 farklı sınav notu (vize1, vize2, final) alınır ve float'a dönüştürülür.
# vize1 = float(input("İlk vize notu: "))
# vize2 = float(input("İkinci vize notu: "))
# final = float(input("Final notu: "))

# ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4) #Ortalama hesaplanır. Matematikteki öncelikler göz ardı edilmez.
# if(ortalama > 90): # Eğer ortalama 90 ve üstüyse:
#     print(f"Ortalamanız {ortalama:.2f} kadar ve AA ile geçersiniz.") #"AA - Başarılı"
# elif(ortalama > 70): # İlk if seçeneğini eledik, yani ortalama >90 değilse bu adıma geldik ve soruyoruz, ortalama 70'ten büyük mü?
#     print(f"Ortalamanız {ortalama:.2f} kadar ve BB ile geçersiniz.")  #"BB - İyi"
# elif (ortalama > 50): #diğer iki seçeneği eledik, yani ortalama 90dan ve 70'ten küçük. Bu koşulda 50'den büyük mü?
#     print(f"Ortalamanız {ortalama:.2f} kadar ve CC ile geçersiniz.") #Eğer öyleyse "CC - Geçer"
# else: #aksi taktirde...
#     print(f"Ortalamanız {ortalama:.2f} kadar ve FF ile kalırsınız.") #FF - Kaldı

#todo Girilen login bilgilerinin doğruluğuna göre girişin yazdırılması
# username = input("Username: ").lower() #aldığımız username'i küçük harflere çevirdik.
# password = input("Password: ") #her ikisinin string ifade olması gerek ki mukayese edilebilsin.

# if username == "beast" and password == "123": #tek satır, genelde kullanılan (hacklenme ihtimalini azaltır)
#     print("Correctly entered.")
# else:
#     print("Wrong entry.")
#* YA DA
# if username == "beast":
#     if password == "123":
#         print("Correctly entered.")
#     else:
#         print("Wrong password.")
# else:
#     print("Wrong username.")
#* Bu uygulamada hangi değeri yanlış girdiğini belirttik, hacklenme oranımızı %50 artırdık.

#todo Girilen ürünün adı: domates, biber, patlıcan ise sebze; notebook, kindle, tablet ise teknoloji; şampuan, sabun, parfüm ise kozmetik reyonu çıktısı veren uygulama
# urun_adi = input("Ürünün ismi: ").lower() #lower metodu ile gelen inputu küçük harflere çevirdik ki if bloğu içinde sıkıntı yaşamayalım
# reyon_adi = "reyon" #best practice, DONT REPEAT YOURSELF için hep :) ağaç yaşken eğilir ^^

# if urun_adi == "domates" or urun_adi == "biber" or urun_adi == "patlıcan":
#     reyon_adi = "Sebze"
# elif urun_adi == "notebook" or urun_adi == "kindle" or urun_adi == "tablet":
#     reyon_adi = "Teknoloji"
# elif urun_adi == "şampuan" or urun_adi == "parfüm" or urun_adi == "sabun":
#     reyon_adi = "Kozmetik"
# else:
#     print("Aradığınız ürün bulunmamaktadır.")
#     exit()
# print(f'Satın alınan ürün için {reyon_adi} Reyonuna gidiniz.')

#todo Alınan kitap sayısına göre indirimi yazdıran uygulama
# #* Bir kitap 5 TL
# kitap_fiyat = 5
# #* Kullanıcıdan satın aldığı kitap sayısını alalım
# kitap_sayisi = int(input("Satın alınan kitap sayısı: "))
# # Alınan kitap sayısı 1 ile 5 arasında ise yüzde 5 iskonto
# if 0 < kitap_sayisi <= 5:
#     indirim = 0.05
# # Alınan kitap sayısı 6 ile 10 arasında ise yüzde 10 iskonto
# elif 5 < kitap_sayisi <= 10:
#     indirim = 0.10
# # Alınan kitap sayısı 11 ile 15 arasında ise yüzde 15 iskonto
# elif 10 < kitap_sayisi <= 15:
#     indirim = 0.15
# # Alınan kitap sayısı 16 ile 20 arasında ise yüzde 20 iskonto
# elif 15 < kitap_sayisi <= 20:
#     indirim = 0.20
# # Alınan kitap sayısı 20'yi aşarsa hata verir.
# elif kitap_sayisi > 20:
#     print("Maximum kitap sayısını aştınız.")
#     exit()
# else:
#     print('Hesaplanamaz bir değer girildi.')
#     exit()

# odenecek_tutar = kitap_fiyat * kitap_sayisi #math beybi
# indirimli_odenecek = odenecek_tutar * (1 - indirim)

# print(f'Kitap fiyatı: {kitap_fiyat} TL\n'
#     f'İndirimsiz ödenilecek tutar: {odenecek_tutar} TL\n'
#     f'İndirim yüzdesi: %{indirim * 100}\n'
#     f'İndirim miktarı: {kitap_fiyat * kitap_sayisi * indirim} TL\n'
#     f'İndirim sonrası ödenecek tutar: {indirimli_odenecek} TL')

#todo Doğru login ile BMI hesaplayan uygulama
# username = input("Username: ").lower()
# password = input("Password: ")
# if username == "beast" and password == "123":
#     print(f'{username}, welcome!') #Bak girişi yaptık, ondan sonra devam ediyoruz koda, giriş yapamazsa bu bloğa ulaşamaz.
#     weight = float(input("Your weight in kgs: "))
#     height = float(input("Your height in cms: "))
#     BMI = weight / (height ** 2) # ** ifadesi C ailesindeki ^ anlamına geliyor, yani üssü.
#     status = ""
#     if 0 < BMI <= 18.5: # 0 < BMI and BMI <= 18.5 yerine geçer aslında, and kullanmadık ortaya aldık değeri
#         status = "Lean"
#     elif 18.5 < BMI <= 24.9:
#         status = "Normal"
#     elif 25 < BMI <= 29.9:
#         status = "Weighted"
#     elif 30 < BMI <= 34.9:
#         status = "First degree obesity"
#     elif 35 < BMI <= 39.9:
#         status = "Second degree obesity"
#     elif BMI > 40:
#         status = "Morbid obesity" 
#     else:
#         print("Wrong entry.")
#         exit()
#     #Neden exit verdim? IF BLOĞUNA DÜZGÜN GİRDİĞİ HER SENARYODA bir sonraki satırdaki PRINT fonksiyonunu YAZ DI RA CAK.
#     #Amaaaaa bu blokta value değerine bir şey atamıyorum ve değer bommmmmboş
#     #DRY prensibini uygulayabilmek için value değerine atadık ancak düzgün çalışması adına burdan çıktık.
#     print(f'User name: {username}\n' #!Sonraki satıra geçmek için \n
#             f'BMI: {BMI}\n'
#             f'Status: {status}')
# else:
#     print("Invalid credantials.")

#endregion

#region MATCH-CASE KULLANIMI

#todo Girilen günün weekday/weekend olduğunu bulan uygulama
# gun = input("Gün: ").lower()
# if gun in ("pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"):
#     match gun:
#         case "pazartesi" | "salı" | "çarşamba" | "perşembe" | "cuma":
#             print("weekday")
#         case "cumartesi" | "pazar":
#             print("weekend")
# else:
#     print("girdiyi kontrol et")

#todo Girilen trafik lambası rengine göre uygun mesaj yazdıran uygulama
# light_color = input("Light color: ")
# if light_color in ("red", "green", "yellow"):
#     match light_color:
#         case "red":
#             print("stop")
#         case "yellow":
#             print("ready")
#         case "green":
#             print("pass")
# else:
#     print("wrong entry")

#todo Girilen ayın çıktısını yazdıran uygulama
# try:
#     month = int(input("Month index: "))
#     if month in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
#         match month:
#             case 1:
#                 pass
#             case 2: 
#                 pass
#             case 3: 
#                 pass
#             case 4: 
#                 pass
#             case 5: 
#                 pass
#             case 6: 
#                 pass
#             case 7:
#                 pass
#             case 8:
#                 pass
#             case 9:
#                 pass
#             case 10: 
#                 pass
#             case 11: 
#                 pass
#             case 12:
#                 pass
#     else:
#         print("no such month")
# except (ValueError, TypeError) as err:
#     print(f"because of {err} you have to enter again.")

#endregion

#region TERNARY IF KULLANIMI

#todo Sınav sonucuna göre harf notunu yazdıran nested+ternary if yapısı
# exam_score = 85
# result = "AA" if exam_score >= 80 else "BB" if exam_score >= 60 else "CC"
# print(result)

#todo Ternary if tek/çift sayı kontrolü
# sayi = int(input("Sayıyı giriniz: "))
# print("Çift") if sayi % 2 == 0 else print("Tek")

#todo Ternary if erişkinlik durumu
# yas = int(input("Yaşınız: "))
# print("Reşit") if yas > 18 else print("Reşit değil")

#endregion

#region IF MATCH KARŞILAŞTIRMA

#todo Girilen mevsimin aylarını yazdıran uygulama.
# season = input("Season: ").lower()
#? Match Case kullanarak:
# match season:
    # case 'winter':
    #     print(f'{season} season includes: December, January, February months.')
    # case "spring":
    #     print(f'{season} season includes: March, April, May months.')
    # case "summer":
    #     print(f'{season} season includes: June, July, August months.')
    # case "autumn" | "fall" : # '|' şu ifade or anlamına geliyor.
    #     print(f'{season} season includes: September, October, November months.')
    # case _: #else ifadesi aslında
    #     print("There is no such a thing love.")
#? If-Elif-Else kullarak:
# if season == "winter":
#     print(f'{season} season includes: December, January, February months.')
# elif season == "spring":
#     print(f'{season} season includes: March, April, May months.')
# elif season == "summer":
#     print(f'{season} season includes: June, July, August months.')
# elif season == "autumn" or season == "fall":
#     print(f'{season} season includes: September, October, November months.')
# else:
#     print("There is no such a thing love.")

#todo Girilen ay ve günün hangi mevsime ait olduğunu yazdıran uygulama
# ay = input("Ayı giriniz: ").lower()

# while True:
#     #bunu 1-31 arasıda nasıl tutabilirim?
#     #gelecekten gelen Su, bunu 1-31 aralığına tutacak güncellemeyi yapıyor :')
#     gun = int(input("Ayın hangi günü: "))
#     if 1 <= gun <= 31: #aha tuttuk.
#         break
#     else:
#         print("Gün negatif veya 31'den büyük değerde olamaz. Girdinizi kontrol ediniz.")
#? IF_ELSE ve MATCH_CASE birleştirerek kullandık :)
# match ay:
#     case "ocak" | "şubat":
#         mevsim = "kış"
#     case "nisan" | "mayıs":
#         mevsim = "ilkbahar"
#     case "temmuz" | "ağustus":
#         mevsim = "yaz"
#     case "ekim" | "kasım":
#         mevsim = "sonbahar"
#     case "mart":
#         if gun >= 21:
#             mevsim = "İlkbahar"
#         else:
#             mevsim = "Kış"
#     case "haziran":
#         if gun >= 20:
#             mevsim = "Yaz"
#         else:
#             mevsim = "İlkbahar"
#     case "eylül":
#         if gun >= 22:
#             mevsim = "Sonbahar"
#         else:
#             mevsim = "Yaz"
#     case "aralık":
#         if gun >= 21:
#             mevsim = "Kış"
#         else:
#             mevsim = "Sonbahar"
#     case _: 
#         print("Böyle bir ay/gün bulunmamaktadır.")
#         exit()
# print(f'Şu anda mevsim: {mevsim}')

#endregion

#endregion

#! LOOPS: 
#* Tekrarlı işleri yaparken tercih edilen yazılım konsepti.

#? While Loop
#* Belirli bir koşul True olduğu sürece içerisindeki kod bloğunu çalıştırmaya devam eder. 
#* Ne zaman duracağını, yani sayacı veya koşulu değiştirmeyi programcının kendisi yönetmelidir.

# SYNTAX YAPISI
counter = 0 #Sayaç, çözülen problemin bağlamında başlangıç değeri ile başlar.
while counter <= 9: #Anahtar kelimesi while, ve şart kelimesi.
    print(counter)
    counter = counter + 1 #counter += 1 şeklinde de yazılabilir.
    # Koşulu değiştiren adım yazılmazsa sonsuz döngü olur

#? Sonsuz döngü
#* Bir döngünün durma koşulunun hiçbir zaman sağlanamadığı (yani koşulun sürekli True kaldığı) durumdur. İsteyerek oluşturulur.

#SYNTAX YAPISI
while True:
    print(counter) #Döngüden çıkılmadığı için sonsuza dek counter'ı yazdıracak ne olursa olsun.
    break #Döngüden çıkması için break yazılır.

#todo anket cevapları alınan uygulamada 3 kez hayır girilirse döngünün sonlandığı uygulama
counter = 0
while True:
    cevap = input("Evet/Hayır: ").lower()
    match cevap:
        case "evet":
            counter = 0
        case "hayır":
            counter += 1
            if counter == 3:
                print("Anket katılımı iptal edildi.")
                break
        case _:
            print("Girdiniz evet ya da hayır dışında, lütfen girdinizi kontrol ediniz.")

#region WHILE LOOP

#todo Girilen sayının asal olup olmadığını kontrol eden uygulama
# while True:
#     try:
#         sayi = int(input("Lütfen bir sayı giriniz: "))
#         is_asal = True
#         if sayi < 2: #2den küçük asal sayı yoktur ve negatif sayılar asal olamaz.
#             print("Negatif sayılarda asallık bakılmaz ve 2'den küçük sayılar asal değildir.")
#             break
#         else:
#             for i in range(2, sayi):
#                 if sayi % i == 0:
#                     is_asal = False
#                     break
#             if is_asal == True:
#                 print(f"Girilen sayı ({sayi}) asaldır.")
#             else:
#                 print(f"Girilen sayı ({sayi}) asal değildir.")
#     except (ValueError, TypeError) as err:
#         print(f"{err} sebebiyle hata verildi, lütfen sayıyı tekrar giriniz.")

#todo random bir sayı üretilir, 3 tahmin hakkı, tahmin sonucu ekrana yazdırılır
# from random import randint #* Random sayı üretebilmek için randint fonksiyonunu random kütüphanesinden çağırdık
# deneme = 3
# i = 1

# random_sayi = randint(a=0,b=10)
# while i <= deneme:
#     tahmini_sayi = int(input("Tahmininiz: "))
#     if tahmini_sayi ==  random_sayi:
#         print("Doğru bildiniz")
#         break
#     else:
#         print(f"{i}. hakkınız, yanlış tahmin.")
#     i += 1

# if i > deneme:
#     print(f"Deneme hakkınız bitti.\n"
#           f"Doğru tahmin: {random_sayi} olacaktı.")

#todo 0-100 arasındaki çift ve tek sayıların toplamlarının ekrana yazdırılması
# i = 0
# sum_even = 0
# sum_odd = 0

# while i <= 100:
#     if i %2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i
#     i = i + 1
# print(f'Sum of Even Numbers: {sum_even}\nSum of Odd Count: {sum_odd}')

#todo (0-100) aralığındaki sayıların ekrana yazdırılması
# i = 0 #counter olarak i, C ailesinde genelde o şekilde kullanılıyor, alıştık ^^
# while i <= 100:
#     print(i)
#     i = i + 1 #i += 1 de olur
# print("Döngü sonlandı")

#* YA DA

# i = 100
# while i >= 0:
#     print(i, end="-")
#     i -= 1 # i = i - 1 de olur
# print("Döngü sonlandı")

#endregion

#region SONSUZ LOOP

#todo anket cevapları alınan uygulamada 3 kez hayır girilirse döngünün sonlandığı uygulama
# counter = 0
# while True:
#     cevap = input("Evet/Hayır: ").lower()
#     match cevap:
#         case "evet":
#             counter = 0
#         case "hayır":
#             counter += 1
#             if counter == 3:
#                 print("Anket katılımı iptal edildi.")
#                 break
#         case _:
#             print("Girdiniz evet ya da hayır dışında, lütfen girdinizi kontrol ediniz.")

#endregion

#! LOOPS: 
#* Tekrarlı işleri yaparken tercih edilen yazılım konsepti.

#? FOR DÖNGÜSÜ
#* bir koleksiyonun elemanları üzerinde veya belirli bir sayı aralığı üzerinde sırayla ilerlemek (iterate etmek) için kullanılan döngüdür.

# SYNTAX YAPISI
isim = "Python"
# 'isim' (string) içindeki her bir harf için döngüyü çalıştır
for harf in isim: #burada harf olarak adlandırılan şey, takma/geçici isim.
    print(harf)

#todo Girilen başlangıç bitiş ve artış miktarlarına göre for döngüsü kurulumu
start = int(input("Başlangıç: "))
finish = int(input("Bitiş: "))
step = int(input("Artış miktarı: "))
for i in range(start, finish, step):
    print(i,end=" ")

#todo 0-100 arası sayıların ekrana yazdırılması uygulaması
for i in range(0,100):
    print(i, end="-")

#region FOR LOOP

#todo Bozma Testi
# Bir listenin üzerinden geçerken, o listeden eleman silmeye çalışırsak ne olur?

# sayilar = [1, 2, 3, 4, 5] #Liste tanımlandı

# for sayi in sayilar: #listedeki her bir elemanı geçerken
#     if sayi == 2: #eğer eleman 2 ise 
#         sayilar.remove(sayi) # Listeyi dönerken değiştirdik!
#     print(sayi) # ve sayıyı yazdırdık

# print("Sonuç:", sayilar) #döngüden çıktıktan sonra ise listenin tamamını yazdırdık

#çıktılar sırasıyla:
# 1
# 2 Burda 2 var ama 3 yok
# 4
# 5
# Sonuç: [1, 3, 4, 5] burda ise 3 var ama 2 yok NEDEN???

# Çünküüü
# 1. adımda, Python 0. indekste `1`'i buldu, bastı.
# 2. adımda, 1. indekste `2`'yi buldu, sildi.
# 3. adımda, Silince, arkadaki `3` sayısı kayarak `2`'nin (yani 1. indeksin) yerine geçti.
# 4. adımda, Döngü "Sıra 2. indekste" dedi ve devam etti. Ama `3` artık 1. indekste olduğu için onu **ATLADI**.

#* Bu koddan çıkartmamız gereken: Asla üzerinde iterasyon yaptığın listeyi (for döngüsü içindeyken) değiştirme! 
#* Bunun yerine listenin bir kopyasını al veya yeni bir liste oluştur.

#todo Girilen sampledaki sesli harfleri, sessiz harfleri, typoları ayrı listelere ekleyen uygulama. İlgili listelerde eleman tekrarı olmamalı. Space ignore.
sample = "buRa1k _Ayi?Lm2aZu"
# for char in sample.lower():
#     if char.isalpha():
#         if char in "aeıioöuü":
#             if char not in sesli_harfler:
#                 sesli_harfler.append(char)
#         else:
#             if char not in sessiz_harfler:
#                 sessiz_harfler.append(char)
#     else:
#         if char == " ":
#             continue #ignore attık
#         elif char not in typo_char:
#             typo_char.append(char)

# print(f"{sessiz_harfler}\n{sesli_harfler}\n{typo_char}")

#todo bu sayı aralığındaki tek sayıların ve çift sayıların toplamını yazdıran uygulama
# toplam_cift = 0
# toplam_tek = 0
# for i in range(0,100):
#     if i % 2 == 0:
#         toplam_cift += i
#     else:
#         toplam_tek += i
# print(f"Çiftlerin toplamı: {toplam_cift}\n"
#       f"Teklerin toplamı: {toplam_tek}")

#todo Girilen şifrenin min 8 karakter uzunluğunda ve boşluksuz olduğunu doğrulayan uygulama
# password = input("Please enter your password: ")
# is_valid = True
# for char in password:
#     if char == " ":
#         is_valid = False
#         msg = "gap is not accepted in passwords"
#     elif len(password) < 8:
#         is_valid = False
#         msg = "length is too short"

# if is_valid:
#     print("Your password is valid!")
# else:
#     print(msg)

#endregion

#region BOTH LOOPS

#todo 10 tane random sayı üreten uygulama
from random import randint #random sınıfından randint fonksiyonunu çağırdık.

# for i in range(1,11): #range fonksiyonunda son sayı dahil olmadığı için +1 ekledik
#     random_number = randint(a = 0, b = 100)
#     print(f'{i}. üretilen sayı = {random_number}')

#* YA DA 

# i = 0
# while i < 10:
#     random_number = randint(a=213, b=32425)
#     i += 1
#     print(f'{i}. üretilen sayı = {random_number}')

#todo Girilen sayıya kadar toplamı veren uygulama
# hedef_sayi = int(input("Kaça kadar olan sayılar toplansın: "))

# i = 0
# toplam = 0
# while i <= hedef_sayi:
#     toplam = toplam + i
#     print(f'{i}. adımdaki toplam = {toplam}')
#     i = i + 1
# print(f'istenen toplam = {toplam}')

#* YA DA

# bitis = int(input("Kaça kadar gitsin? "))
# sayi = range(1, bitis)
# toplam = 0
# for i in sayi:
#     toplam = i + toplam
#     print(f'her adımdaki toplam: {toplam}')
# print(f'sonuçtaki toplam: {toplam}')

#todo Girilen sayının faktöriyelini hesaplayan uygulama
n = int(input("Faktöriyeli hesaplanacak sayı: "))
faktoriyel = 1
i = 1

# if n > 0:
#     while i <= n:
#         faktoriyel = faktoriyel * i
#         print(f'{i}. adımdaki toplam = {faktoriyel}')
#         i = i + 1
# elif n == 0:
#     faktoriyel = 1
# else:
#     print("Faktöriyel hesabı yapılamaz.")
#     exit()
# print(f'istenen faktöriyel = {faktoriyel}')

#* YA DA

# for i in range(1, n + 1):
#     faktoriyel = faktoriyel * i
#     print(f'{i}. adımdaki toplam = {faktoriyel}')
# print(f'istenen faktöriyel = {faktoriyel}')

#endregion

#! LISTS
#* Farklı veri tiplerini tek bir yerde tutmaya yarayan veri koleksiyonlarıdır.
#* Listeler verileri kalıcı olarak depolamazlar, listeler RAM'de depolanır.
#* LİSTELER DEĞİŞTİRİLEBİLİR (MUTABLE) BİR VERİ KOLEKSİYONUDUR

#SYNTAX YAPISI
meyveler = ["elma", "muz", "kiraz"]
karisik_liste = [10, "Merhaba", 3.14, True] #burdan öğrenmemiz gereken şu, listelerde FARKLI VERI TİPLERİ AYNI ANDA DEPOLANABİLİR!!

#? Index Nedir, nasıl çalışır
#* Index, bir listedeki her bir öğenin konumunu belirten sayısal etikettir. 
#* Listeler sıralı olduğu için, her öğenin sabit bir konumu vardır.
#* Negatif indeksleme ile listenin son öğesine -1. elemanı ile ulaşabildiğimizi gösterir.

#SYNTAX OLARAK GÖSTERİMİ
isimler = ["Ali", "Burak", "Cem", "Deniz"]
# Index:    0       1       2        3
# Negatif: -4      -3      -2       -1

print(isimler[0])   # Çıktı: Ali (İlk öğe)
print(isimler[3])   # Çıktı: Deniz
print(isimler[-1])  # Çıktı: Deniz (Son öğe)

#region Nested List
#? Nested List Yapısı
#* Liste içerisinde liste yapısıdır, en basit anlatımıyla matematikteki matriks yapısı gibi düşün.

alisveris_sepeti = [
    "Ekmek",                        # 0. indexteki Tekil Ürün
    "Süt",                          # 1. indexteki Tekil Ürün
    ["Elma", "Muz", "Portakal"],    # 2. indexteki öğeler (Meyveler Kutusu)
    ["Kalem", "Silgi"],             # 3. indexteki öğeler (Kırtasiye Kutusu)
    15.99                           # 4 indexteki ürün (fiyat)
]
# alisveris_sepeti listesi 5 öğeye sahiptir ve 2 ve 3. indexteki öğeler de ayrıca listelerdir.
print(alisveris_sepeti[2][2]) #Listenin 2. indexteki elemanının 2. indexindeki elemanını yazdır.
#endregion

#region Dilimleme
#? Slicing (Dilimleme) Operatörü
#* Pandas (veri analizinde de) kullanılır, çok önemli!!!!
#* Mevcut bir SIRALI YAPININ belirli bir bölümünü alarak YENİ BİR YAPI oluşturma işlemidir. 
#* Bu dilimleme orjinal listeyi değiştirmez.

#SYNTAX YAPISI
#           yeni_liste = eski_liste [başlangıç_index(DAHİL) : bitiş_index(HARİÇ) : adım] 
#             default değerleri --- [       0 (SIFIR)       :    listenin_sonu   :  1  ]

fruits = [
    "Apple", "Banana", "Orange", "Mango", "Pineapple",
    "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
    "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
    "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
]

print(fruits[2:7]) #birinci değer başlangıç indexi, ikinci değer n-1 olacak şekilde kapanış indexi
print(fruits[:3]) #burada başlangıç belirtilmedi yani başlangıç 0 ve burada : ile 3.ye kadar diyoruz
print(fruits[1::2]) #birden başla, iki iki zıplayarak git demek çift iki nokta ile 
print(fruits[::4]) #gene başlangıCı vermedi ama 4er 4er zıplayarak git anlamına geldi 

print(fruits[::-1]) #0dan başla, -1 -1 git dedik ve aslında listeyi tersine çevirmiş olduk. 
# eksi koyunca reverse ediliyor gibi düşün, 0. eleman direkt son eleman gibi düşün
print(fruits[10::-3]) #başlangıç verdik diye burda reverse düşünme, 10. elemandan başla geriye doğru 3er adımla git
print(fruits[::-2])
#endregion
