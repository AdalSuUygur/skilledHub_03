
# # #challenge CRUD sözlük üzerinden create, read, update, delete yapmaya çalış
# # list vs tuple
# # prons & cons
# # set()
# # dictionary, built-in, CRUD operasyonularını sözlük üzerinden uygulayın.

# #? set fonksiyonu :D finally!!!!
# # liste gibi davranır
# # küme yapısı
# # tekrarlı eleman olmaz
# # unique valueları döner ama kendine has unique bir dönüş tipi vardır.

# #todo örnek
# numbers = [1,1,1,2,3,4,5,5,5,2,3,4,5]
# print(set(numbers))
# #süslü parantezle gösterilir
# #string ifadelerde de kullanılır
# #tekrar eden sayılar gösterilmez
# #dönüş tipi convert edilebilir gerektiği gibi set fonksiyonunda
# #sayısal verilerde değil, sözel ifadelerde de kullanılabilir.

# #todo
# full_name = "buraburak"
# unique_ch = set(full_name)
# print(unique_ch)

# #? setin kendine has operatörleri

# x = {1, 2, 3, 4, 5}
# y = {4, 5, 6, 7, 8}

# print(x & y) #iki setin kesişimini verir

# print(x / y) #birleşim kümesini verir

# #? set fonksiyonları:
# #* eleman eklemek için:

# boxers = {"muhammed ali", "mike tyson"}

# boxers.add("lenox lewis") #add ile eklenir
# boxers.remove("lenox lewis") #olmayan bir eleman yazıldığında patlar
# boxers.discard("lenox lewis") #bu da varsa silerim yoksa da ignorelar devam ederim diyor

# #? ALL FUNCTION
# #* bir şart yazılır ve şart listenin tüm elemanları için sağlıyorsa true, sağlamıyorsa false dönüyor
# #* bütün itemların şartı sağlaması lazım
# ages = [18,24,35,65,41,13]
# member = all(age > 18 for age in ages)
# print(member) #hepsi 18den büyük olmadığı için false döner

# #todo örnek tüm ürünlerde stok var mı yok mu

# products = [
#     ['name', 'boxing gloves', 'price', 59.99, 'stock', 5],
#     ['name', 'punching bags', 'price', 159.99, 'stock', 15],
#     ['name', 'handwrap', 'price', 19.99, 'stock', 0]
# ]

# stock = all(product[5] > 0 for product in products)
# print(stock) #false döner çünkü stokta 0 olan ürün var

# #todo örnek password

# password = "Bu?ra4k_"

# is_password_valid = [
#     any(ch.isupper() for ch in password),
#     any(ch.islower() for ch in password),
#     any(ch.isdigit() for ch in password),
#     any(not ch.isalnum() for ch in password)
# ]

# print(
#     all(is_password_valid)
# )

# #? tuples - demetler
# #* immutable
# #* listelerdeki gibi crud operasyonları yapılamıyor, sabitlerimizi tanımlayabileceğimiz bir yapı
# #* yapısı gereği okuma operasyonlarında daha hızlı

# #örneğin, bir data geliyor ve sadece okuma amaçlı kullanacağım
# #o zaman tuplea dönüştürüyorum
# #sadece okulayacaksam!!

# #data ieçrisinde update yapacaksak, veya manipülasyonlar yapılacaksa, yeni veriler eklenecekse lsite kullanılır
# #SADECE OKUMA YAPILACAKSA TUPLE KULLANILIR!!!

# tuple_1 = ("Galatasaray",
#            "Adana Demirspor",
#            "Beşiktaş",
#            "Trabzonspor",
#            "Fenerbahçe"
#            )

# tuple_2 = ("Red Skins",
#            "Seahawks",
#            "Vikings",
#            "Patriots"
#            )

# tuple_3 = tuple_1 + tuple_2 #max yapılabilecek işlem toplama
# #ve dilimleme/slicing yapılabilir
# print(tuple_3[2:5])

#nested tuple'lar veya liste içinde tuplelar tanımlanılabilir. bunlarda sınırlama yok.
#okuma amaçlı kullanılacağı zaman tuple tercih edilir!!!!

#? tuplelarda built in fonksiyonları yoktur çok çok az (nokta notasyonu, metoddan bahsediyo hoca saırım)

#? DICTIONARIES
#süslü parantez ile tanımlanır
#key value ile çalışır
#anahtar tanımlanır karşılığında anahtar tanımlanır
#genelde keyler için tuplelar kullanılır

release_year_movie = { #sol taraf key sağ taraf value
    'Fight Club': 1999,
    'Matrix': 1999,
    'Interstaller': 2014,
    'Inception': 2018,
    'Dune': 2021
}

# #region read
# #todo fight club anahtarında tutulan value ekrana yazdırın
# #path i
# print(release_year_movie["Fight Club"])
# #path ii
# print(release_year_movie.get("Fight Club"))

# #end region

# #get ALL values:
# for value in release_year_movie.values():
#     print(value)

# #get ALL keys: 
# for keys in release_year_movie.keys():
#     print(keys)

# #get ALL items:
# for key,value in release_year_movie.items():
#     print(
#         f"Movie name: {key}\n"
#         f"Release year: {value}"
#     )

# #endregion

#region create item
# yeni bir item eklerken de: key - value olarak eklemek gerek sözlüğün yapısından dolayı
release_year_movie["Dune II"] = 2023
print(release_year_movie)

#endregion

#region update
#dune ii'nin çıkış tarihini 2024 yapalım:

release_year_movie.update( #update fonksiyonu bizden sözlük ister
    {
        "Dune II": 2024
    }
)

#endregion

#region delete
#path i
del release_year_movie["Dune II"]
print(release_year_movie)

#endregion

#todo ödev

