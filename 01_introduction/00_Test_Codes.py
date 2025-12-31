
#region 22 aralık ödevi
# #todo Ödev (22 Aralık Ödevi-2): Girilen bilgilerin doğruluğunu check eden fonksiyon yapılarıyla kurulmuş uygulama

# #* 1 sign in ve sign up
# #* sign up işleminde kullanıcının girdiği password valid mi, user_name unique mi? e_mail valid mi?
# #* bu kurallardan geçerse üyelik işlemi tamamlanacak
# #* sign inta da yine pass word doğru mu bu sefer, e-mail ve password doğruysa giriş yap
# #* veri yapısı: 
# #* aşağıda sample data structure

# users = {
#     "adal": {"adal@skilledhub.com": "Adal.123"},
#     "su": {"su@outlook.com": "Su.123"},
#     "ahmet": {"ahmet@gmaiwindowslive.com": "Ahmet.123"},
#     "mehmet": {"mehmet@skilledhub.com": "Mehmet.123"},
#     "kerim": {"kerim@hotmail.com": "Kerim.123"},
#     "cemal": {"cemal@yahoo.com": "Cemal.123"}
#     }

# #region Doğrulayıcılar
# import string
# def is_valid_password(password: str) -> bool: #uygunsa true, değilse false olarak döner
#     min_character = 6
#     if len(password) <= min_character:
#         return False
    
#     if any(ch.isspace() for ch in password): #burda da boşluk var mı yok mu
#         return False
    
# # gelen passwordu setten geçireceğiz ama neden?
#     ch_set = set(password)
# # performans sağlamak için

#     checks = [
#     any(ch.islower() for ch in ch_set),
#     any(ch.isupper() for ch in ch_set),
#     any(ch.isdigit() for ch in ch_set),
#     any(ch for ch in ch_set if ch in string.punctuation)
#             ]
#     return all(checks)

# # def is_valid_email(mail_adresses: str) -> bool | str:
# #     try:
# #         if "@" not in mail_adresses:
# #             raise TypeError("The mail adress must contain the @ symbol.")
# #         if mail_adresses in users.keys():
# #             raise ValueError("This mail adress has already taken.")
# #         return True #iflerden geçerse true dönecek
    
# #     except (TypeError, ValueError) as err:
# #         return str(err)
# #     #öbür türlü zaten patlayacak ve string olarak errorü vercek.

# def is_valid_email(mail_adresses: str) -> bool: #bool ihtiyacımız oldu aşağıdaki sign up kısmı için ondan sildik
#     try:
#         if "@" not in mail_adresses:
#             raise TypeError("The mail adress must contain the @ symbol.")
#         if mail_adresses in users.keys():
#             raise ValueError("This mail adress has already taken.")
#         return True #iflerden geçerse true dönecek
    
#     except (TypeError, ValueError) as err:
#         print(err) #bu da kendimize log gibi düşün
#         return False

# #region işlemler
# def sign_up(mail_adresses: str, password: str) -> str:
#     if is_valid_password(password=password) and is_valid_email(mail_adresses=mail_adresses):
#         users[mail_adresses] = password
#         return "Your membership has been completed!"
#     else:
#         return "Invalid credentials."

# def sign_in(mail_adresses: str, password: str) -> str:
#     for key, values in users.items():
#         if key == mail_adresses and values == password:
#             return f"Welcome to the jungle"
#     return "Invalid credentials."

# def main():
#     while True:
#         process = input("Type a process: ")

#         match process:
#             case "sign in":
#                 sign_in(
#                     mail_adresses= input("Mail adress: "),
#                     password= input("Password: ")
#                 )

#             case "sign up":
#                 sign_up(
#                     mail_adresses= input("Mail adress: "),
#                     password= input("Password: ")
#                 )
#                 print(users) #kendimize backdoor
#             case _:
#                 print("Type a valid process name.")

# main()

#endregion

#region yapamadığım ve yapmak ZORUNDA olduğum örnek

#hatalarım
# u_plus_p = list(zip(*(username for username in users))) #bu yapı bana usernames listesi ve şifreler listesi verdi, ben burdan usernames çekmeye çalışıyorum

#todo Doğru loginde, ürün search ve fiyat output. Yanlış loginde yeni kayıt. Username'ler unique olacak.

#bütün ürünlerin toplam fiyatı nedir
#ürün adı laptop olan ürünlerin fiyatlarını toplayalım
#kullanıcı ürün search edebilsin, yani ürün search etti monitör yazdı varsa fiyatını verdi
#fiyatı 200 tl altında olan ürünler listelensin
#register olsun, yani kayıt da olsun; username varsa hali hazırda ekleyemesin

# users = [
#     ["beast", "123"],
#     ["bear", "456"],
#     ["keko", "789"]
# ]

# def is_login(user_name, pass_word):
#     for USERNAME, PASSWORD in users:
#         if user_name == USERNAME and pass_word == PASSWORD:
#             return True
#     return False

# username = input("Username: ").lower()
# password = input("Password: ")
# case_login = is_login(username, password)

# while not case_login:
#     sign_in = input("Wrong entry, would you like to sign up(1) or try to sign in again?(0): ")
#     match sign_in:
#         case "1":
#             #* case1 içini çalıştıramadım, şu an giriş alsa bile eklemiyor sanırım listeye, debug gerek
#             # new_username = input("Please enter a username: ").lower()
#             # usernames = list(zip(*users))[0]
#             # if new_username not in usernames:
#             #     new_password = input("Please enter password: ")
#             #     users.append([new_username, new_password])
#             #     print("Welcome, you can login with new informations now.")
#             #     username = input("Username: ").lower()
#             #     password = input("Password: ")
#             #     new_case_login = is_login(username, password)
#             # else:
#             #     new_case_login = False
#             # if not new_case_login:
#             #     break
# #* case0 sorunsuz çalışıyor, kendime hayran kaldım :D
#         case "0":
#             username = input("Username: ").lower()
#             password = input("Password: ")
#             case_login = is_login(username, password)
#         case _:
#             print("Try again.")




            # if new_username not in USERNAME:

            #     
            #     print("Welcome, you can login with new informations now.")




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

#endregion

#region 24 aralık çözümü


# # 24 12 2025
# # ders 24

# # #todo Filtreleme uygulaması
# # #* Kullanıcıdan aradığı ürünün adını, fiyat aralığını, stokta olanları gösterip gösterilmeyeceği bilgilerini girdikten sonra gelen sonuçları ekrana yazdıralım.
# # products = [
# #     {'name': 'Lenovo X1 Carbon', 'price': 110_000, 'stock': 12},
# #     {'name': 'Lenovo Thinkpad', 'price': 89_000, 'stock': 7},
# #     {'name': 'Macbook Pro', 'price': 89_000, 'stock': 3},
# #     {'name': 'Macbook Air', 'price': 125_000, 'stock': 5},
# #     {'name': 'Asus Zenbook', 'price': 150_000, 'stock': 4},
# #     {'name': 'Monster Huma', 'price': 55_000, 'stock': 18},
# #     {'name': 'Monster Alba', 'price': None, 'stock': 0},
# #     {'name': "Monster Abra", 'price': 72_000, 'stock': 0},
# #     {'name': "Monster Tulpar", 'price': 104_000, 'stock': 3},
# #     {'name': "Monster Semruk", 'price': 243_000, 'stock': 14},
# #     {'name': "MSI Katana 17", 'price': 73_000, 'stock': 5}
# # ]

# # def get_clean_data(data: list) -> list: #gelen listede ismi veya priceı none olanları eledik
# #     """Adı veya Fiyatı None olanları eler."""
# #     # FAZ 6: List Comprehension kullanımı
# #     return [p for p in data if p.get("name") is not None and p.get("price") is not None]
# # print(get_clean_data(products))

# # # --- FİLTRELER ---
# # def filter_by_criteria(data: list, name_search: str, min_p: float, max_p: float) -> list:
# #     """İsim ve Fiyat aralığına göre filtreler"""
# #     return [
# #         p for p in data 
# #         if name_search.lower() in p["name"].lower() # İsim kontrolü
# #         and min_p <= p["price"] <= max_p           # Fiyat kontrolü
# #     ]


# # # # --- FAZ 4 & 5: GÜVENLİ INPUT FONKSİYONU ---
# # # def get_safe_float(prompt: str, default_value: float) -> float:
# # #     """
# # #     Kullanıcıdan sayı ister.
# # #     - Boş geçerse -> Default değeri döner.
# # #     - Harf girerse -> Hata vermez, uyarır ve Default değeri döner.
# # #     """
# # #     raw_data = input(prompt)
# # #     if not raw_data: # Kullanıcı hiçbir şey yazıp enter'a bastıysa
# # #         return default_value
    
# # #     try:
# # #         return float(raw_data)
# # #     except ValueError:
# # #         print(f"⚠️ Hatalı giriş! Varsayılan değer ({default_value}) kullanılıyor.")
# # #         return default_value

# # # # --- FAZ 3: STOK MANTIĞI ---
# # # def apply_stock_filter(data: list, only_in_stock: bool) -> list:
# # #     """
# # #     only_in_stock True ise: Sadece stoku > 0 olanları getir.
# # #     only_in_stock False ise: Hepsini getir (stok 0 olsa bile).
# # #     """
# # #     if not only_in_stock:
# # #         return data # Filtreleme yapma, hepsini gönder
    
# # #     return [p for p in data if p["stock"] > 0]


# # # # --- ANA PROGRAM (MAIN) ---
# # # def main():
# # #     print("--- ÜRÜN FİLTRELEME SİSTEMİ V1.0 ---")
    
# # #     # 1. Adım: Temiz Veriyi Hazırla
# # #     # Senin "beceremedim" dediğin yer burasıydı. Temiz veriyi bir değişkene alıyoruz.
# # #     clean_products = get_clean_data(products) 
    
# # #     # 2. Adım: Kullanıcıdan Verileri Güvenli Al (Faz 4-5)
# # #     aranan_isim = input("Aranan ürün adı (Hepsi için Enter): ").strip()
# # #     min_fiyat = get_safe_float("Min Fiyat (Varsayılan 0): ", 0.0)
# # #     max_fiyat = get_safe_float("Max Fiyat (Varsayılan 500.000): ", 500000.0)
    
# # #     stok_sorusu = input("Sadece stokta olanları mı göstereyim? (E/H): ").lower()
# # #     sadece_stoktakiler = True if stok_sorusu == 'e' else False

# # #     # 3. Adım: Filtreleri Uygula (Pipeline)
# # #     # Temiz listeden -> İsim/Fiyat Filtresine
# # #     filtered_list = filter_by_criteria(clean_products, aranan_isim, min_fiyat, max_fiyat)
    
# # #     # Kalan listeden -> Stok Filtresine
# # #     final_result = apply_stock_filter(filtered_list, sadece_stoktakiler)

# # #     # 4. Adım: Sonuçları Yazdır
# # #     print(f"\n🔍 Bulunan Ürün Sayısı: {len(final_result)}")
# # #     if not final_result:
# # #         print("😔 Kriterlere uygun ürün bulunamadı.")
# # #     else:
# # #         for urun in final_result:
# # #             durum = "✅ Stokta" if urun['stock'] > 0 else "❌ Tükendi"
# # #             print(f"- {urun['name']:<20} | {urun['price']:,.0f} TL | {durum}")

# # # # Programı Başlat
# # # main()

# # # #hoca da stock durumunu çözemedi, stock true gelirse stoğu 0 olmayanları gösterme, stock false gelirse stoğu sıfır olsa da göster anlamına geliyor

# # # #faz 3: stok durumunu çözdükten sonra, try excepte gerek var mı, varsa neden gerek var? ne olabilir burda? çöz.

# # # #faz4: bunları input yapsaydık, yani get data içine yazdıklarımızı, kullanıcı yanlışlıkla string girerse ne olur?

# # # #faz 5: kullancıı değer girmeyi atlarsa ne olacak?




# fruits = [
#     "Apple", "Banana", "Orange", "Mango", "Pineapple",
#     "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
#     "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
#     "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
# ]

# b = fruits[:]
# print(b)

#endregion