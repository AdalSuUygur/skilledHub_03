


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

# 22 12 2025
#ders 23
# pazartesi

#fonksiyonlara giriş yaptık önceki derste

#fonksiyonlar devamlı aynı işi yapan yapılara denir

# def greeting_people(): #parametre almayan fonks.
#     print("Hello!")
# greeting_people #fonksiyonu çağırmak

# def greeting(full_name: str): #parametre alan fonks.
#     print(f"Hello, {full_name}!")
# greeting(full_name="Adal") #fonksiyonu çağırmak
# #burda ise greeeting() yazıp bir içerik göndermezsek patlar

# def greeting_default(full_name: str = "User"): #parametre alan ve default değeri olan fonks
#     print(f"Hello, {full_name}!")
# greeting() #fonksiyonu çağırmak burda değer girilmediyse default değer gelir
# greeting(full_name="Adal") #bu şekilde yaparsak da üstüne yazar bizim girdiğimiz değeri

# #fonksiyonları define ettik
#fonksiyonları çağırmak

#clean code için fonksiyon yazılmalı
#merkeziyetçilik için yine

#? returnable fonksiyonlar yani değer döndüren fonksiyonlar
# çalışcak, işi bitince değer dönücek, biz de o değeri alıp başka yerde kullanabileceğiz.
# ben burda yapılan iş sonucunda elde edilen değeri alıp başka yerde kullanacak mıyım? evet ise returnable fonksiyon

# def pow_number(x: int = 1, pow: int = 1) -> int: # -> int demek bu fonksiyon integer olarak dönecek demektir.
#     """Bir tam sayının kuvvetini hesaplayan fonksiyon
#     Args:
#         x(int): Kuvveti alınacak sayı, integer
#         pow(int): kuvvet değeri, integer

#     Returns:
#         int: sonuç
#     """
#     return x ** pow
# #return altında kalan kodlar çalıştırılmaz.

# #return edilen değişkeni bir değişkene atamamız lazım

# result = pow_number(x=2,pow=9)
# print(result)

#* inputlar fonksiyonun içinde olmaz, neden? çünkü değerler dışarıdan geliyor, içerde tanımlanmıyor gibi düşün.

#todo ısınma sorusu
#* kullanıcıdan alınan 3 adet sayıyı toplayan fonksiyon

# def addition(x: int = 0, y: int= 0, z:int= 0) -> int:
#     return x+y+z

# toplam = addition(x=8, y= 15, z=-3)
# toplam = addition(
#     x= int(input("İlk sayi: "))
#     y= int(input("İkinci sayi: "))
#     z= int(input("Üçüncü sayi: "))
# ) #diye burada da istenebilir değerler

# print(toplam)

#todo bir söz öbeğindeki tekrar eden kelimelerden arındırarak string formatında çıktı veren fonksiyonu yazınız
#* hint: 

# sample_input = "merhaba ben burak burak ben merhaba merhaba burak burak burak"

# def remove_duplicate_word(sentence: str) -> str:
#     #path i - junior çözümü
#     lst = [] #geçici liste
#     for item in sentence.split():
#         #kelime kelime dolaşır
#         if item not in lst:
#             lst.append(item)
    
#     str_output = " ".join(lst)
#     return str_output


    # #path ii - 
    # lst_1 = [item for item in sentence.split()]
    # lst_2 = set(lst_1)
    # str_output = " ".join(lst_2)
    # return str_output

    # #path iii
    # return " ".join(set([item for item in sentence.split()]))

# result = remove_duplicate_word(sample_input)
# print(result)

#todo araaaa
#* daha kaliteli kod yazmak
#* daha okunabilir kod yazmak
#* debug edileibilir kod yazmak

#* 2 adet yazılım presibi:
#* single responsibility principle (SRP): bir fonksiyonun sadece bir görevi olur diyor
#ki o fonksiyonu ikidebir değiştirmek zorunda kalmayalım.
#birden fazla görevi olan fonksiyonları sürekli değiştirmek gerekir
#böl parçala yönet :D
#maintaince için.

#* ve Seperation of concern (SOC): sıkıntılarını parçala demek

#todo kullanıcıdan rastgele üretilecek sayı miktarını alalım
#çift olanları even_lst'ye tek olanları odd_lst'ye ekleyerek çıktı verelim

#path kendi çözümüm
# from random import randint

# def num_generator(input: int = 0, start_point: int = 0, end_point: int = 0) -> list:
#     return [randint(a=start_point, b=end_point) for number in range(input)]

# def even_odd_seperator(input_lst: list) -> list:
#     even_lst = [item for item in input_lst if item % 2 == 0]
#     odd_lst = [item for item in input_lst if item % 2 != 0]
#     return [even_lst, odd_lst]

# sayi_urettik = num_generator(15, 0, 100)
# deneme = even_odd_seperator(sayi_urettik)

# print(deneme)

#hocanın çözümü

from random import randint
def number_generator(amount: int, start_point: int, end_point: int) -> list:
    return [randint(a=start_point, b=end_point) for _ in range(amount)]

def find_even_odd(number_lst: list[int]):
    even_lst = []
    odd_lst = []
    for number in number_lst:
        if number % 2 == 0:
            even_lst.append(number)
        else:
            odd_lst.append(number)

    return even_lst, odd_lst

no_generator = number_generator(amount=10, start_point=0, end_point=9)
print(no_generator)
even_list, odd_list = find_even_odd(number_lst=no_generator)
print(even_list)
print(odd_list)

#todo ödev:
#* 1 sign in ve sign up
#* sign up işleminde kullanıcının girdiği password valid mi, user_name unique mi? e_mail valid mi?
#* bu kurallardan geçerse üyelik işlemi tamamlanacak
#* sign inta da yine pass word doğru mu bu sefer, e-mail ve password doğruysa giriş yap
#* veri yapısı: 
#* aşağıda sample data structure

users = {
    "xyz.xyz@skilledhub.com": "şifresineyse artık",

    }

#todo ödev:
# 100 tane rakamlardan oluşan bir liste generate edelim
#bu liste içerisinde bulunan rakamların geçme sıklığını bulan ve aşağıdaki yapıda return eden fonksiyonu yazın

{
    1: 10, #1den 10 tane üretti
    2: 30, #2den 30 tane üretti
    3: 5 #yani hangi sayıdan kaç tane üretildi :D
}

#Counter ile de yapabilirimmmmmm

#bilmediğimiz kadar parametre gelince ne yapalım? *args vs **kwargs içerisinde çözücez, perşembe günün konusu

#tüm bu problem main() fonksiyonu içinde çalışacak. parametresi yok. Tüm iş burda olcak, kod bloğu
#yani:
def main():
    pass

main() #execute edicez burda

# while True:
#     try:
#         rakam_1 = int(input("rakam giriniz islem icin: "))
#         rakam_2 = int(input("rakam giriniz islem icin: "))
#         islem_type = input("islem novu giriniz : ('+' ,'/' , '*' , '-'")

#         match islem_type:
#             case "+":
#                 print(f'toplama islemi sonucu: {rakam_1 + rakam_2}')
#             case "-":
#                 print(f'cikma islemi sonuc: { rakam_1 - rakam_2}')
#             case "/":
#                 print(f'bolme islem sonucu : {rakam_1 / rakam_2}')
#             case "*":
#                 print(f'carpma sonucu : {rakam_1 * rakam_2}')
#             case _:
#                 print("boyle bir islem type yok..!!")  
#     except ValueError as hata:
#         print("rakam girmeniz gerekli..!!") 
#         print("hata:" ,  hata ) 

#         break
#     else:
#         print("girisiniz iptal oldu isim , soyisim , passwordunuzu dogru giriniz..!!")
#         deneme_sansi -= 1

# aranan = 5
# i = 0
# while i < 4:
#     if i == aranan:
#         print("Bulundu!")
#         break # Break ile çıktığı için else çalışmayacak.
#     i += 1
# else:
#     print("Döngü bitti ama aranan sayı bulunamadı.") 
#     # Eğer break hiç çalışmazsa burası devreye girer.