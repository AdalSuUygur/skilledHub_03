
#! DICTIONARIES - SÖZLÜKLER
#* Koleksiyondur, key-value ile çalışır.
#* Sırasızlardır ve değiştirilebilirler ancak key value'ları eşsizdir. Değiştirlemezler, sabitlerdir.
#* Key(anahtar) tanımlanır karşılığında value tanımlanır.
#* key value ile çalışır

#? SYNTAX Yapısı
# Sözlükler süslü parantez "{}" ile tanımlanır. Set'ten farkı ne? Sette Key:Value şeklinde tanımlama yapılamaz.
# Sözlükte ise yapısından gereği tanımlama key:value şeklinde olmalıdır.

# sözlük_ismi = {key : value} şeklinde tanımlama yapılır.

release_year_movie = { #Sözlüğün ismi,
    'Fight Club': 1999, #İlk elemanı, Key: Fight Club, Value: 1999.
    #Neden key ismi? Çünkü aynı isimde tek film olur, ancak 1999 yılında 1 film olmaz.
    'Matrix': 1999,
    'Interstaller': 2014,
    'Inception': 2018,
    'Dune': 2021
}

#? CRUD Operasyonları

#* Create:
# Sözlüğe yeni bir item ekleneceğinde key:value şeklinde eklenmelidir.

release_year_movie["Dune II"] = 2023 # "Dune II" keyiyle bir item ekledik, value'su da 2023

#* Read: "Fight Club" anahtarında tutulan value değerlerini okumak için
# Path I
print(release_year_movie["Fight Club"])

# Path II
print(release_year_movie.get("Fight Club"))

# get ALL values: #Tüm VALUEları okur
for value in release_year_movie.values():
    print(value)

# get ALL keys: #Tüm KEYleri okur
for keys in release_year_movie.keys():
    print(keys)

#get ALL items: #HER ŞEYİ OKUR
for key,value in release_year_movie.items():
    print(
        f"Movie name: {key}\n"
        f"Release year: {value}"
    )

#* Update: "Dune II"nin çıkış tarihini yanlış yazdığımızı varsayalım ve value değerini 2024 yapalım

release_year_movie.update( #update fonksiyonu bizden sözlük ister
    {
        "Dune II": 2024
    }
)

#* Delete:

del release_year_movie["Dune II"]
print(release_year_movie)

#region Examples

#todo Products listesindeki sözlüklerin içerisindeki işlemler
products = [
    {"name": "Lenovo X1 Carbon", "price": 110.000},
    {"name": "Lenovo Thinkpad", "price": 89.000},
    {"name": "Macbook Pro", "price": 250.000},
    {"name": "Mackbook Air", "price": 125.000},
    {"name": "Asus Zenbook", "price": 150.000},
    {"name": "Monster Huma", "price": 55.000},
    {"name": "Monster Alba"},
    {"price": 250.000}
]

#* Products listesindeki tüm ürünlerin fiyatlarının toplamı:
# Path I: Junior Çözümü
# total_price = 0
# for product in products: #product'ın tipi sözlük
#     total_price += product.get("price")
# print(total_price)

# Path II: Mid Çözümü
# total_price = sum(product.get("price") for product in products)
# #* sum() fonksiyonu iterable bir nesne alır ve değerleri toplayarak ilerler.
# print(total_price)

#* Products listesindeki ürünlerin fiyat aralığı 100.000'den büyük olanları listeleyelim
# Path I: Kendi Çözümüm
# print(list(
#     product for product in products if product.get("price") > 100.000
# ))

# Path II: Hocanın Mid Seviye Çözümü
# price_threshold = 100.000 #input olarak da kullanıcıdan alınabilir
# filtered_product = [product for product in products if product.get("price") > price_threshold]
# print(filtered_product)

#* Ürün adı ("name") içerisinde "Lenovo" geçen ve fiyat aralığı 100.000-150.000 aralığında olan ürünleri listeleyin
#* Burdaki çıkarım: .get() metodu içerisinde default tanımlama yapılması.
# Path I: Kendi Çözümüm
# print(list(
#     product for product in products if ("Lenovo" in product.get("name")) and (100.000 < product.get("price") < 150.000)
# )) #none type hatası geldi 2 eksik sözlük yapısını listeye ekleyince.

# Path II: Hocanın çözümü
# name_kwd = "Lenovo" #input olarak alabileceğimiz için hoca bunları bu şekilde değişkene atadı.
# min_price = 100.000
# max_price = 150.000

# Benim çözümümle aynı, ne farkı var? Fark default tanımlama yaptı.
# filtered_product = [
#     product for product in products 
#     if name_kwd in product.get("name", "") and  # Burada product.get("name", "") burada get metodu içine default değer tanımladık eğer tanımlanmamışsa diye
#     #bu da name'i olmayan bir ürün geldiyse default değer olarak "" yazdır demek.
#     min_price < product.get("price", 0) < max_price
#     ]

# print(filtered_product)

#todo 19.ders yerine gelen ödev sorusu çözümü 
# Aşağıdaki categories sözlüğüne: Kullanıcı sınırsız işlem yapabilsin.
# 1. yeni kayıt eklenecek (Create New Record)
# 1.1. id bilgisi 'd912b8cf-0b59-4efb-bfcf-17356dd59c9b' uuid modülünden faydalanarak yaratılacak
# 2. var olan bir kayıt güncellenecek (Update) --> kullanıcıdan id bilgisi alınacak ve ilgili kayıt güncelenecek
# 3. var olan bir kayıt silinecek (Delete) --> kullanıcıdan id bilgisi alınacak ve ilgili kayıt güncelenecek
# 4. Read operasyonları --> bütün kayıtlar listelenecek, kullanııdan ürün adı alınacak ve ilgli ürün listelenecek,

categories = {
    'd912b8cf-0b59-4efb-bfcf-17356dd59c9b': {
        'name': 'Boxing Gloves',
        'description': 'Best boxing gloves'
    },
    '9ecfa748-ee8e-4ac3-a471-33e1fd9fe52c': {
        'name': 'MMA Gloves',
        'description': 'Best MMA gloves'
    }
}

from uuid import uuid4
from pprint import pprint #pretty print demek bu, sözlükler için kullanıyoruz. Tatlış print :D

print(uuid4()) #test
print(type(uuid4)) #test

# Soru şu: bizim UUID4 çıktısının tipi ile bizim elimizdeki dataların tipi farklı, elimizdeki data tipi string.
# O zaman elimizdeki tipi de stringe çevirmemiz gerek.

print(str(uuid4()))

# while True:
#     process = input("Type a process: ").lower() #kullanıcı bize yapacağı işi söylesin.
# # value'ya atanmış olan idler key, karşılığında ise value olarak sözlük var.
# # iç sözlükte 2 tane key var 2 tane de value var. 

#     match process:
#         case "create": #yapının aynısını kuruyoruz
#             new_name = input("Please type a category name: ")
#             new_descp = input("Please type a description name: ")
#             categories[str(uuid4())] = {
#                 "name": new_name,
#                 "description": new_descp
#             }
# #birebir yukarıdaki yapıyı çalıştırdık
#             pprint(categories)

#         case "get all":
#             pprint(categories)

#         case "get by id":
#             category_key = input("Category Key: ")
#             result = categories.get(category_key)
#             if result is None:
#                 print("There is no category.")
#             else:
#                 print(result)

#         case "get by name":
#             # Kendi çözümüm:
#             # categories.values() burda values olarak iç sözlüğe ulaştım
#             # içerideki her değeri gezdim ve value değişkenindeki "name" adındaki keyi yazdırdım.
#             # print(list(value["name"] for value in categories.values()))
#             # Hocanın çözümü:
#             cat_name = input("Category name: ")
#             filtered_categories = [category for category in categories.values() if cat_name in category.get("name")]
#             pprint(filtered_categories)

#         case "update": #single report güncellenecekse id den gidilir ki karışmasın
#             category_key = input("Category Key: ")
#             if category_key is None:
#                 print("There is no category.")
#             else:
#                 new_name = input("Please type a category name: ")
#                 new_descp = input("Please type a description name: ")
#                 categories.update({
#                         category_key: {
#                         "name": new_name,
#                         "description": new_descp
#                 }})
#                 print("Category key has been edited.")

#         case "delete":
#             category_key = input("Category Key: ")
#             is_exist = any(key == category_key for key in categories.keys())
#             if is_exist:
#                 del categories[category_key]
#                 print(f"{category_key} has been removed.")
#             else:
#                 print("There is no such a category.")

#         case _:
#             print("Invalid process type.")

#endregion
