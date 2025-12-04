
#! LISTS
#* Farklı veri tiplerini tek bir yerde tutmaya yarayan veri koleksiyonlarıdır.
#* Listeler verileri kalıcı olarak depolamazlar, listeler RAM'de depolanır.
#* LİSTELER DEĞİŞTİRİLEBİLİR (MUTABLE) BİR VERİ KOLEKSİYONUDUR

#SYNTAX YAPISI
meyveler = ["elma", "muz", "kiraz"]
karisik_liste = [10, "Merhaba", 3.14, True] #burdan öğrenmemiz gereken şu, listelerde FARKLI VERI TİPLERİ AYNI ANDA DEPOLANABİLİR!!

#? Index Nedir, nasıl çalışır
#* Index, bir listedeki her bir öğenin konumunu belirten sayısal etikettir. 
#* Listeler sıralı olduğu için, her öğenin sabit bir konumu vardır.
#* Negatif indeksleme ile listenin son öğesine -1. elemanı ile ulaşabildiğimizi gösterir.

#SYNTAX OLARAK GÖSTERİMİ
isimler = ["Ali", "Burak", "Cem", "Deniz"]
# Index:    0       1       2        3
# Negatif: -4      -3      -2       -1

print(isimler[0])   # Çıktı: Ali (İlk öğe)
print(isimler[3])   # Çıktı: Deniz
print(isimler[-1])  # Çıktı: Deniz (Son öğe)

#? Listelerde yerleşik metodlar
#* Bu metotlar, liste adından sonra nokta (.) (Bu duruma nokta notasyonu denir) koyularak çağrılır.

#todo Listelerde metot kullanımı: 
#region Hocanın çözümü, boxers 
boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewix', "Evander Holyfiled", "George Foreman"]

#? Listenin sonuna "Rocky Marciano"
boxers.append("Rocky Marciano") #Listenin sonuna ekler
#nokta notasyonu = bir objenin sonuna nokta konulduğunda ona ait features/functions gelir.
print(boxers)

#? Kullanıcıdan alınan boksör ismini yine kullanıcıdan alınan index değerine yazdıralım
boxer_name = input("Name: ")
index_value = int(input("Index: "))
boxers.insert(index_value, boxer_name)
print(boxers)

#? Merge Two Lists 
royal_division = ["Antorny Jasua", "Tyson Fury", "Deantony Wilder"]
boxers.extend(royal_division)
print(boxers)

#? Read an Item
print(boxers[2])

#? 5. indexte bulunan itemı "Joe Frazeir" ile değiştirin.
boxers[5] = "Joe Frazeir"
print(boxers)

#? 0. Indexteki elemanı silelim
boxers.pop(0)
print(boxers)

#veya

boxers.remove("Lenox Lewix")
print(boxers)

#? Listedeki içindeki itemları alıp işleme sokulması, yani teker teker sırayla dolaşılması
for boxer in boxers: #boxer geçiçi bir isim olarak verildi burada.
    print(boxer)

for i in range(len(boxers)): #boxers listesinin uzunluğu kadar
    print(boxers[i])

for ch in 'adal su': #"adal su" kısım da string aslında liste mantığı gibi çalışabilir.
    print(ch,end='-') #bundaki her karakteri de teker teker dolaşabiliyorum.
#endregion

#region Kendi çözümüm, Formula 1 Drivers
drivers = [
    "Oscar Piastri", "Lando Norris", 
    "George Russell", "Kimi Antonelli",
    "Max Verstappen", "Yuki Tsunoda",
    "Charles Leclerc", "Lewis Hamilton"]
print(drivers) #buraya herhangi bir şey eklemedik yani albon'u görmeyeceğiz.

drivers.append("Alexander Albon") #Append metodu ile albonu liste sonuna ekledik
print(drivers) #burada ise albonu görürüz

drivers.insert(1,  "Carlos Sainz") #Insert metodu ile 1. index değerine "Carlos Sainz"'i sıkıştırdık.
print(drivers) #Burada 1. indexte sainzi görürüz

last_drivers = [
    "Liam Lawson", "Isack Hadjar",
    "Esteban Ocon", "Oliver Bearman",
    "Lance Stroll", "Fernando Alonso", 
    "Nico Hulkenberg", "Gabriel Bortoleto"
    "Pierre Gasly", "Franco Colapinto"
] #yeni bir liste tanımladık ve burada kalan diğer driverları yazdık.

drivers.extend(last_drivers) #drivers listesine last_drivers listesini ekledik
print(drivers) #burada iki listenin birleşmiş halini görürüz

print(drivers[2]) #Bu 2. indexteki değeri çekiyor, print fonksiyonu ile de yazdırdık.

drivers[4] = "DUTDUT DURUT" #MAX VERSTAPPEEEEN!
print(drivers) #4. Indexteki değeri (Kimi Antonelli) "DUTDUT DURUT" ile değiştirdik.

drivers.pop(4) #burda da DUTDUR DURUT" ifadesini index'i ile sildik.
print(drivers)
#buraya veya gelmeli
drivers.remove("DUTDUT DURUT") #burada da içeriğini girdik, ilk denk geldiğini siler.
print(drivers)

for driver in drivers:
    print(driver)

#endregion

#? Nested List Yapısı
#* Liste içerisinde liste yapısıdır, en basit anlatımıyla matematikteki matriks yapısı gibi düşün.

alisveris_sepeti = [
    "Ekmek",                        # 0. indexteki Tekil Ürün
    "Süt",                          # 1. indexteki Tekil Ürün
    ["Elma", "Muz", "Portakal"],    # 2. indexteki öğeler (Meyveler Kutusu)
    ["Kalem", "Silgi"],             # 3. indexteki öğeler (Kırtasiye Kutusu)
    15.99                           # 4 indexteki ürün (fiyat)
]
# alisveris_sepeti listesi 5 öğeye sahiptir ve 2 ve 3. indexteki öğeler de ayrıca listelerdir.
print(alisveris_sepeti[2][2]) #Listenin 2. indexteki elemanının 2. indexindeki elemanını yazdır.

#? Slicing (Dilimleme)
#* Pandas (veri analizinde de) kullanılır, çok önemli!!!!
#* Mevcut bir listenin belirli bir bölümünü alarak yeni bir liste oluşturma işlemidir. Bu dilimleme orjinal listeyi değiştirmez.

#SYNTAX YAPISI
#           yeni_liste = eski_liste [başlangıç_index(DAHİL) : bitiş_index(HARİÇ) : adım] 
#             default değerleri --- [       0 (SIFIR)       :    listenin_sonu   :  1  ]

fruits = [
    "Apple", "Banana", "Orange", "Mango", "Pineapple",
    "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
    "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
    "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
]

print(fruits[2:7]) #birinci değer başlangıç indexi, ikinci değer n-1 olacak şekilde kapanış indexi
print(fruits[:3]) #burada başlangıç belirtilmedi yani başlangıç 0 ve burada : ile 3.ye kadar diyoruz
print(fruits[1::2]) #birden başla, iki iki zıplayarak git demek çift iki nokta ile 
print(fruits[::4]) #gene başlangıCı vermedi ama 4er 4er zıplayarak git anlamına geldi 

print(fruits[::-1]) #0dan başla, -1 -1 git dedik ve aslında listeyi tersine çevirmiş olduk. 
# eksi koyunca reverse ediliyor gibi düşün, 0. eleman direkt son eleman gibi düşün
print(fruits[10::-3]) #başlangıç verdik diye burda reverse düşünme, 10. elemandan başla geriye doğru 3er adımla git
print(fruits[::-2])

#? Unpacking - Unboxing
#* Bir koleksiyonun öğelerini alıp bu öğeleri ayrı ayrı değişkenlere atanması durumudur.

my_family = [ #Bu listemiz
    ["Lale Selam", 29, "Analyst-Unemployed"],
    ["Aslı Meram", 33, "Guidance Counselor"],
    ["Karam Çalık", 37, "English Teacher"],
    ["Alık Balık", 61, "Retired"],
    ["Sade Kanık", 67, "Chauffeur"]
]

for item in my_family: #şimdi ailedeki her bir öğeyi dışarı çıkartıyoruz (bu da unboxing aslında)
    print(item)

#* Unpacking yaparken karşılaması gereken valueların tam olması lazım, eksik veya fazla olursa patlar
for name, age, occupation in my_family: #myfamilyden bana gelen bilgileri öyle bir karşılayayım ki tık tık tık eşleşsin
    print(                              #Ki bu da unboxing bak
        f"Full name: {name}\n"
        f"Age: {age}\n"
        f"Occupation: {occupation}"
    )

#? enumarete() built-in-function
#* Var olan listenin içerisinde dolaşırken fonksiyonun içerisine verilirse, listenin indexini ve itemını verir.

for index, item in enumerate(meyveler):
    print(
        f"Index value: {index}\n"
        f"Item Value: {item}"
    )

#? List Comprehensions (01-12-25, ders 14)
#* Bir listeyi oluşturmak için gereken adımları (boş liste tanımlama, döngü kurma, .append() ile ekleme) tek bir sözdizimi içine yerleştirmektir.
#* Yani listeyi kısaca oluşturmak için List Comprehensions kullanılır.

#Geleneksel yöntem ile liste oluşturma:
lst_geleneksel = []
for i in range(10):
    lst_geleneksel.append(i)
print(lst_geleneksel)

#YA DA list comprehension ile kısa yoldan liste oluşturma:
lst_comprehension = [i for i in range(10)]
print(lst_comprehension)

#HATTA tek satırda bile yazılabilir:
print(lst_comprehension_shorter = [i for i in range(10)])

#Comprehension kompleksleştikçe yazması da okuması da zorlaşıyor, peki neden tercih ediliyor? 
#Time fonksiyonu ile örnekte göreceğiz ^^

#todo rastgele üretilmiş 10 sayı ile list comprehension uygulaması
from random import randint
lst_random = [randint(a=10, b=100) for _ in range(10)] #randint fonksiyonunu kullanabildik.
print(lst_random)

#todo rakamların karesinin list compehension ile oluşturulması
lst_squares = [i**2 for i in range(10)] #işlem yapabildik.
print(lst_squares)

#todo 0-100 arasındaki çift sayıları listeye eklenmesi
lst_even_numbers = [i for i in range(101) if i%2 == 0] #if ile birlikte kullanabildik.
print(lst_even_numbers)

#todo ternary if ile, meyve içerisinde "an" geçiyorsa true, geçmiyorsa false eklenen list
fruits = [
    "Apple", "Banana", "Orange", "Mango", "Pineapple",
    "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
    "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
    "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
]

lst_includes_an = [True if "an" in fruit.lower() else False for fruit in fruits] #ternary if yapısı ile kullanabildik
print(lst_includes_an)

#? çarpım tablosu, satır-sütun algoritması
#* SATIR SÜTUN ALGORİTMALARINDA: i satırı, j sütunu yönetir, yani i 1. adımındayken j orada belirtilen adım kadar çalışır.

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
    print("-------------------")

#List comprehenstion ile yapılması:

lst_carpim_tablosu = [ i*j 
    for i in range(1,11) for j in range(1, 11)
]
print(lst_carpim_tablosu)

print(
    [
        [f"{i} x {j} = {i*j}"] for i in range(1,11) for j in range(1,11)
    ]
) #bu da hem tek satırda hem de süslüce hali

#? Filter() Function
#* Listeler üzerinde filtrelemeye yarayan fonksiyon
#* Listedeki tüm öğeleri gezer ve koşulu True döndüren öğeleri seçerek yeni bir sonuç dizisi oluşturur.
#* Filtreleme kuralı basit olduğunda, genellikle yerleşik ve isimsiz Lambda fonksiyonları kullanılır, bu da kodu daha kısa yapar:

#todo Fruits listesindeki içinde "an" geçen meyveleri filtreleme uygulaması
print(
    list(
        filter(
            lambda fruit: "an" in fruit, fruits
        )
    )
)

#todo -100 ile 100 aralığındaki 1000 random sayı ile oluşturulan bir listeden pozitif sayıları çekme uygulaması
from random import randint
numbers = [randint(a=-100, b=100) for i in range(1000)] #numbers diye 1000 itemlı liste oluşturuldu

#PATH I --- list comprehension
lst_positive_numbers = [number for number in numbers if number > 0]
print(lst_positive_numbers)

#PATH II --- filter() function
temp_lst = filter(lambda x: x>0, numbers) #geçici bir liste oluşturuldu, lambda fonksiyonunu küme tanımlamalarına benzetebilirsin
#geçici listede, numbers listesi içerisindeki x için, x>0 durumlarını temp_lst değişkenine ekle gibi bir çıkarım var.

lst_positive_numbers_lambda = list(temp_lst) #gelen değişkeni listeye çevirdik.
print(lst_positive_numbers_lambda)

#todo filter fonksiyonu ile çift sayıların filtrelenip ve liste olarak ekrana yazdırılması
temp_lst = filter(lambda x: x % 2 == 0, numbers)
even_numbers = list(temp_lst)
print(even_numbers)

#region 15. ders 03/12/2025
#? isinstance() fonksiyonu
#* içerisine girilen nesnenin belirli bir veri tipine ait olup olmadığını kontrol etmeye yarayan built-in fonksiyondur.
#* Yani: "Bu nesne, bahsettiğim türden bir şey midir?" sorusunun cevabını True veya False olarak verir.

lst = [None, "b", 3.14, False, 9, "Oscar Piastri"]
# Burdan sadece tam ve ondalıklı sayıları almamız gerek.

numbers = list( #listeye convert etmek için.
    filter(lambda x: isinstance(x, (int, float)), lst) #x yani lstedeki eleman int veya float mı
)
print(numbers) #çıktı olarak da: [3.14, False, 9] verir, çünkü isinstance değeri bool döndürür, bundan dolayı direkt öyle bir ifadeyi çıktı olarak verir.

#todo sonu .com ile biten mail adreslerini filter fonksiyonu ile yazdıran ifade
#* Hint: endswith() fonksiyonunu kullan

mails = [
    "burak.yilmaz@outloo.com", 
    "savage@mail.com", 
    "beast@", 
    "keko@com.xyz", 
    "adal@gmail.com"
]

correct_mails = (list(
    filter(
        lambda x: x.endswith(".com"), mails)
    )
)
print(correct_mails)

#todo Verilen listedeki değerlerin karşılığı sayısal ise bunu yazdıran uygulama
#* Hint: isgidit() fonksiyonunu kullan

some_values = ["123", "burak", "zxc", "987", "345"]
number_values = list(
    filter(
        lambda x: x.isdigit(), some_values
    )
)
print(number_values)

#Hocanın çözümü: Lambda fonksiyonu bir performans sorunudur, bunu engellemek için kullanmadan yapalım:
only_digit = list(
    filter(str.isdigit, some_values) #! lambdadan kurtulduk burda 
                                     #! built in fonksiyonlarını tiplerine özel olarak çalıştırabiliriz. 
                                     #! yani lambdayı built in fonksiyonlar özelinde kullanmayabiliriz.
)
print(only_digit)
#* python, içerisindeki built in fonksiyonları kullandığımız zaman daha hızlı çalışır.