


#todo decorator ödev 3 aşağıdakilerin genişletilmesi?

# def is_manager(func):
#     def wrapper(user):
#         if user.get('role') in ['manager', 'general manager']:
#             return func(user)
#         else:
#             print(f'{user.get("username")} - {user.get("role")}\nRaporu görüntüleme yetkiniz bulunmamaktadır..!')
#     return wrapper

# @is_manager
# def get_report(user):
#     print(f'{user.get("username")} - {user.get("role")}\nReport görüntülendi..!')

# user_1 = {
#     'username': 'Hasan Cobanoğlu',
#     'role': 'manager'
# }

# user_2 = {
#     'username': 'Rana Nur Ceylan',
#     'role': 'general manager'
# }

# user_3 = {
#     'username': 'Burak Yılmaz',
#     'role': 'Irgat'
# }

# get_report(user_1)
# get_report(user_3)
# get_report(user_2)



#todo bunları decoratore dönüştürme uygulaması
# 100.000.000 tane rastgele sayı üretilecek. list comprhenbsion ile yapılacak
# Path I, II, III time ve memory cost hesaplayarak ekrana rapor olarak yazdırın
# Path I --> List Comprehensions ile poszitif sayılar bulunacak ve liste olarak ekrana basılacak.
# Path II --> Filter fonksiyonu ile poszitif sayılar bulunacak ve liste olarak ekrana basılacak.
# Path III --> For loop yapıalcak
# from random import randint
# import time
# import tracemalloc


# tracemalloc.start()
# t1 = time.perf_counter()

# # Sayı yaratırken aşağıdaki list comprehension kullanmak yerine generator pattern kullansaydınız işin rengi baya değişirdi. 
# # Sayı üretim hızı dramatik birşekilde artardı ve zaman maliyeti azalırdı.
# # numbers = [randint(a=-100, b=100) for _ in range(1000000)]
# numbers = (randint(a=-100, b=100) for _ in range(1000000))

# # List Comprehension
# positive_number = [number for number in numbers if number > 0]

# # Filter Func
# # positive_number = list(filter(lambda number: number > 0, numbers))

# # With For Loop
# # positive_number = []
# # for number in numbers:
# #     if number > 0:
# #         positive_number.append(number)

# print(positive_number)

# t2 = time.perf_counter()
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()

# runtime_ms = (t2 - t1) * 1000
# peak_memory = peak / 1024 / 1024

# print(
#     '===============================\n'
#     'Method --> List Comprehension\n'
#     f'Runtime: {runtime_ms}\n'
#     f'Peak Memory: {peak_memory}'
    
# )

"""
===============================
Method --> List Comprehension
Runtime: 5728.366099996492
Peak Memory: 28.39721393585205
===============================
Method --> Filter Func
Runtime: 3872.5149999954738
Peak Memory: 28.40944004058838
===============================
Method --> With For Loop
Runtime: 4765.219499997329
Peak Memory: 28.41720485687256
"""


#todo decorator ödev 2: log örneği ile kripto örneklerini birleştir lab 18-19

# from socket import gethostbyname, gethostname
# from datetime import datetime
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

# def sys_log(**kwargs) -> str:
#     try:
#         if '@' not in kwargs.get('email_address'):
#             raise ValueError('Invalid email address..!')
#         return 'Your email address is valid..!'
#     except ValueError as err:
#         aes_key = get_random_bytes(16)
#         aes_obj = AES.new(key=aes_key, mode=AES.MODE_EAX)
#         chipper_text = aes_obj.encrypt(b'valueerrorhappen')
#         with open(file=kwargs.get('file'), mode='a', encoding='utf-8') as file:
#             file.write(str(chipper_text))
#             file.write(' || ')
#             file.write(f'Machine Name: {kwargs.get("machine_name")}')
#             file.write(' || ')
#             file.write(f'IP Address: {kwargs.get("ip_address")}')
#             file.write(' || ')
#             file.write(f'Exception Date: {kwargs.get("exception_date")}')
#         return f'{err}'

# print(
#     sys_log(
#         file='log.txt',
#         machine_name=gethostname(),
#         ip_address=gethostbyname(gethostname()),
#         exception_date=datetime.now(),
#         email_address='qwe.qwezxc.com'
#     )
# )

# from datetime import datetime

# def log_info(func):
#     def wrapper(*args, **kwargs):
#         print(
#             '===============================\n'
#             f'Yapılan İşlem: {func.__name__}\n'
#             f'İşlem Tarihi: {datetime.now()}\n'
#         )
#         return func(*args, **kwargs)
#     return wrapper

# @log_info
# def para_cekme(hesap_no: str, bakiye: int, cekilecek_tutar: int):
#     bakiye -= cekilecek_tutar
#     return (
#         f'Bu {hesap_no}, para çekildi..!\n'
#         f'Güncel Bakiye: {bakiye}'
#     )
    
# @log_info
# def para_yatırma(hesap_no: str, bakiye: int, yatırılacak_tutar: int):
#     bakiye += yatırılacak_tutar
#     return (
#         f'Bu {hesap_no}, para yatırıldı..!\n'
#         f'Güncel Bakiye: {bakiye}'
#     )
    
# print(
#     para_cekme(
#         hesap_no='1234456',
#         bakiye=1000,
#         cekilecek_tutar=500
#     )
# )

# print(
#     para_yatırma(
#         hesap_no='1234456',
#         bakiye=1000,
#         yatırılacak_tutar=500
#     )
# )



# # 1. Adım: Aynı fonksiyon tanımlar gibi decorator tanımlanır, ancak içerisine parametre olarak fonksiyon verilir.
# def my_decorator(func):
#     # 2. Adım: İçerisinde wrapper (hediye paketi :D) adlı iç fonksiyon olur. 
#     def wrapper():

#         print('Bazı işler burada çalıaşcak..!') #* Ara adım: Fonksiyon verilmeden önce çalışacak kod bloğu. Aslında süsleme kısmı

#         # 3. Adım: Bu wrapper adlı fonksiyonun içerisinde argümanı verilen fonksiyon execute edilir.
#         func()

#         print('belki bazı işlerde burada çalışacak..!') #* Ara adım: Fonksiyon çağrıldıktan sonra çalışacak kod bloğu. Aslında süsleme kısmı
    
#     # 4. Adım return wrapper denilir.
#     return wrapper

# #* Not: wrapper execute edilmez, define edilir ve standby olarak beklemesi için return wrapper dedik.

# # 5. Adım: Kullanımı yazılan bir fonksiyonun başına "@" ifadesi ile decorator çağrılır.
# @my_decorator
# def hello():
#     print('Merhaba')

# hello()
















# #region 24 aralık çözümü

# # # 24 12 2025
# # # ders 24

# # # #todo Filtreleme uygulaması
# # # #* Kullanıcıdan aradığı ürünün adını, fiyat aralığını, stokta olanları gösterip gösterilmeyeceği bilgilerini girdikten sonra gelen sonuçları ekrana yazdıralım.
# # # products = [
# # #     {'name': 'Lenovo X1 Carbon', 'price': 110_000, 'stock': 12},
# # #     {'name': 'Lenovo Thinkpad', 'price': 89_000, 'stock': 7},
# # #     {'name': 'Macbook Pro', 'price': 89_000, 'stock': 3},
# # #     {'name': 'Macbook Air', 'price': 125_000, 'stock': 5},
# # #     {'name': 'Asus Zenbook', 'price': 150_000, 'stock': 4},
# # #     {'name': 'Monster Huma', 'price': 55_000, 'stock': 18},
# # #     {'name': 'Monster Alba', 'price': None, 'stock': 0},
# # #     {'name': "Monster Abra", 'price': 72_000, 'stock': 0},
# # #     {'name': "Monster Tulpar", 'price': 104_000, 'stock': 3},
# # #     {'name': "Monster Semruk", 'price': 243_000, 'stock': 14},
# # #     {'name': "MSI Katana 17", 'price': 73_000, 'stock': 5}
# # # ]

# # # def get_clean_data(data: list) -> list: #gelen listede ismi veya priceı none olanları eledik
# # #     """Adı veya Fiyatı None olanları eler."""
# # #     # FAZ 6: List Comprehension kullanımı
# # #     return [p for p in data if p.get("name") is not None and p.get("price") is not None]
# # # print(get_clean_data(products))

# # # # --- FİLTRELER ---
# # # def filter_by_criteria(data: list, name_search: str, min_p: float, max_p: float) -> list:
# # #     """İsim ve Fiyat aralığına göre filtreler"""
# # #     return [
# # #         p for p in data 
# # #         if name_search.lower() in p["name"].lower() # İsim kontrolü
# # #         and min_p <= p["price"] <= max_p           # Fiyat kontrolü
# # #     ]


# # # # # --- FAZ 4 & 5: GÜVENLİ INPUT FONKSİYONU ---
# # # # def get_safe_float(prompt: str, default_value: float) -> float:
# # # #     """
# # # #     Kullanıcıdan sayı ister.
# # # #     - Boş geçerse -> Default değeri döner.
# # # #     - Harf girerse -> Hata vermez, uyarır ve Default değeri döner.
# # # #     """
# # # #     raw_data = input(prompt)
# # # #     if not raw_data: # Kullanıcı hiçbir şey yazıp enter'a bastıysa
# # # #         return default_value
    
# # # #     try:
# # # #         return float(raw_data)
# # # #     except ValueError:
# # # #         print(f"⚠️ Hatalı giriş! Varsayılan değer ({default_value}) kullanılıyor.")
# # # #         return default_value

# # # # # --- FAZ 3: STOK MANTIĞI ---
# # # # def apply_stock_filter(data: list, only_in_stock: bool) -> list:
# # # #     """
# # # #     only_in_stock True ise: Sadece stoku > 0 olanları getir.
# # # #     only_in_stock False ise: Hepsini getir (stok 0 olsa bile).
# # # #     """
# # # #     if not only_in_stock:
# # # #         return data # Filtreleme yapma, hepsini gönder
    
# # # #     return [p for p in data if p["stock"] > 0]


# # # # # --- ANA PROGRAM (MAIN) ---
# # # # def main():
# # # #     print("--- ÜRÜN FİLTRELEME SİSTEMİ V1.0 ---")
    
# # # #     # 1. Adım: Temiz Veriyi Hazırla
# # # #     # Senin "beceremedim" dediğin yer burasıydı. Temiz veriyi bir değişkene alıyoruz.
# # # #     clean_products = get_clean_data(products) 
    
# # # #     # 2. Adım: Kullanıcıdan Verileri Güvenli Al (Faz 4-5)
# # # #     aranan_isim = input("Aranan ürün adı (Hepsi için Enter): ").strip()
# # # #     min_fiyat = get_safe_float("Min Fiyat (Varsayılan 0): ", 0.0)
# # # #     max_fiyat = get_safe_float("Max Fiyat (Varsayılan 500.000): ", 500000.0)
    
# # # #     stok_sorusu = input("Sadece stokta olanları mı göstereyim? (E/H): ").lower()
# # # #     sadece_stoktakiler = True if stok_sorusu == 'e' else False

# # # #     # 3. Adım: Filtreleri Uygula (Pipeline)
# # # #     # Temiz listeden -> İsim/Fiyat Filtresine
# # # #     filtered_list = filter_by_criteria(clean_products, aranan_isim, min_fiyat, max_fiyat)
    
# # # #     # Kalan listeden -> Stok Filtresine
# # # #     final_result = apply_stock_filter(filtered_list, sadece_stoktakiler)

# # # #     # 4. Adım: Sonuçları Yazdır
# # # #     print(f"\n🔍 Bulunan Ürün Sayısı: {len(final_result)}")
# # # #     if not final_result:
# # # #         print("😔 Kriterlere uygun ürün bulunamadı.")
# # # #     else:
# # # #         for urun in final_result:
# # # #             durum = "✅ Stokta" if urun['stock'] > 0 else "❌ Tükendi"
# # # #             print(f"- {urun['name']:<20} | {urun['price']:,.0f} TL | {durum}")

# # # # # Programı Başlat
# # # # main()

# # # # #hoca da stock durumunu çözemedi, stock true gelirse stoğu 0 olmayanları gösterme, stock false gelirse stoğu sıfır olsa da göster anlamına geliyor

# # # # #faz 3: stok durumunu çözdükten sonra, try excepte gerek var mı, varsa neden gerek var? ne olabilir burda? çöz.

# # # # #faz4: bunları input yapsaydık, yani get data içine yazdıklarımızı, kullanıcı yanlışlıkla string girerse ne olur?

# # # # #faz 5: kullancıı değer girmeyi atlarsa ne olacak?
