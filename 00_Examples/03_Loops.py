
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

#region FOR LOOP

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
