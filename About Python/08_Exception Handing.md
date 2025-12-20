---
description: >-
  try-except-finally bloğu, programın çalışması sırasında oluşabilecek
  istisnaları (exceptions) yönetmek için kullanılan bir mekanizmadır.
---

# Exception Handling

## Try - Except - Finally

Elimizde olmayan bir durumdan dolayı ya da;\
X firmanın yazdığı API'ye request atılan durumlarda;\
Bağlandığın veritabanında bağlantın kesildiyse vs. gibi olası hatalara karşı bu yapı kullanılır.

Bu yapıyı kullanırken end-user'ın yaptığı tüm hataları düşünmemelisin, çünkü end-user'ın yaptığı hatalar front-end yapısında farklı dillerle halledilir. Burada eğer kontrol etmeye kalkarsak server'a gidip gelinebilir, bu da cost-back sebebiyeti verir. Yani maliyeti artırır.

* `try`: Şüphelendiğiniz, yani hata oluşturma potansiyeli olan kod bloğunu içerir. Program bu kod bloğunu dener.
* `except`: `try` bloğu içinde bir hata (istisna) meydana gelirse, programın normal akışı durur ve kontrol hemen `except` bloğuna geçer. Bu blok, hatayı yakalar ve kullanıcıya yönelik bilgilendirici bir mesaj verme veya sorunu çözmeye çalışma gibi işlemleri gerçekleştirir.
* `finally`: İsteğe bağlıdır. `try` bloğu hata oluştursa da oluşturmasa da mutlaka çalıştırılması gereken kodları (örneğin, bir dosyayı kapatma, veritabanı bağlantısını sonlandırma) içerir.

```py
# SYNTAX YAPISI
#Hata beklediğimiz kodları try bloğunun içine alıyoruz.
try:
    bolunen = int(input("Bölünen sayı: "))
    bolen = int(input("Bölen sayı: "))
except ZeroDivisionError as err:
#except satırına da beklediğimiz hatayı yazıyoruz ve takma isim veriyoruz.
    print(err)
```

### Birden fazla hata gelebileceği durumlarda

```py
# SYNTAX YAPISI
try:
    bolunen = int(input("Bölünen sayı: "))
    bolen = int(input("Bölen sayı: "))
except (ZeroDivisionError, ValueError, TypeError) as err: #Parantez içine aldık
    print(err)
```

## finally Bloğu Kullanımı

`finally` bloğu, hata oluşsa da oluşmasa da her zaman çalışır, isteğe bağlı yazılır.

Genelde finally bloğu: veritabanına bağlan, hata alsan da almasan da bağlantıyı kopar veya, üst güvenlikli senaryolarda, başarılı olsan da olmasan da key'i kill et, bağlantıyı sonlandır gibi senaryolarda kullanılır.

```py
dosya = None # Dosyayı dışarıda tanımlıyoruz
try:
    dosya = open("veri.txt", "r")
    icerik = dosya.read()
except FileNotFoundError as err: #Dosya bulunamadı hatasında 
    #Kendimize mail attık
    #Log tuttuk
    print("Hata: Dosya bulunamadı.")
finally:
    # Dosya başarılı okunduysa da, hata oluştuysa da bağlantıyı kapat
    if dosya:
        dosya.close()
        print("Dosya bağlantısı kapatıldı.")
finally:
    #ne olursa olsun ben çalışırım demek.
    print("Çalışıyor.") 
```

Her şeyi öngöremiyoruz ee neden her yere try-except yazmıyoruz. Çünkü try-except maliyetli bir işlemdir. Bu yüzden arada bir yazıyoruz. Programın memory ve işlemciden yediği miktar maliyetini belirler.

```py
try:
         pass
except Exception as err:
##Burdaki tüm hatalara bak demek. 
##Bu da maliyeti iyice katlar. Bu sebeple çok nadir kullanılır.
         pass
```

## Exception Raise

Bazı durumlarda, developer bile/isteye exception raise eder, neden? Çünkü nereden hata geldiğini bulunmasına yardımcı olur.

```py
# Örneğin:
#Database'den gelen data'da bir tanesinin mail adresinde "@" yok, eklenmemiş.
try: 
    mail_adress = input("Type mail adress: ") 
    #Normalde bu son kullanıcıdan gelmez, gelen datadan olur.
    if '@' not in mail_adress:
        raise TypeError('Mail adress have to containg "@"')
except TypeError as err:
    print(err)
    #Genelde log tutuluyor
    #Müşteri bilgilendirici feedback/mail gider
    #Notification sistemleri de çalışabilir
    #Kendimize mail atarız
    #Bazı sistemlerde ticket açılır ve görevlendirme yapılır vs vs.
```

Uygulamada hangi tuşlara basıldı, en son ne yapıldı gibi kayıtların tutulmasına log denir.
