
# #! small projects içindeki benchmarkı tekrar çöz, anla, gerekirse diğer projelerede benchmark ekle

# #14. ders ödevi:
# # 100.000 tane rastgele sayı üretilecek. List comprehension ile yapılacak
# #path i, ii, iii t,öe ve öeöpry cost hesaplanarak ekrana rapor olarak yazdırın
# #path i: list comprehensions ile pozitif sayılar bulunacak ve liste olarak ekrana basılacak
# #path ii: filter onksiyonu ile pozitif...
# #pathiii for loop ile

# # #14. ders ödevine ek olarak: bu satır sutün algoritması için de time ve memory cost hesapla.
# # #region Satır Sutün Algoritması
# # #? Satır-Sütun algoritması
# # #* SATIR SÜTUN ALGORİTMALARINDA: i satırı, j sütunu yönetir, yani i 1. adımındayken j orada belirtilen adım kadar çalışır.

# # #Geleneksel yöntem:
# # for i in range(1,11):
# #     for j in range(1,11):
# #         print(f"{i} x {j} = {i * j}")
# #     print("-------------------")

# # #List comprehension ile yapılması:
# # lst_carpim_tablosu = [ 
# #     (i*j) #yazdırılacak sonuç 
# #     for i in range(1,11) #en dış döngü
# #     for j in range(1, 11) #en iç döngü
# # ]
# # print(lst_carpim_tablosu)
# # #* Tek satır olmadı yine alt satıra geçtik, ee ne anlamı kaldı list comprehension'ın? Go for benchmark testing!

# # #List comprehension ile PRINT FONKSİYONU İÇİNDE yapılması:
# # print(
# #     [
# #         [f"{i} x {j} = {i * j}" for i in range(1, 11)] for j in range(1, 11) #liste içinde liste yaptık
# #     ]
# #     ) #Burda aslında list içinde for içinde for ve liste içinde liste de tanımlıyoruz, sınırımız yok.
# # #endregion

# # #Geleneksel yöntem:
# # for i in range(1,11):
# #     for j in range(1,11):
# #         print(f"{i} x {j} = {i * j}")
# #     print("-------------------")

# # #List comprehension ile yapılması:
# # lst_carpim_tablosu = [ 
# #     (i*j) #yazdırılacak sonuç 
# #     for i in range(1,11) #en dış döngü
# #     for j in range(1, 11) #en iç döngü
# # ]
# # print(lst_carpim_tablosu)
# # #* Tek satır olmadı yine alt satıra geçtik, ee ne anlamı kaldı list comprehension'ın? Go for benchmark testing!

# # #List comprehension ile PRINT FONKSİYONU İÇİNDE yapılması:
# # print(
# #     [
# #         [f"{i} x {j} = {i * j}" for i in range(1, 11)] for j in range(1, 11) #liste içinde liste yaptık
# #     ]
# #     ) #Burda aslında list içinde for içinde for ve liste içinde liste de tanımlıyoruz, sınırımız yok.
# # #endregion


#todo Doğru loginde, ürün search ve fiyat output. Yanlış loginde yeni kayıt. Username'ler unique olacak.

#bütün ürünlerin toplam fiyatı nedir
#ürün adı laptop olan ürünlerin fiyatlarını toplayalım
#kullanıcı ürün search edebilsin, yani ürün search etti monitör yazdı varsa fiyatını verdi
#fiyatı 200 tl altında olan ürünler listelensin
# #register olsun, yani kayıt da olsun; username varsa hali hazırda ekleyemesin

# users = [
#     ["beast", "123"],
#     ["bear", "456"],
#     ["keko", "789"]
# ]

# is_login = False
# username = input("Username: ").lower()
# password = input("Password: ")
# for USERNAME, PASSWORD in users:
#     if username == USERNAME and password == PASSWORD:
#         is_login = True
#         break


# while is_login == False:

#     sign_in = input("Wrong entry, would you like to sign up(1) or try to sign in again?(0): ")
#     match sign_in:
#         case "1":
#             new_username = input("Please enter a username: ").lower()
#             if new_username not in USERNAME:
#                 new_password = input("Please enter password: ")
#                 users.append([new_username, new_password])
#                 print("Welcome, you can login with new informations now.")
#                 username = input("Username: ").lower()
#                 password = input("Password: ")
#                 for USERNAME, PASSWORD in users:
#                     if username == USERNAME and password == PASSWORD:
#                         is_login = True
#         case "0":
#             break
#         case _:
#             print("Try again.")

products = [
    ["Laptop", 850],
    ["Smartphone", 499],
    ["Headphones", 79],
    ["Keyboard", 45],
    ["Monitor", 220],
    ["Mouse", 25],
    ["Smartwatch", 150],
    ["Tablet", 310],
    ["External Hard Drive", 95],
    ["Webcam", 60],
    ["Laptop", 850]
]


# print(
#     list(
#         map(
#             lambda x: x[0], [user for user in users]
#         )
#     )
# )






