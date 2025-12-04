
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

#region Listelerde Yerleşik Metodlar (Built-in Method)
#* Bu metotlar, liste adından sonra nokta (.) (Bu duruma nokta notasyonu denir) koyularak çağrılır.

#? Listelerde yerleşik metodlar
#* Sadece List sınıfına ait metodlardır.
#* Ait olduğu nesne üzerinden doğrudan değişiklik yapar.

#todo Listelerde metot kullanımı: 
drivers = [
    "Oscar Piastri", "Lando Norris", 
    "George Russell", "Kimi Antonelli",
    "Max Verstappen", "Yuki Tsunoda",
    "Charles Leclerc", "Lewis Hamilton"]
print(drivers) #buraya herhangi bir şey eklemedik yani albon'u görmeyeceğiz.

#? append()
drivers.append("Alexander Albon") #Append metodu ile albonu liste sonuna ekledik
print(drivers) #burada ise albonu görürüz

#? insert()
drivers.insert(1,  "Carlos Sainz") #Insert metodu ile 1. index değerine "Carlos Sainz"'i sıkıştırdık.
print(drivers) #Burada 1. indexte sainzi görürüz

last_drivers = [
    "Liam Lawson", "Isack Hadjar",
    "Esteban Ocon", "Oliver Bearman",
    "Lance Stroll", "Fernando Alonso", 
    "Nico Hulkenberg", "Gabriel Bortoleto"
    "Pierre Gasly", "Franco Colapinto"
] #yeni bir liste tanımladık ve burada kalan diğer driverları yazdık.

#? extend()
drivers.extend(last_drivers) #drivers listesine last_drivers listesini ekledik
print(drivers) #burada iki listenin birleşmiş halini görürüz

#? indexteki değeri çekmek list_name[index]
print(drivers[2]) #Bu 2. indexteki değeri çekiyor, print fonksiyonu ile de yazdırdık.

#? indexteki değeri değiştirmek
drivers[4] = "DUTDUT DURUT" #MAX VERSTAPPEEEEN!
print(drivers) #4. Indexteki değeri (Kimi Antonelli) "DUTDUT DURUT" ile değiştirdik.

#? pop()
drivers.pop(4) #burda da DUTDUR DURUT" ifadesini index'i ile sildik.
print(drivers)

#? remove
#buraya veya gelmeli
#drivers.remove("DUTDUT DURUT") #burada da içeriğini girdik, ilk denk geldiğini siler.
print(drivers)

#? her bir driverı yazdırma
for driver in drivers:
    print(driver)


#region Nested List
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
