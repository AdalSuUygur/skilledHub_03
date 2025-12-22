
#! Custom Functions
#* Fonksiyonlar, devamlı aynı işi yapan yapılara denir.
#* Bu kod blokları programın istenilen herhangi bir yerinde çağırılmasını sağlar ve kodlarımız lineer olarak çalışmaz.
#* Bu da fonksiyonel programming olur. Clean coding felsefesine de uygundur.

# #custom yazdığımız fonksiyonları da istediğimiz zaman istediğimiz yerde çağırıp kullanıcaz
#? SYNTAX
#* Fonksiyonu tanıtmak/define etmek için "def" anahtar sözcüğü kullanılır.

def greeting_people(): #def ile "greeting_people" adlı fonksiyonu tanıttık.
    print("Hello World!") #artık fonksiyonumuz tanımlandı ve işini yapıyor.

#* Fonksiyonu programın herhangi bir yerinde çağırmak için fonksiyonun execute edilmesi gerek.
greeting_people() #bu da execution kısmı.
# Artık bu tanımlanmış fonksiyonu istediğim yerde istediğim kadar kullanabilirim

#? Parametre alan, almayan ve default değeri olan fonksiyonlar:
def greeting_people(): # Parametre almayan fonksiyon
    print("Hello!")
greeting_people # fonksiyonu çağırmak/execute etmek.

def greeting(full_name: str): # Parametre alan fonksiyon
    print(f"Hello, {full_name}!")
greeting(full_name="Adal") # fonksiyonu çağırmak/execute etmek.
# Burada ise greeeting() yazıp bir içerik göndermezsek patlar.

def greeting_default(full_name: str = "User"): #parametre alan ve default değeri olan fonks
    print(f"Hello, {full_name}!")
greeting() # fonksiyonu çağırmak/execute etmek. Burda değer girilmediyse default değer gelir.
greeting(full_name="Adal") # Bu şekilde default değerin üzerine yazarsak da default değer ezilir ve en son yazılan gelir.

#? Fonksiyonlarda tanımlama yapmak:
#* Bunu yapabilmek için 1 autodocs extension'ı kurulumu olmalı

# 1. Adım: Fonksiyon tanımla:
def generate_docs(a: int, b:int):
    # 2. Adım: 3 kere konsol tuşuna tıkla.
    """Bu fonksiyon 2 tane tam sayı toplar.
    Args:
        a (_type_): integer tipinde tam sayı
        b (_type_): integer tipinde tam sayı
    """
    # 4. Adım: gelen Docstring'i seç.
    # 5. Adım: İçeriğini uygun şekilde doldur.
    print(a+b)

#region Examples
#todo FullName ve DomainName olan data ile kurumsal mail adresi craft etmek
# full_name = input("Lütfen isminizi giriniz: ")

# def create_email(full_name: str, domain_name: str): #2 tane inputa ihtiyacımız var, birisi isim diğeri domain name
#     names = full_name.lower().split(" ")
#     print(f"Mail adresses: {names[0]}.{names[-1]}{domain_name}")

# create_email(full_name="adal su uygur", domain_name="@outlook.com")
# #firmanın kurumsal mail adresi sabittir.

# #default değeri olacak parametrelere tip geçtikten sonra yanına eşittir koyup değer geçebiliyoruz.
# def create_mail(full_name: str, domain_name: str = "@skilledHub.com"): #buraya default değer verdim diye bunu ezemeyeceğim anlamına gelmiyor
#     names = full_name.lower().split(" ")
#     print(f"Mail adresses: {names[0]}.{names[-1]}{domain_name}")

# #bu ezmediğimiz değerli hali
# create_mail(full_name="adal su uygur")

# #bu da ezdiğimiz değerli hali
# create_mail(full_name="adal su uygur", domain_name="@xyz.com")

#todo 3 sayıyı çarpan bir fonksiyon
#* Burdaki çıkarım: default değerlerin önemi
# def multiply(number_1: float, number_2: float, number_3: float):
#     print(number_1 * number_2 * number_3)
# multiply(12,24) # Burada eksik argüman gönderdik ve çalıştırmaya çalıştığımızda patladık.
# # Patlamasının sebebi: Missing Parameter

# def multiply(number_1: float = 1, number_2: float = 1, number_3: float = 1):
#     print(number_1 * number_2 * number_3)
# multiply(12,24) # Bu şekilde eksik argüman gönderdiğimizde program patlamasın diye default değer tanımlıyoruz

#todo dairenin alanı hesaplayan fonksiyon
#* Burdaki çıkarım: bir parametreye birden fazla tip gelebilir.

# def calculate_area_disk(radius: int | float, pi = 3.1415): #radius değeri hem int olabilir hem de float olabilir.
#     """
#     Docstring for calculate_area_disk
    
#     :param radius: Description
#     :type radius: int | float
#     :param pi: Description
#     """
#     print(radius**2 * pi)
# calculate_area_disk(3)
#endregion

#? Returnable (Değer Döndüren) Fonksiyonlar
#* Fonksiyon çalışacak, ve çalışması tamamlandığında bir değer dönecek.
#* Dev ile bu değeri alıp farklı bir yerde kullanacak.

def pow_number(x: int = 1, pow: int = 1) -> int: # -> int demek bu fonksiyon integer olarak dönecek demektir.
    """Bir tam sayının kuvvetini hesaplayan fonksiyon
    Args:
        x(int): Kuvveti alınacak sayı, integer
        pow(int): kuvvet değeri, integer
    Returns:
        int: sonuç
    """
    return x ** pow # x üzeri pow değeri dönecektir.
#return altında kalan kodlar çalıştırılmaz.

#Burada built-in fonksiyon yapılarındaki gibi, return edilen değeri bir değişkene atamamız lazım.
result = pow_number(x=2,pow=9)
print(result)

#* Not: Inputlar fonksiyonun içinde olmaz, neden? Çünkü değerler dışarıdan geliyor, içerde tanımlanmıyor gibi düşün.

#region Examples

#todo Kullanıcıdan alınan 3 adet sayıyı toplayan fonksiyon

# def addition(x: int = 0, y: int= 0, z:int= 0) -> int:
#     return x+y+z
# toplam = addition(
#     x= int(input("İlk sayi: ")),
#     y= int(input("İkinci sayi: ")),
#     z= int(input("Üçüncü sayi: "))) #diye burada da istenebilir değerler
# print(toplam)

#todo Verilen cümleden tekrar eden kelimelerden arındırarak string formatında çıktı veren fonksiyon
sample_input = "merhaba ben adal adal ben merhaba merhaba adal adal adal"

def remove_duplicate_word(sentence: str) -> str:
    #* Path I - junior çözümü
    # lst = [] #geçici liste
    # for item in sentence.split():
    #     #kelime kelime dolaşır
    #     if item not in lst:
    #         lst.append(item)
    
    # str_output = " ".join(lst)
    # return str_output

    #* Path II - Senior çözümü
    # lst_1 = [item for item in sentence.split()]
    # lst_2 = set(lst_1)
    # str_output = " ".join(lst_2)
    # return str_output

    #* Path III - Cool jojuq çözümü
    return " ".join(set([item for item in sentence.split()]))

result = remove_duplicate_word(sample_input)
print(result)

#todo Rastgele üretim aralığı verilen sayıları verilen miktarda ürettiren fonksiyon
# from random import randint

# def number_generator(amount: int, start_point: int, end_point: int) -> list:
#     return [randint(a=start_point, b=end_point) for _ in range(amount)]

# def find_even_odd(number_lst: list[int]):
#     even_lst = []
#     odd_lst = []
#     for number in number_lst:
#         if number % 2 == 0:
#             even_lst.append(number)
#         else:
#             odd_lst.append(number)
#     return even_lst, odd_lst

# no_generator = number_generator(amount=10, start_point=0, end_point=9)
# print(no_generator)
# even_list, odd_list = find_even_odd(number_lst=no_generator)
# print(even_list)
# print(odd_list)

#endregion
