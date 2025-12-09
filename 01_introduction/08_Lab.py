
#! Listelerde Sıklıkla Kullanılan Built-In-Fonksiyonlar (Built-in Function) 2

numeric_lst = [1,2,3,4,5,6,7,8,9,0]
alpha_lst = ["a","b","c","d","e","f","g","h"]

#? filter() buil-in-function
#* Bir kurala tanımlanır ve kurala uyan elemanları ayıklar
#* Listeler üzerinde filtrelemeye yarayan fonksiyon
#* Listedeki tüm öğeleri gezer ve koşulu True döndüren öğeleri seçerek yeni bir sonuç dizisi oluşturur.
#* Filtreleme kuralı basit olduğunda, genellikle yerleşik ve isimsiz Lambda fonksiyonları kullanılır, bu da kodu daha kısa yapar:
#* Filter fonksiyonu obje içinde obje yarattığı için (Lambda aslında bir fonksiyon) aslında oldukça maliyetli O(N**2) kadar maliyetli oluyor.

print( #filter fonksiyonu ile üretilen liste, geçiçi bir liste olduğu için
    list( #eldeki veriyi listeye çevirdik (çevirmezsek çalışmaz)
        filter(lambda x: x < 5, numeric_lst) #kümelere benzer, x öyle ki, numberic_lst'te 5'ten küçük olan x'leri al.
        )
    )

#region Examples
#todo Verilen listedeki değerlerin karşılığı sayısal ise bunu yazdıran uygulama
#* Hint: isgidit() fonksiyonunu kullan
#* Lambda fonksiyonu bir performans sorunudur, bunu engellemek için kullanmadan yapalım:

some_values = ["123", "su", "zxc", "987", "345"]
only_digit = list(
    filter(str.isdigit, some_values) #! lambdadan kurtulduk burda 
                                     #! built in fonksiyonlarını tiplerine özel olarak çalıştırabiliriz. 
                                     #! yani lambdayı built in fonksiyonlar özelinde kullanmayabiliriz.
)
print(only_digit)
#* Python programlama dili, içerisindeki built in fonksiyonları kullandığımız zaman daha hızlı çalışır.

#todo filter fonksiyonu ile çift sayıların filtrelenip ve liste olarak ekrana yazdırılması
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

#todo sonu .com ile biten mail adreslerini filter fonksiyonu ile yazdıran ifade
#* Hint: endswith() fonksiyonunu kullan

# mails = [
#     "burak.yilmaz@outloo.com", 
#     "savage@mail.com", 
#     "beast@", 
#     "keko@com.xyz", 
#     "adal@gmail.com"
# ]

# correct_mails = (list(
#     filter(
#         lambda x: x.endswith(".com"), mails)
#     )
# )
# print(correct_mails)
#endregion





# #? map() built-in-function
# #* Her elemana bir fonksiyon uygular. (Genellikle list() ile kullanılır.)


# # 8 12 2025
# #? map() built-in-function
# #* Her elemana bir fonksiyon uygular. (Genellikle list() ile kullanılır.)
# #* tip dönüşümlerinde kullanılabilir, filtrelemelerde kullanılabilir, bir sınıf bir tipe ait mi değil mi

# #sektörde maplemek, yani belirli tipteki elemanları belirli bir tipe dönüştürmeye maplemek denir
# # kullanımına bakıldığında filter ile benzer kullanıma sahip

# # #todo rakamların karesini alalım

# # print(
# #     list(
# #         map(
# #             lambda x: x**2, [i for i in range(10)]
# #         )
# #     )
# # )

# # #todo tip dönüşümü örneği

# # print(
# #     list(
# #         map(str, [i for i in range(10)]) #str bir fonksiyon, lambda yerine
# #     )
# # )

# # str(10) #çıktısı "10"
# # int("10") #çıktısı 10 yani bunlar birer fonksiyon

# # #todo mail adress

# # mail_adresses = [
# #     "burak.yilmaz@outlook.com",
# #     "hakan.yilmaz",
# #     "ipek.yilmaz@outlook.com"
# # ]

# # print(
# #     list(
# #         map(
# #             lambda x: "@" in x, mail_adresses
# #         )
# #     )
# # )

# #todo liste içinde liste

# products = [ #ürün adı, stoktaki miktarı, fiyatı
#     ["boxing gloves", 100, 59.9],
#     ["punching bags", 150, 160.99],
#     ["hand wrap", 200, 11.99]
# ]

# #pricelara %10 kdv uygulamaca


# # prices = [price for name, stock, price in products]


# # print("Orijinal Fiyatlar:")
# # prices = list(map(lambda p: p[2], products))
# # print(prices)

# # kdv = list(map(lambda price: price * 1.10, prices))

# # print(kdv)

# # print ( list(
# #     map(lambda p: (p[0], p[2] * 1.10), products)
# # )
# # )

# #sadece ürün fiyatı listeleme
# #kendi çözümüm
# print(
#     list(
#         map(lambda x: x * 1.1, [price for name, stock, price in products])
#     )
# )

# #hocanın çözümü

# print(
#     list(
#         map(
#             lambda x: x[2] * 1.1, products
#         )
#     )
# )

# print(
#     list(
#         map(
#             lambda x: x, [names for names, stock, prices in products]
#         )
#     )
# )

# #map fonksiyonu ile eleman dğeiştirilmiyor sadece anlık yeni bir liste oluşturuluyo gibi düşün

# #todo baş harfleri büyüterek listeyeleyin
# names = ['burak yilmaz', 'hakan yilmaz', 'ipek yilmaz']
# print(
#     list(
#         map(str.title, names)
#     )
# )

# #kendi çözümüm
# # print(
# #     list(
# #         map(
# #             str.title, ["burak yilmaz", "hakan yilmaz", "ipek yilmaz"] 
# #         )
# #     )
# # )

# #todo aynı listeden şu sabitle mail adresi craft edin

# domain_name = "@outlook.com"

# #kendi çözümüm
# # print(
# #     list(
# #         map(
# #             lambda x: x + domain_name, [name.replace(" ", "") for name in names]
# #         )
# #     )
# # )

# # #hocanın çözümü
# # print(
# #     list(
# #         map(
# #             lambda x: f"{x.replace(' ', '.')}{domain_name}", names)
# #         )
# #     )

# #todo iki listeyi toplayarak listeye ekleyin
# #bir liste diğerinden short olabilir, bunu göz onünde bulundurarak çözünüz
# #* önemli soru bunu düşünerek çözmeni beklerler sınavlarda

# lst_1 = [87, 67, 81, 69, 65, 99, 79, 57, 62, 65]
# lst_2 = [20, 39, 46, 100, 48, 34, 75, 59]

# #path i
# print(
#     list(
#         map(
#             lambda x, y: (x + y), lst_1, lst_2)
#         )
#     )

# #path ii
# print(
#     list(
#         map(
#             lambda x: x[0] + x[1], 
#             zip(lst_1, lst_2)
#         )
#     )
# )

# # print(
# #     list(
# #         map(
# #             lambda x: x[0]+x[1], list( zip (lst_1, lst_2) ) 
# #             ) 
# #             )
# # )

# #ödev
# # -100 ile + 100 arasında 10 tane rastegele sayı üretelim
# # sadece pozitif sayıları string dönüştürerek bir liste içerisinde çıktı verin

# # list comprehension ile 2 tane rastgele sayılar içeren liste oluşturun
# # üretilecek sayı aralıkları -100, +100
# # her iki listedeki sayıları toplayalım
# # toplamları negatif olanları pozitif dönüştürerek bir liste içerisinde yazıdralım