
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

#? map() built-in-function
#* map() fonksiyonunun ana amacı, koleksiyon üzerinde döngü kurup her öğeyi hızlı ve verimli bir şekilde işler.
#* Her elemana bir fonksiyon uygular.
#* Bu, özellikle büyük veri kümeleriyle çalışırken geleneksel for döngülerine göre daha okunabilir ve genellikle daha hızlı bir yaklaşımdır.

#* Tip dönüşümlerinde kullanılabilir, filtrelemelerde kullanılabilir, bir sınıf bir tipe ait mi değil mi gibi uygulamalarda kullanılır.
#* Gerçek hayat uygulamalarında "maplemek" terimi; belirli bir tipteki elemanları belirli bir tipe dönüştürmeye denir.

#SYNTAX YAPISI:
# map(fonksiyon, iterable nesne)

print(
    list(
        map(
            str, numeric_lst #numeric_lst içerisindeki itemları numeric ancak map fonksiyonu ile str'ye dönüştürdük.
        )
    )
)

#region Examples
#todo Mail adreslerinin içerisinde "@" olup olmadığını kontrol eden uygulama
# mail_adresses = [
#     "burak.yilmaz@outlook.com",
#     "hakan.yilmaz",
#     "ipek.yilmaz@outlook.com"
# ]

# print(
#     list(
#         map(
#             lambda x: "@" in x, mail_adresses
#         ) #true, false, true çıktısı verir. 
#     )
# )

# print(
#     list(
#         filter(
#             lambda x: "@" in x, mail_adresses
#         ) #bu da doğrudan mail adreslerini çıkartır.
#     )
# )

#todo Liste içerisindeki listede verilen ürünler ile alakalı uygulamalar
products = [ #ürün adı, stoktaki miktarı, fiyatı
    ["boxing gloves", 100, 59.9],
    ["punching bags", 150, 160.99],
    ["hand wrap", 200, 11.99]
]

#Priceların ekrana yazdırılması
# print(
#     list(
#         map(
#             lambda x: x[2], products
#         )
#     )
# )

#Pricelara %10 KDV uygulanılması
# print(
#     list(
#         map(lambda x: round(x * 1.1,2), [price for name, stock, price in products])
#     )
# )

#todo Verilen listedeki isimlerin baş harflerini büyüten uygulama
names = [ #Bu listemiz
    "lale selam",
    "aslı meram",
    "karam çalık",
    "alık balık",
    "sade kanık"
    ]

# print(
#     list(
#         map(str.title, names)
#     )
# )

#todo verilen listeden mail adresi craft eden uygulama
domain_name = "@outlook.com"

#kendi çözümüm boşluğu kaldırarak çözmüşüm
# print(
#     list(
#         map(
#             lambda x: x + domain_name, [name.lower().replace(" ", "") for name in names]
#         )
#     )
# )
#hocanın çözümü hoca nokta eklemiş
# print(
#     list(
#         map(
#             lambda x: f"{x.replace(' ', '.')}{domain_name}", names)
#         )
#     )

#todo Verilen 2 farklı listenin aynı indexlerinin toplanması uygulaması
#* ÖNEMLİ: Sana gerçek hayat uygulamalarında BİR LİSTENİN DİĞERİNDEN KISA OLDUĞU CASE'i HESABA KATMANI İSTERLER!!!!
from random import randint
numbers_1 = [randint(-100,100) for _ in range(25)]
numbers_2 = [randint(-100,100) for _ in range(12)]
#print(numbers_1) #test
#print(numbers_2) #test

#PATH I - map()
# print(
#     list(
#         map(
#             lambda x, y: (x + y), numbers_1, numbers_2)
#         ) 
#     )
#map() fonksiyonu da kısa olanı alır ikili verilen inputlarda, bu yüzden bu çıktı da düzgün gelir.

#PATH II - zip()
#print(list(zip(numbers_1, numbers_2))) #şu an bu 2 elemanlı tuplelerden oluşan bir liste, test amaçlı yazdırdık

# print(
#     list(
#         map(
#             lambda x: x[0] + x[1], #iki elemanlı tuplelerden 0. eleman ve 1. elemanı yani tupleleri topluyoruz birbirleriyle.
#             zip(numbers_1, numbers_2) #burda zip'ten çıkartıp listeye çevirmiyoruz çünkü çıkan zip özel nesnesi de iterable bir nesne
#         )
#     )
# ) #zip fonksiyonu zaten kısa olana kadar alacağı için bu senin safe yolun olacak.
#endregion
