
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

#region Examples



#endregion
