


# # 18 12 25 - ders notları
# #ödev çözümü

# # özlemin çözümü

# # author_name = input("Auther name:")
# # articles = []
# # for article in data["articles"]:
# #     author = article.get("author")
    
# #     if author and author_name.lower() in author.lower():
# #         articles.append(article)
# # if articles:
# #     print(f"\nArticles by {author_name}:\n")
# #     for art in articles:
# #         print(art["title"])



# #hoca çözdü ama anlamadım, şimdi functions kısmına geçiyoruz

# #! Custom Functions

# #Artık kod blokları lineer olarak çalışmayacak
# #Yazacağımız kodları fonksiyon olarak yazmaya başlayacağız
# #Artık yukarı çıkacağız aşağı ineceğiz, başka dosyaya gidip farklı bir şey çağırabilecek vs.
# #Artık functional programming kısmına geçiyoruz.

# #custom yazdığımız fonksiyonları da istediğimiz zaman istediğimiz yerde çağırıp kullanıcaz
# #fonksiyon nedir
# #avantajları neler
# #dezavantajları neler
# #neden kullanılır vs vs

# #fonksiyon declate/define etme (tanıtma)

# #def anahtar sözcüğü ile :
# def greeting_people(): #fonksiyon tanımlıyorum demek def, yaptığı iş ile alakalı da isimlendirme yapmak lazım

#     print("Hello World!")
# #artık tanımlandı

# #şimdi ne zaman fonksiyon çalıştırılacak o zaman fonksiyon execute edilmiş olcak
# greeting_people()
# greeting_people()
# #bu da execution kısmı
# #artık istediğim yerde istediğim kadar kullanabilirim


# #1. Bunu yapabilmek için 1 autodocs extenionı kurulumu olmalı
# #2. 3 kere konsol tuşuna tıkla
# def sum_two_number(a: int, b: int):
#     """Bu fonksiyon 2 tane tam sayı toplar.

#     Args:
#         a (_type_): integer tipinde tam sayı
#         b (_type_): integer tipinde tam sayı
#     """
#     print(a+b)

# sum_two_number(a=2, b=4) #a= ve b= kısmındaki değerlere parametre/argüman??? diyoruz, değerleri alıyorlar ve fonksiyona taşıyorlar ve 

# #farklı kullanımı
# # sum_two_number_input(
# #     a = int(input("tam sayi: ")),
# #     b = int(input("tam sayı: ")),
# # )

# #todo örnek full name ve domain name alalım, kurumsal mail adresi craft

# # full_name = input("Lütfen isminizi giriniz: ")

# # def crafting_mail(name: str):
# #     domain_name = "@outlook.com"
# #     lst_name = name.split(" ")
# #     print(f"{lst_name[0]}.{lst_name[-1]}{domain_name}")

# # crafting_mail(name= full_name)

# #hocanın çözümü
# #1. adım, function decleraation

# def create_email(full_name: str, domain_name: str): #2 tane inputa ihtiyacımız var, birisi isim diğeri domain name
#     names = full_name.lower().split(" ")
#     print(f"Mail adresses: {names[0]}.{names[-1]}{domain_name}")

# create_email(full_name="adal su uygur", domain_name="@outlook.com")

# #firmanın kurumsal mail adresi sabittir.
# #default değeri olacak parametrelere tip geçtikten sonra yanına eşittir koyup değer geçebiliyoruz.
# #örnek:

# def create_mail(full_name: str, domain_name: str = "@skilledHub.com"): #buraya default değer verdim diye bunu ezemeyeceğim anlamına gelmiyor
#     names = full_name.lower().split(" ")
#     print(f"Mail adresses: {names[0]}.{names[-1]}{domain_name}")

# #bu ezmediğimiz değerli hali
# create_mail(full_name="adal su uygur")

# #bu da ezdiğimiz değerli hali
# create_mail(full_name="adal su uygur", domain_name="@xyz.com")

# #default değer vermek bize opsiyon da sağlar.

# #todo 3 sayıyı çarpan bir fonksiyon yaz, burdaki çıkarım default değerlerin önemi

# def multiply(number_1: float = 1, number_2: float = 1, number_3: float = 1):
#     print(number_1 * number_2 * number_3)

# multiply(12,24) #böyle yazınca patlamasın diye default değer tanımlıyoruz

# #missing parametre patlamasını da gördük

# #todo dairenin alanı hesaplayan fonksiyon

# def area_circle(radius: int = 1, pi: float = 3.1415):
#     area = (radius ** 2) * pi
#     print(area)

# area_circle(radius= 3)

# #hocanın çözümü
# #bir parametreye birden fazla tip gelebilir, int tanımlanmış olan radius float da olabilir

# def calculate_area_disk(radius: int | float, pi = 3.1415):
#     """
#     Docstring for calculate_area_disk
    
#     :param radius: Description
#     :type radius: int | float
#     :param pi: Description
#     """
#     print(radius**2 * pi)

# calculate_area_disk(3)

# #fonksiyon nedir
# #parametreler nedir
# #returnable ve unreturnable fonksiyonların karşılaştırılması
# # *args vs *kwargs
# # decorator

### 🚀 HARDCORE UYGULAMA: VKİ (BMI) Analizörü

# Şimdi öğrendiklerini birleştirme zamanı. Sıra sende!

# Senden **Vücut Kitle İndeksi** hesaplayan ve sonucu yorumlayan bir program istiyorum.

# # **Gereksinimler:**

# # 1. Kullanıcıdan `kilo` (kg) bilgisini al (float).
# # 2. Kullanıcıdan `boy` (metre) bilgisini al (float). (Örn: 1.75)
# # 3. **Formül:** `vki = kilo / (boy ** 2)`
# # 4. **Karar Ağacı:**
# # * VKİ < 18.5 ise: Ekrana **"Zayıf"** yazsın.
# # * 18.5 ile 24.9 arasında ise: **"Normal"** yazsın.
# # * 25 ile 29.9 arasında ise: **"Fazla Kilolu"** yazsın.
# # * 30 ve üzeriyse: **"Obez"** yazsın.



# # Kodunu yaz, buraya yapıştır, inceleyip "Code Review" yapalım. Sonra LeetCode sorusuna geçeceğiz! 💻☕️

# kilo = float(input("Kilo: "))
# boy = float(input("Boy: "))
# if boy == 0:
#    print("Lütfen 0'dan farklı bir değer giriniz.")
# else:
#    vki = kilo / (boy ** 2)

# if vki < 18.5:
#     print("Zayıf")
# elif 18.5 <= vki < 24.9:
#     print("Normal")
# elif 25 <= vki < 29.9:
#     print("Fazla kilolu")
# elif vki > 30:
#     print("Obez")



# While - Else (Python'un Gizli Silahı)
#               hocaya sormakta fayda var


# Bilgisayar 1-100 arası bir sayı tutsun. Sen bulmaya çalış.

# Kütüphane: import random -> sayi = random.randint(1,100)

# while True kullan.

# Kullanıcıya ipucu ver: "Daha büyük gir", "Daha küçük gir".

# Kullanıcı doğru bilirse break yap ve kaçıncı denemede bildiğini yaz.

# QA Dokunuşu: Kullanıcı "çıkış" yazarsa oyunu nazikçe kapat (q tuşu).

# from random import randint

# sayi = randint(a=1, b=100)
# deneme = 0

# while True:
#     tahmin_sayi = int(input("Sayı tahmini: "))
#     deneme += 1
#     if tahmin_sayi < sayi:
#         print("Daha büyük gir")
#     elif tahmin_sayi == sayi:
#         print(f"Bravo! {deneme}. denemenizde bildiniz!")
#         break
#     elif tahmin_sayi > sayi:
#         print("Daha küçük gir")
#     else:
#         print("Program kapatılıyor.")
#         break


# sayilar = [1, 2, 3, 4, 5]

# for sayi in sayilar:
#     if sayi == 2:
#         sayilar.remove(sayi) # Listeyi dönerken değiştirdik!
#     print(sayi)

# print("Sonuç:", sayilar)





toplam_maliyet = 0
maaslar = [20000, 30000,40000,50000,25000,15000]

for maas in maaslar:
    if maas < 20_000:
        yeni_maas = maas * 1.2
    yeni_maas = maas * 1.1
    print(f"Yeni maaş: {yeni_maas}")
    toplam_maliyet += yeni_maas
print(f"Şirketin toplam ödemesi: {toplam_maliyet} TL")

