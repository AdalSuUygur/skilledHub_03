
#! Exception Handling (Try-Except-Finally)
#* try-except-finally bloğu, programın çalışması sırasında oluşabilecek istisnaları (exceptions) yönetmek için kullanılan bir mekanizmadır.

# SYNTAX YAPISI
try: #Hata beklediğimiz kodları try bloğunun içine alıyoruz.
    bolunen = int(input("Bölünen: "))
    bolen = int(input("Bölen: "))
    sonuc = bolunen / bolen #bölen değerine 0 verirsek hata verir.
    print(sonuc)
except (ZeroDivisionError, ValueError) as err: #except satırına da beklediğimiz hatayı yazıyoruz ve takma isim veriyoruz.
    print("Hatalı giriş.")
    print(f'{err}')
finally: #ne olursa olsun bu bloğa gel ve bunu çalıştır anlamına gelir.
    print("Çalışıyor.") 

#? Her şeyi öngöremiyoruz ee neden her yere try-except yazmıyoruz. 
#? Çünkü try-except maliyetli bir işlemdir. İşlemin memory ve işlemciden yediği miktar maliyetini belirler.
try:
    pass
except Exception as err: #Burdaki tüm hepsine tüm hatalara bak demek. Bu da maliyeti iyice katlar. Çok nadir kullanılır.
    pass

#? Bazı durumlarda bilerek exception raise edilir. Mesela gelen data'da bir tanesinin mail adresinde @ yok, eklenmemiş.
try: 
    mail_adress = input("Type mail adress: ") #Normalde bu son kullanıcıdan gelmez, gelen datadan olur.
    if '@' not in mail_adress:
        raise TypeError('Mail adress have to containg "@"')
except TypeError as err:
    print(err)
    #Genelde log tutuluyor
    #Müşteri bilgilendirici feedback/mail gider
    #Notification sistemleri de çalışabilir
    #Kendimize mail atarız
    #Bazı sistemlerde ticket açılır ve görevlendirme yapılır vs vs.


#! Built-in Functions (Yerleşik Fonksiyonlar)

#* Python programlama dilinin en temel ve en sık kullanılan işlemler için doğrudan dilin içine gömülmüş olarak gelen fonksiyonlardır.
#* Bu fonksiyonları kullanmak için herhangi bir kütüphane veya modül indirmenize gerek yoktur. Python'ı kurduğunuz anda kullanıma hazırdırlar.

#? range() fonksiyonu - built in fonksiyon.
for i in range(19):
    print(i) #tek sayı verdik, başlangıç değeri 0, artış miktarı 1

for i in range(3,6):
    print(i) #2 değer verirsek ilk değer başlangıç, ikinci değer bitiş, artış miktarı 1

for i in range(5,65,3):
    print(i) #başlangıç, bitiş, artış miktarı olarak sıralandı.

#! Operatörler
#* Bir veya daha fazla işlenen, operand adı verilen değer üzerinde belirli bir matematiksel, mantıksal veya atama eylemini gerçekleştiren mekanizmalardır.

#? in operatörü
print('s' in 'su') #su içinde s varsa true döner
print('a' in 'su') #içinde mi diye sorar
#? not in operatörü
print('s' not in 'su') #su içinde s yoksa true döner
print('a' not in 'su') #içinde değil mi

#! Modülden Fonksiyon Çağırma
from random import randint #C ailesindeki randomizer gibi, farklı bir modül çağırmadım
#bu python içinde tanımlıdır ancak direkt kullanılmaz
#kullanılmak istenilince import edilinmeli

import random #olduğu gibi modülü importlar
from random import randint #burada ise random modülünden sadece randint fonksiyonu impotlanır, yani daha az maliyetli.

#? bir modülden 1-2 fonksiyon çağırılacaksa, spesifik olaral fonksiyonları çağırmak daha doğru (daha az maliyetli)
#? bir modülden 10 tane fonksiyon çağırılacaksa direkt modülün çağırılması daha doğru (daha az iş gücü)

random_number = randint(a = 0, b = 100)
print(random_number)