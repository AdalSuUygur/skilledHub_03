
#! LIST COMPREHENSION

#? List Comprehensions 
#* Bir listeyi oluşturmak için gereken adımları (boş liste tanımlama, döngü kurma, .append() ile ekleme), tek bir sözdizimi içine yerleştirmektir.
#* Yani listeyi kısaca oluşturmak için List Comprehensions kullanılır.

#Geleneksel yöntem ile liste oluşturma:
lst_geleneksel = []
for i in range(10):
    lst_geleneksel.append(i)
print(lst_geleneksel)

#YA DA list comprehension ile kısa yoldan liste oluşturma:
#* append etme mantığı gibi düşün, bak geleneksek yöntemle i'yi ekliyoruz append ile ama tek satırda.
lst_comprehension = [i for i in range(10)]
print(lst_comprehension)

#todo Ternary if + List Comprehension ile
fruits = [
    "Apple", "Banana", "Orange", "Mango", "Pineapple",
    "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
    "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
    "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
]

#todo1 meyve listesindeki meyvelerin içerisinde "a" geçiyorsa bu meyveleri yazdıran uygulama
lst_includes_a = [fruit for fruit in fruits if "a" in fruit.lower()] #fruit.lower() yazmamızın sebebi de içinde küçük a harfine bakıyor olmamız.
print(lst_includes_a)

#todo2 meyve listesindeki meyvelerin içerisinde "an" geçiyorsa True, geçmiyorsa False eklenen uygulama
# Hint: "adult" if age >= 19 else "child"
lst_includes_an = [True if "an" in fruit.lower() else False for fruit in fruits] #ternary if yapısı ile kullanabildik
print(lst_includes_an)
#* Comprehension kompleksleştikçe yazması da okuması da zorlaşıyor, peki neden tercih ediliyor? ÇÜNKÜ ÇOK DAHA AZ MALİYETLİ

#region Satır Sutün Algoritması
#? Satır-Sütun algoritması
#* SATIR SÜTUN ALGORİTMALARINDA: i satırı, j sütunu yönetir, yani i 1. adımındayken j orada belirtilen adım kadar çalışır.

#Geleneksel yöntem:
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
    print("-------------------")

#List comprehension ile yapılması:
lst_carpim_tablosu = [ 
    (i*j) #yazdırılacak sonuç 
    for i in range(1,11) #en dış döngü
    for j in range(1, 11) #en iç döngü
]
print(lst_carpim_tablosu)
#* Tek satır olmadı yine alt satıra geçtik, ee ne anlamı kaldı list comprehension'ın? Go for benchmark testing!

#List comprehension ile PRINT FONKSİYONU İÇİNDE yapılması:
print(
    [
        [f"{i} x {j} = {i * j}" for i in range(1, 11)] for j in range(1, 11) #liste içinde liste yaptık
    ]
    ) #Burda aslında list içinde for içinde for ve liste içinde liste de tanımlıyoruz, sınırımız yok.
#endregion

#region Dilimleme
#? Slicing (Dilimleme) Operatörü
#* Pandas (veri analizinde de) kullanılır, çok önemli!!!!
#* Mevcut bir SIRALI YAPININ belirli bir bölümünü alarak YENİ BİR YAPI oluşturma işlemidir. 
#* Bu dilimleme orjinal listeyi değiştirmez.

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
#endregion

#region Unboxing özelliği
#? Unpacking - Unboxing (Söz dizimi özelliği)
#* Bir koleksiyonun öğelerini alıp bu öğeleri ayrı ayrı değişkenlere atanması durumudur.

my_family = [ #Bu listemiz
    ["Lale Selam", 29, "Analyst-Unemployed"],
    ["Aslı Meram", 33, "Guidance Counselor"],
    ["Karam Çalık", 37, "English Teacher"],
    ["Alık Balık", 61, "Retired"],
    ["Sade Kanık", 67, "Chauffeur"]
]

for item in my_family: #şimdi ailedeki her bir öğeyi dışarı çıkartıyoruz (bu da unboxing aslında)
    print(item) #Kısaca liste içindeki listenin dış listesinden kurtardık.

#* Unpacking yaparken karşılaması gereken valueların tam olması lazım, eksik veya fazla olursa patlar
for name, age, occupation in my_family: #myfamilyden bana gelen bilgileri öyle bir karşılayayım ki tık tık tık eşleşsin
    print(                              #Ki bu da unboxing bak
        f"Full name: {name}\n"
        f"Age: {age}\n"
        f"Occupation: {occupation}"
    )
#endregion
