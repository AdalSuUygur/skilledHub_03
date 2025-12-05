

#! 04_lists ve 05_lists examples tekrar çöz
#! small projects içindeki benchmarkı tekrar çöz, anla, gerekirse diğer projelerede benchmark ekle

# # #todo Login bilgileri eşleşirse, ürün search ve fiyat output.
# # #todo Yanlış loginde yeni kayıt. username'ler unique
# # #bütün ürünlerin toplam fiyatı nedir
# # #ürün adı laptop olan ürünlerin fiyatlarını toplayalım
# # #kullanıcı ürün search edebilsin, yani ürün search etti monitör yazdı varsa fiyatını verdi
# # #fiyatı 200 tl altında olan ürünler listelensin
# # #register olsun, yani kayıt da olsun; username varsa hali hazırda ekleyemesin
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


#region benchmark testing

#todo generate ile numbers listesini kur (liste olmayacak haliyle.)
#todo Benchmark testing between listComprehension / lambdaFilter / forLoop
#Random sayılardan oluşan bir liste üretilir (a=-100, b=100)
#Path1 ile list comprehension, Path2 ile lambda filter, Path3 ile for loop ile pozitif sayılar ayıklanır.
#Bu pathler arasında benchmark testi yapılır.

from random import randint #random sayı üretmeye yarayan fonksiyon
import tracemalloc #memory hesabı için kullanacağız
import time #nanosecond olarak ölçmeye yarayan fonksiyon
from time import time_ns
import sys

ADET = 1_000_000 
print(f"{ADET} adet sayı üretiliyor, lütfen bekleyiniz")
# Sayı üretme süresini teste dahil etmiyoruz, o yüzden dışarıda yapıyoruz.
numbers = (randint(a=-100, b=100) for i in range(ADET))#[randint(a=-100, b=100) for i in range(ADET)]
#numbers_with_generate = (randint(a=-100, b=100) for i in range(ADET)) #liste olarak tanımlamadık ve memory tüketimi azaldı
print("Sayılar üretildi, yarış başlıyor!\n" + "-"*50)


# --- PATH 1: List Comprehension ---
timer_start = time_ns() # Kronometreyi başlat

path_1 = [number for number in numbers if number > 0]
#print(path_1) #test

timer_finish = time_ns() # Kronometreyi durdur
sure_path1 = timer_finish - timer_start

size_path1 = sys.getsizeof(path_1) # Bellek Boyutu Ölçümü

print(f"Path 1 (List Comp) : {sure_path1:,} ns") #Okunabilirlik için binlik ayırıcı (,)
print(f"  Bellek Boyutu (Tahmini): {size_path1:,} byte")

del path_1 # Belleği serbest bırak


# --- PATH 2: Filter + Lambda ---
timer_start = time_ns() # Kronometreyi başlat

path_2 = list(filter(lambda x: x>0, numbers))
#print(path_2) #test

timer_finish = time_ns() # Kronometreyi durdur

sure_path2 = timer_finish - timer_start
size_path2 = sys.getsizeof(path_2) # Bellek Boyutu Ölçümü

print(f"Path 2 (Filter)    : {sure_path2:,} ns")
print(f"  Bellek Boyutu (Tahmini): {size_path2:,} byte")

del path_2


#PATH3 for loop
timer_start = time_ns() # Kronometreyi başlat

path_3 = []
for number in numbers:
    if number > 0:
        path_3.append(number)
#print(path_3) #test

timer_finish = time_ns() # Kronometreyi durdur
sure_path3 = timer_finish - timer_start

size_path3 = sys.getsizeof(path_3)

print(f"Path 3 (For Loop)  : {sure_path3:,} ns")
print(f"  Bellek Boyutu (Tahmini): {size_path3:,} byte")
del path_3


print("-" * 30)


en_hizli = min(sure_path1, sure_path2, sure_path3)
if en_hizli == sure_path1: print("KAZANAN: Path 1 (List Comprehension)")
elif en_hizli == sure_path2: print("KAZANAN: Path 2 (Filter)")
else: print("KAZANAN: Path 3 (For Loop)")
#endregion

#todo Girilen data sheetten ilkisim.soyisim@outlook.com şeklinde mail_adresses üretilip ekrana yazdırılan uygulama.
#* İpucu1: split() fonksiyonu
#* İpucu2: bir listenin uzunluğu ne olursa olsun son elemanına nasıl ulaşırım
users = ["Burak Yılmaz", "Adal Su Uygur", "Yasemin Uygur Erdem", "Sami Lütfü Esen Berk"]

#region Kendi denemem2
mail_addresses = []
mail_uzantisi = "@outlook.com"

for user in users:
    name_slices = user.split(" ")
    ilkisim = name_slices[0]
    soyisim = name_slices[-1]
    mail_addresses.append(f"{ilkisim}.{soyisim}{mail_uzantisi}")
print(mail_addresses)
#endregion YAPTIM KIZ

#region Kendi denemem1

users_splited = users.split(" ")
mail_adress = []

for user in users:
    user = user.lower()
    name_piece = user.split(" ")
    first_name = name_piece[0]
    last_name = name_piece[1]

#endregion

#region Hocanın çözümü

users = ['Burak Yılmaz', 'Rana Nur Ceylan', 'İpek Yılmaz', 'kerim Abdurrahman Burak Yılmaz']
mail_addresses = []
domain_name = "@outlook.com"
for user in users:
    user_names = user.lower().split(" ")
    mail_address = (f"{user_names[0]}.{user_names[-1]}{domain_name}")
    mail_addresses.append(mail_address)
print(mail_addresses)
#endregion

#todo Girilen sampledaki sesli harfleri, sessiz harfleri, typoları ayrı listelere ekleyen uygulama. İlgili listelerde eleman tekrarı olmamalı. Space ignore.
sample = "buRa1k _Ayi?Lm2aZu"
sesli_harfler = []
sessiz_harfler = []
typo_char = []
space_char = []

#region kendi çözümüm

for char in sample.lower():
    if char.isalpha():
        if char in "aeıioöuü":
            if char not in sesli_harfler:
                sesli_harfler.append(char)
        else:
            if char not in sessiz_harfler:
                sessiz_harfler.append(char)
    else:
        if char == " ":
            continue #ignore attık
        elif char not in typo_char:
            typo_char.append(char)

print(f"{sessiz_harfler}\n{sesli_harfler}\n{typo_char}")
#endregion YAPTIKKKKKK

#region Hocanın çözümü

word = input("Type something: ")

for ch in word.lower():
    if ch.isalpha(): #karakter alfabetik mi diye bakıyoruz.
        if ch not in sesli_harfler and ch not in sessiz_harfler:
            if ch in "aeıioöuü":
                sesli_harfler.append(ch)
            else:
                sessiz_harfler.append(ch)
    else:
        if ch == " ":
            continue
        typo_char.append(ch)

print(sesli_harfler)
print(sessiz_harfler)
print(typo_char)
#endregion


# todo is password valid uygulaması
# min 16 karakter
# min 1 büyük 1 küçük harf
# min 1 noktalama işareti
# min 1 rakam
# hint: string kütüphanesi noktalama işaretleri hazır olarak var

# region kendi deneme başlangıcım da tam oturmadı kafama
# password = input("şifre: ")
# #sample PWD: beast?Beast1beast

# is_karaktersiniri = len(password)
# is_kucukharf = any(char.isupper for char in password)
# is_buyukharf = any(char.isupper for char in password)
# is_noktalamaisareti = any(char.ispuncti for char in password)
# is_rakam = any(char.isupper for char in password)
# endregion

# region hocanın çözümü
# from string import punctuation

# password = input('Password giriniz: ')

# if len(password) < 16:
#     print("invalid password")
# if not any(ch.isupper() for ch in password):
#     print("invalid password")
# if not any(ch.islower() for ch in password):
#     print("invalid password")
# if not any(ch.isdigit() for ch in password):
#     print("invalid password")
# if not any(ch in punctuation for ch in password):
#     print("invalid password")


# #*logic mantığı

# if (
#     len(pwd) < 16 and
#     not any(ch.isupper() for ch in pwd)
#     #and ile bağlayıp herhangi bir şey
# ):
#     print()

# endregion

# region hasan çözümü
# import string
# password = input("Şifreyi gir: ")
# uzunluk = len(password) >= 16
# b_harf  = any(ch.isupper() for ch in password)
# k_harf  = any(ch.islower() for ch in password)
# rakam  = any(ch.isdigit() for ch in password)
# noktalama = any(ch in string.punctuation for ch in password)

# if uzunluk and b_harf and k_harf and rakam and noktalama:
#     print("Şifre geçerli.")
# else:
#     print("Şifre geçersiz.")
#     if not uzunluk:
#         print("16 karakterden az olamaz.")
#     if not b_harf:
#         print(" büyük harf içermeli.")
#     if not k_harf:
#         print(" küçük harf içermeli.")
#     if not rakam:
#         print("rakam içermeli.")
#     if not noktalama:
#         print(" özel karakter içermeli.")  
# print(f"Girilen şifre: {password}")
# endregion

#todo Login, 3 yanlış hak, try-except & match-case & infinitive loop kullanımı isteniliyor. Login yapıldığında hesap makinesine ulaşılacak.

#region Hopefully last try ^^ (28.11.25) **DRY prensibine uyamadım. Will try again!

username = "adal"
password = "123"
#isim ve şifre belirledik
hak = 3
while hak > 0:
#kullanıcıdan da istedik neden döngü içinde, her seferinde sorabilmek için
    user_name = input("Username: ")
    pass_word = input("Password: ")
    if user_name == username and pass_word == password:
        print("Login successful") #login olduk ama hak için bir şey yapmadık. Test lazım.
        while True:
            try:
                n1 = int(input("Number1: "))
                n2 = int(input("Number2: "))
                operation = input("Enter desired matematical operation, e for exit: ")
                match operation:
                    case "+":
                        result = n1 + n2
                        print(f"Your calculation is : {n1} {operation} {n2} = {result}") #DRY prensibine uyamadım.
                    case "-":
                        result = n1 - n2
                        print(f"Your calculation is : {n1} {operation} {n2} = {result}")
                    case "*":
                        result = n1 * n2
                        print(f"Your calculation is : {n1} {operation} {n2} = {result}")
                    case "/":
                        result = n1 / n2
                        print(f"Your calculation is : {n1} {operation} {n2} = {result}")
                    case "e":
                        print("Exiting the program.")
                        break
                    case _:
                        print("Invalid entry, try again.")
            except (ValueError, TypeError, ZeroDivisionError) as err:
                print(f"Cannot continue because of ({err}), try again.")
    else:
        print(f"Login denied!, remaining tries = {hak - 1}")
        hak -= 1 #döngüye sokacağız mecbur, burda da hakkımızı düşürdük.
print("Hakkınızı yitirdiniz, bye!") #While döngüsünden çıktığımızda hakkımız kalmamış olcak.

#endregion

#region First Try
# while i < try_count: #Sayacımız try_count kadar devam edicek
#     username = input("Username: ") #Username istedik
#     if username == "Adal": #Eğer doğruysa
#         password = input("Password: ") #Şifre istedik
#         if password == "1234": #Şifre doğrusa
#             print("Login successful! Welcome.") #Giriş yapıldığını söyledik.
#             login_successful = True #Artık login_successfull değişkenimiz true oldu ve döngüyü sonlandırdık.
#             break
#         else:
#             print("Incorrect password.") #Yanlışsa bunu kullanıcıya bildirdik ve 
#             i += 1 #sayacı artırdık.
#     else: #Kullanıcı adı yanlışsa:
#         print(f"Uncorrect username, please try again.")
#         i += 1 #Sayacı 1 artırdık.
#     if login_successful == False:
#         if (try_count - i) > 0:
#             print(f"You have {try_count - i} tries left")
#         else:
#             print("No more tries left. Account locked.")

#endregion

#region Second Try GEREKSİZ KARMAŞIK BU NE OKUNMUYO BİLE KADIN
# while (i+j) < try_count: #Sayacımız try_count kadar devam edicek
#     username = input("Username: ") #Username istedik
#     if username == "Adal": #Eğer doğruysa
#         while i+j < try_count:
#             password = input("Password: ") #Şifre istedik
#             if password == "1234": #Şifre doğrusa
#                 print("Login successful! Welcome.") #Giriş yapıldığını söyledik.
#                 login_successful = True #Artık login_successfull değişkenimiz true oldu ve döngüyü sonlandırdık.
#                 break
#             else:
#                 print("Incorrect password.") #Yanlışsa bunu kullanıcıya bildirdik ve 
#                 j += 1 #sayacı artırdık.
#                 print(f"You have {try_count - (i+j)} tries left")
#     else: #Kullanıcı adı yanlışsa:
#         print(f"Uncorrect username, please try again.")
#         i += 1 #Sayacı 1 artırdık.
#         print(f"You have {try_count - (i+j)} tries left")
#     if login_successful == False:
#         if (try_count - (i+j)) > 0:
#             pass
#         else:
#             print("No more tries left. Account locked.")
#     else:
#         print("happy happy happy") #Buraya calculator
#         while login_successful == True:
#             # stop_attemt = input("Write "STOP" for closing the program.: ").lower()
#             if stop_attemt == "stop":
#                 print("Program is shutting down.")
#                 break #döngüden çıkıyoruz.
#             calculator = input("Desired Mathematical Operation: ")
#             if not calculator in ["+", "-", "*", "/"]:
#                 pass
#             else:
#                 number1 = float(input("First number: "))
#                 number2 = float(input("Second number:  "))
#                 #try: buraya input olarak string kabul etmemeliyiz
#                 #except:
#                 match calculator:
#                     case "+":
#                         result = number1 + number2
#                     case "-":
#                         result = number1 - number2
#                     case "*":
#                         result = number1 * number2
#                     case "/":
#                         if number2 == 0:
#                             pass
#                             # try:
#                             # except:
#                         else:
#                             result = number1 / number2
#                     case "e":
#                         pass
#                     case _:
#                         #Buraya loop koyalım ve diyelim ki doğru işareti girene kadar devam
#                         pass

#endregion

#region Third Try
# i = 0
# try_count = 3
# USERNAME = "Adal"
# PASSWORD = "1234"
# login_successful = False

# while i < try_count:
#     username = input("Username: ")
#     if username == USERNAME:
#         while i < try_count:
#             password = input("Password: ")
#             if password == PASSWORD:
#                 print("Correct password.")
#                 login_successful = True
#                 break
#             else:
#                 i += 1
#                 print(f"Password is wrong, please try again.\nTry count = {i}\nRemaining try count = {try_count - i}")
#         print("Correct username.")
#         break
#     else:
#         i += 1
#         print(f"Username is wrong, please try again.\nTry count = {i}\nRemaining try count = {try_count - i}")

# if login_successful == True:
#     print("Login successful.")
#     while True:
#         operator = input("Please enter the mathematical expression you want to calculate (+, -, *, /, e(to exit)): ")
#         if operator in ["+", "-", "*", "/", "e"]:
#             while True:
#                 try:
#                     number1 = float(input("Number 1: "))
#                     break
#                 except ValueError as err:
#                     print("Please enter invalid number.")
#             while True:
#                 try:
#                     number2 = float(input("Number 2: "))
#                     break
#                 except ValueError as err:
#                     print("Please enter invalid number.")
#             match operator:
#                 case "+":
#                     result = number1 + number2
#                 case "-":
#                     result = number1 - number2
#                 case "*":
#                     result = number1 * number2
#                 case "/":
#                     while number2 == 0:
#                         try:
#                             number2 = float(input("Please re-enter the divisor number: "))
#                         except (ZeroDivisionError, ValueError) as err:
#                             print("You cannot divide a number to 0 or another letter, please check your number.")
#                     result = number1 / number2
#                 case "e":
#                     print("Program is shutting down.")
#                     exit()
#             print(f"Your calculation is: {number1} {operator} {number2} = {result}")
#         else:
#             print("You are attempting an undefined operation, please try again.")
# else:
#     print("You've consumed all of your tries, program is shutting down.") #Buraya programdan çıkış
#     exit()
#endregion

#todo Girilen sayının asal olup olmadığını kontrol eden uygulama

#region Second Try
while True:
    try:
        sayi = int(input("Lütfen bir sayı giriniz: "))
        is_asal = True
        if sayi < 2: #2den küçük asal sayı yoktur ve negatif sayılar asal olamaz.
            print("Negatif sayılarda asallık bakılmaz ve 2'den küçük sayılar asal değildir.")
            break
        else:
            for i in range(2, sayi):
                if sayi % i == 0:
                    is_asal = False
                    break
            if is_asal == True:
                print(f"Girilen sayı ({sayi}) asaldır.")
            else:
                print(f"Girilen sayı ({sayi}) asal değildir.")
    except (ValueError, TypeError) as err:
        print(f"{err} sebebiyle hata verildi, lütfen sayıyı tekrar giriniz.")

#endregion

#region Hocanın çözümü
sayi = int(input("Sayıyı giriniz: "))
if sayi < 2:
    print("2'den küçük sayıların asallık durumu yoktur.")
else:
    is_asal = True
    i = 2
    while i < sayi: #Burada eşitlik olmaması durumu sayi mod sayi = 0 olmaması için gerekli.
        if sayi % i == 0:
            is_asal = False
            break
#Buraya else: yazsak da olur, yazmasak da olur.
        i += 1
    if is_asal: #is_asal is True:
        print(f'{sayi} asaldır.')
    else:
        print(f'{sayi} asal değildir.')
#endregion


