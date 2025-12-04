
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

#todo Girilen sayının faktöriyelini hesaplayan uygulama
# n = int(input("Faktöriyeli hesaplanacak sayı: "))
# faktoriyel = 1
# i = 1

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

# for i in range(1, n + 1):
#     faktoriyel = faktoriyel * i
#     print(f'{i}. adımdaki toplam = {faktoriyel}')
# print(f'istenen faktöriyel = {faktoriyel}')

#todo Girilen sayıya kadar toplamı veren uygulama
# hedef_sayi = int(input("Kaça kadar olan sayılar toplansın: "))

# i = 0
# toplam = 0
# while i <= hedef_sayi:
#     toplam = toplam + i
#     print(f'{i}. adımdaki toplam = {toplam}')
#     i = i + 1

# print(f'istenen toplam = {toplam}')

# bitis = int(input("Kaça kadar gitsin? "))
# sayi = range(1, bitis)
# toplam = 0
# for i in sayi:
#     toplam = i + toplam
#     print(f'her adımdaki toplam: {toplam}')
# print(f'sonuçtaki toplam: {toplam}')