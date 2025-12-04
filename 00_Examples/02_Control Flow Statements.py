
#todo Ternary if tek/çift sayı kontrolü
# sayi = int(input("Sayıyı giriniz: "))
# print("Çift") if sayi % 2 == 0 else print("Tek")

#todo Ternary if erişkinlik durumu
# yas = int(input("Yaşınız: "))
# print("Reşit") if yas > 18 else print("Reşit değil")

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