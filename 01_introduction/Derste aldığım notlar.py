
# 10 12 25
# 18. ders


# #challenge CRUD sözlük üzerinden create, read, update, delete yapmaya çalış
# list vs tuple
# prons & cons
# set()
# dictionary, built-in, CRUD operasyonularını sözlük üzerinden uygulayın.


# from random import randint
# numbers_1 = [randint(-100,100) for _ in range(10)]
# numbers_2 = [randint(-100,100) for _ in range(10)]
# # print(numbers_1) #test
# # print(numbers_2) #test

# # print( #5. adım : terminale çıktısını verdik
# #     list( #4. adım : bulunan değerleri listeye çevirdik.
# #         map(abs, #3. adım : burda da hesaplanan değerlerin mutlak değerini aldık
# #             map(lambda x: x[0] + x[1], #2. adım : map fonksiyonu ile tupledaki değerleri topladık
# #                 zip(numbers_1, numbers_2)) #1. adım : iterable nesnemizi yarattık ve 2 farklı listenin indexlerini birleştirdik
# #         )
# #     )
# # )

# #derste örneğin çözümü ve hocanın esktraları:
# result = [abs(x+y) for x,y in zip(numbers_1,numbers_2)]
# lst_result = list(map(str, result))
# #çıktının "-" ifadelerle bağlanmasını istiyoruz.
# print("-".join(lst_result))

#lst_result'ın itemlarını aralarına - koyarak birleştir.

#? join fonksiyonu çok önemli bir fonksiyondur.
#* string birleştirme mevzusu var, iki string ifadeyi birleştirmek için " " = "" + "" gibi kullanılır, fstring içinde de benzer.
#* stringler değiştirilemez yapılardır, iki string ifadeyi birleştirince ramde farklı bir yere yazdırır (memory leake sebep olur) bundan dolayı daha az maliyetli olan join kullanılır.
#stringler immutable olduğu için.
#tekrar yer kaplamasın diye

#? set fonksiyonu :D finally!!!!
# liste gibi davranır
# küme yapısı
# tekrarlı eleman olmaz
# unique valueları döner ama kendine has unique bir dönüş tipi vardır.

#todo örnek
numbers = [1,1,1,2,3,4,5,5,5,2,3,4,5]
print(set(numbers))
#süslü parantezle gösterilir
#string ifadelerde de kullanılır

#mülakatlarda set özel işlemler gelir, dersi de tekrar etmek lazım.
#buraları yazmadım XD


#? ALL FUNCTION
#* şart listenin tüm elemanlarını sağlıyorsa true, sağlamıyorsa false dönüyor

ages = [18,24,35,65,41,13]

member = all(age > 18 for age in ages)

print(member) #false döner

#todo örnekk

products = [
    ['name', 'boxing gloves', 'price', 59.99, 'stock', 5],
    ['name', 'punching bags', 'price', 159.99, 'stock', 15],
    ['name', 'handwrap', 'price', 19.99, 'stock', 0]
]

stock = all(product[5] > 0 for product in products)
print(stock) #false döner çünkü stokta 0 olan ürün var

