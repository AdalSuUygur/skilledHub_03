
# LISTS

Python'da Liste (List), birden fazla öğeyi tek bir değişken içinde tutmak için kullanılan **sıralı** ve **değiştirilebilir** (mutable) bir v**eri koleksiyonu**dur.

Listeler verileri kalıcı olarak depolamazlar. Listeler RAM'de depolanır yani geçici alanda depolanır. RAM'in heap alanında referanslar saklanır.

>_Yani: Listeler farklı veri tiplerini tek bir değişken altında tutmaya yarar._

Veri Biliminde `Pandas DataFrame` dediğimiz o devasa tabloların atası Listelerdir.

## Listenin Anatomisi

Listeleri, arkasına sonsuz sayıda vagon eklenebilen bir **Tren** gibi düşün.

* **Sıralıdır (Ordered):** Vagonların sırası bellidir. Sen değiştirmediğin sürece karışmaz.
* **Değiştirilebilir (Mutable):** (Burası çok önemli!) Stringlerin aksine, bir listenin 2. vagonundaki yükü indirip yerine başka bir şey koyabilirsin.
* **Heterojendir:** İlk vagonda **Sayı**, ikinci vagonda **Yazı**, üçüncü vagonda **Başka Bir Liste** taşıyabilirsin.

## SYNTAX

Listeler köşeli parantezler (`[]`) içinde tanımlanır ve öğeler virgülle ayrılır.

```py
# List Syntax
meyveler = ["elma", "muz", "kiraz"]
karisik_liste = [10, "Merhaba", 3.14, True]
```

## Listelerin Index (Dizin) Mantığı Nedir?

Listeler sıralı olduğu için, her öğenin sabit bir konumu vardır.
Listenin elemanlarının bulunduğu sayıya index denir.

>**Yani:** Index, bir listedeki her bir öğenin konumunu belirten sayısal etikettir.

```py
#          0        1         2        3
iller = ["İzmir", "Ankara", "İstanbul", "Van"]
#         -4       -3        -2       -1

print(iller[0])  # İzmir (Başı)
print(iller[-1]) # Van (Sonu - Uzunluğu bilmene gerek yok!)
```

### Sıfır Tabanlı İndeksleme

Python'da sayım 0'dan başlar. Listenin ilk öğesi `0` indexindedir.

### Negatif İndeksleme

Listenin sonundan başlamak için kullanılır. Son öğe `-1` indexindedir.

> **NOT:** Veri biliminde son 5 günlük veriyi çekmek istediğinde `data[-5:]` yazacaksın. Negatif indeksleme hayat kurtarır.

## Slicing (Veri Dilimleme)

Elimizde devasa bir liste var ama bize sadece bir kısmı lazım. İşte burada **Dilimleme (Slicing)** devreye girer.\
Pandas (veri analizinde de) kullanılır, çok önemli!!!!\
Mevcut bir SIRALI YAPININ belirli bir bölümünü alarak YENİ BİR YAPI oluşturma işlemidir.\
Bu dilimleme orjinal listeyi değiştirmez.

**Formül:** `liste[başlangıç : bitiş : adım]`

* **Başlangıç:** Dahil (Yazmazsan 0).
* **Bitiş:** DAHİL DEĞİL (Yazmazsan listenin sonuna kadar).
* **Adım:** Kaçar kaçar gideceği.

```py
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sayilar[2:5])   # [2, 3, 4] -> 5 dahil değil!
print(sayilar[:3])    # [0, 1, 2] -> Baştan başla, 3. indekse kadar al.
print(sayilar[::2])   # [0, 2, 4, 6, 8] -> Baştan sona 2'şer atla.
print(sayilar[::-1])  # [9, 8, ... 0] -> LİSTEYİ TERS ÇEVİRİR! (Mülakat Sorusu)
```

## Unboxing - Unpacking (Söz dizimi özelliği)

Bir koleksiyonun öğelerini alıp bu öğeleri ayrı ayrı değişkenlere atanması durumudur.

```py
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

    ```py

