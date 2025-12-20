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