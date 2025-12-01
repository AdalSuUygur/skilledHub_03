
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

#todo Girilen data sheetten ilkisim.soyisim@outlook.com şeklinde mail_adresses üretilip ekrana yazdırılan uygulama.
#* İpucu1: split() fonksiyonu
#* İpucu2: bir listenin uzunluğu ne olursa olsun son elemanına nasıl ulaşırım
users = ["Burak Yılmaz", "Adal Su Uygur", "Yasemin Uygur Erdem", "Sami Lütfü Esen Berk"]

#region Kendi denemem2
mail_addresses = []
mail_uzantisi = "@outlook.com"

for user in users:
    name_slices = user.split(" ")
    ilkisim = name_slices[0]
    soyisim = name_slices[-1]
    mail_addresses.append(f"{ilkisim}.{soyisim}{mail_uzantisi}")
print(mail_addresses)
#endregion YAPTIM KIZ

#region Kendi denemem1

users_splited = users.split(" ")
mail_adress = []

for user in users:
    user = user.lower()
    name_piece = user.split(" ")
    first_name = name_piece[0]
    last_name = name_piece[1]

#endregion

#region Hocanın çözümü

users = ['Burak Yılmaz', 'Rana Nur Ceylan', 'İpek Yılmaz', 'kerim Abdurrahman Burak Yılmaz']
mail_addresses = []
domain_name = "@outlook.com"
for user in users:
    user_names = user.lower().split(" ")
    mail_address = (f"{user_names[0]}.{user_names[-1]}{domain_name}")
    mail_addresses.append(mail_address)
print(mail_addresses)
#endregion

#todo Girilen sampledaki sesli harfleri, sessiz harfleri, typoları ayrı listelere ekleyen uygulama. İlgili listelerde eleman tekrarı olmamalı. Space ignore.
sample = "buRa1k _Ayi?Lm2aZu"
sesli_harfler = []
sessiz_harfler = []
typo_char = []
space_char = []

#region kendi çözümüm

for char in sample.lower():
    if char.isalpha():
        if char in "aeıioöuü":
            if char not in sesli_harfler:
                sesli_harfler.append(char)
        else:
            if char not in sessiz_harfler:
                sessiz_harfler.append(char)
    else:
        if char == " ":
            continue #ignore attık
        elif char not in typo_char:
            typo_char.append(char)

print(f"{sessiz_harfler}\n{sesli_harfler}\n{typo_char}")
#endregion YAPTIKKKKKK

#region Hocanın çözümü

word = input("Type something: ")

for ch in word.lower():
    if ch.isalpha(): #karakter alfabetik mi diye bakıyoruz.
        if ch not in sesli_harfler and ch not in sessiz_harfler:
            if ch in "aeıioöuü":
                sesli_harfler.append(ch)
            else:
                sessiz_harfler.append(ch)
    else:
        if ch == " ":
            continue
        typo_char.append(ch)

print(sesli_harfler)
print(sessiz_harfler)
print(typo_char)
#endregion

#todo 10ar tane rastgele sayı üretilip 2 listeye eklenecek. 3. listeye aktarılacak. appen kullanılması yasak, index mantığıyla çalışılacak.
lst_1 = []
lst_2 = []
lst_3 = []
from random import randint

#region kendi çözümüm
for i in range(10):
    sayi_1 = randint(a=0,b=100)
    lst_1.insert(i, sayi_1)
    sayi_2 = randint(a=0,b=100)
    lst_2.insert(i, sayi_2)
    lst_3.insert(i, lst_1[i] + lst_2[i])
print(lst_1)
print(lst_2)
print(lst_3)
#endregion

#region hocanın çözümü
for i in range(10):
#    print(randint(a=0,b=100)) #1. adım, ürettik evet 10 tane
    lst_1.insert(i, randint(a=0,b=100)) #2. adım ooh hemen üretilen kodla lst_1'e ekleyek
    lst_2.insert(i, randint(a=0, b=100)) #4. adım, bak bunu da ürettik hatta test edelim yine.

    lst_3.insert(i, lst_1[i]+lst_2[i]) #6. adım, oh misler gibi çalıştı bak, bir deyazdıralım da görelim
#print(lst_1) #3. test adımı, ee düzgün çalışıyor demekki o zaman lst_2'ye de aynı şekilde ekleyek
#print(lst_2) #5. adım, çözdük, o zaman devamke
print(f"{lst_1}\n{lst_2}\n{lst_3}")
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
    ["Adal Su Uygur", 29, "Analyst-Unemployed"],
    ["Yasemin Uygur Erdem", 33, "Guidance Counselor"],
    ["Habiba Uygur", 37, "English Teacher"],
    ["Süreyya Uygur", 61, "Retired"],
    ["Abdülrezzak Uygur", 67, "Chauffeur"]
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

#todo Login bilgileri eşleşirse, ürün search ve fiyat output.
#todo Yanlış loginde yeni kayıt. username'ler unique
# kullanıcı login olacak
# register olsun
# bütün ürünlerin toplam fiyatı nedir
# ürün adı laptop olan ürünlerin fiyatlarını toplayalım
# kullanıcı ürün search 
# fiyatı 200 TL altında olan ürünler listelensin

users = [
    ["beast", "123"],
    ["bear", "456"],
    ["keko", "789"]
]

products = [
    ["Laptop", 850],
    ["Smartphone", 499],
    ["Headphones", 79],
    ["Keyboard", 45],
    ["Monitor", 220],
    ["Mouse", 25],
    ["Smartwatch", 150],
    ["Tablet", 310],
    ["External Hard Drive", 95],
    ["Webcam", 60],
    ["Laptop", 850]
]

#region kendi çözümüm

#endregion

#region hocanın çözümü

while True:
    #login mi sign in mi olsun diye sorduk
    first_process = input('Sign In --> 1\nSign Up -- 2\nTuşlayınız: ')
    match first_process:
        case '1':
            kullanici_adi = input('User Name: ')
            sifre = input('Password: ')
            
            is_exists = False #kullanıcı adı var mı diye kontrol ediyoruz
            for user in users: #bilgi birikimi henüz yetersiz, teker teker kontrol ediyoruz ^^
                if user[0] == kullanici_adi and user[1] == sifre:
                    is_exists = True
                    break
            
            if is_exists:
                print(f'Giriş başarılı..!\nHoşgeldiniz, {kullanici_adi}')
                while True:
                    second_process = input('İşlem Adı Giriniz: ')
                    
                    match second_process:
                        case 'toplam fiyat':
                            total = 0
                            for product in products:
                                total += product[1]
                            print(f'Toplam Fiyatlar: {total}')
                        case 'laptop toplam fiyat':
                            total = 0
                            for product in products:
                                if product[0] == 'Laptop':
                                    total += product[1]
                            print(f'Toplam Fiyatlar: {total}')
                        case 'ürün ara':
                            urun_adi = input('Ürün adı giriniz: ')
                            for product in products:
                                if product[0] == urun_adi:
                                    print(f'Ürün Adı: {product[0]}\nFiyatı: {product[1]}')
                            else:
                                print('Aradığınız ürün bulunmamaktadır..!')
                        case 'fiyat aralığına göre ara':
                            alt = int(input('Alt limit fiyato: '))
                            ust = int(input('Üst limit fiyato: '))
                            for product in products:
                                if product[1] >= alt and product[1] <= ust:
                                    print(f'Ürün Adı: {product[0]}\nFiyatı: {product[1]}')
                        case 'çıkış':
                            print('Uygulama kapatılıyor...!')
                            break
                        case _:
                            print('Lütfen doğru işlem türü giriniz..!')
            else:
                print('Kullanıcı adı yada şifre hatalı..!')
        case '2':
            kullanici_adi = input('User Name: ')
            sifre = input('Password: ')

            is_exist = False
            for user in users:
                if user[0] == kullanici_adi:
                    is_exist = True
                    break

            if is_exist:
                print('Kullanıcı adı zaten var.')
            else:
                new_user = [kullanici_adi, sifre]
                users.append(new_user)
                print('Üyelik işleminiz tamamlandı.')
        case _:
            print('Lütfen uygun işlem numarasını giriniz..!')

#endregion