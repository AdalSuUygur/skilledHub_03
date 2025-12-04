
#! Control Flow Statements / Karar Mekanizmaları (If-Else, Match-Case)
#* Belirli bir koşulun sağlanıp sağlanmamasına göre farklı kod bloklarının çalıştırılmasının standart yoludur.

#region If - Elif - Else
#? If - Elif - Else SYNTAX
#* if - elif - else bloğunda herhangi bir şart tutarsa diğer şartlara bakılmaz.
#* Mantıksal operatörler (and, or, not) kullanarak birden fazla karmaşık koşulu aynı anda kontrol etmeye olanak tanır.
kosul_1 = ""
kosul_2 = ""
if kosul_1:
    # Koşul_1 doğru ise bu blok çalışır
    print("Koşul 1 Doğru")
elif kosul_2:
    # Koşul_1 yanlış VE Koşul_2 doğru ise bu blok çalışır
    print("Koşul 2 Doğru")
else:
    # Yukarıdaki koşulların hiçbiri doğru değilse bu blok çalışır
    print("Hiçbiri Doğru Değil")

#todo Kullanıcıdan alınan 2 tane tam sayının büyük olanının hesabı
number_1 = int(input("Birinci sayı: "))
number_2 = int(input("İkinci sayı: "))

if number_1 > number_2 :
    print(f'{number_1} daha büyüktür {number_2}')
elif number_1 == number_2: 
    print("Her ikisi birbirlerine eşittir.")
else:
    print(f'{number_2} daha büyüktür {number_1}')

#todo Girilen sayının tek mi çift mi
#* Kendi çözümüm ^^ (Mod ifadesini bilmiyordum, bu şekilde çözdüm. BU KOD BLOĞU sana workaround'un her zaman olduğunu göstersin!)
#* GO GIRLLLLL!!!!!
number = float(input("Sayıyı giriniz: "))
sonuc = number / 2
if sonuc.is_integer() == True:
    print("Sayı çifttir")
else:
    print("Sayı tektir.")

#Mod ifadesi ile kolay çözümü :)
sayi = int(input('Bir sayi giriniz :'))
if sayi %2 == 0:
    print(f'{sayi} çift')
else:
    print(f'{sayi} tek')

#region Ternary If (Tek satır if)
#? Ternary If (Tek satır if) SYNTAX
#* Tek satırda if-else gibi düşün. Tek mi çift mi gibi tek şart olan durumlarda kullanılır.

#değişken = [True ise atanacak değer] if [koşul] else [False ise atanacak değer]
sayi = 0
sonuc = "Pozitif" if sayi > 0 else "Pozitif Değil (Sıfır veya Negatif)"

#todo Yaşını giren kullanıcının reşit olup olmaması durumunu kontrol eden ternary if
age = int(input("Your age: "))
status = "adult" if age >= 18 else "child"
print(status)

#todo Girilen sayının negatif mi pozitif mi olduğunu kontrol eden ternary if
number = int(input("Number: "))
print(f"Status {'positive' if number > 0 else 'negative'}") #f-string fonksiyonu içinde yazdık.

#todo Girilen sayının negatif mi pozitif mi olduğunu kontrol eden If-Elif-Else bloğu
number = int(input("Sayıyı giriniz: "))
if number > 0:
    print(f'Sayınız pozitiftir.')
elif number == 0:
    print("Sayınız nötrdür.")
else: 
    print("Sayınız negatiftir.")

#region Match-case yapısı:
#? Match-case yapısı:
#* if else'e alternatif olarak gelen bir yapı. (C ailesindeki switch-case) match-case status kontrolü için sıklıkla tercih edilir ancak case'de and/or kullanmak daha zor.
#* Genel olarak birebir uyum (==) sağlandığında case ifadesi daha tercih edilir.

#todo Subscription yapılan üyeliklerdeki statusu beliren uygulama
boxing_gloves_status = "passive"
match boxing_gloves_status:
    case "passive":
        pass
    case "active":
        pass
    case "modified":
        pass
    case _:
        print("None")

#todo Match case'te and ifadesinin kullanımı (ÇOK ZOR SAÇMA SAPAN SYNTAX)
kitap = 5
adet_kitap = int(input('Satın Alınan Kitap Sayısı: '))
if adet_kitap <= 0:
    print('Eksi kitap sayısı olamaz.')
else:
    match adet_kitap:
        case n if 1 <= adet_kitap <= 5: #if ile iç içe kullanıyoruz :)
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.95}')
        case n if 5 <= adet_kitap <= 10:
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.90}')
        case n if 10 <= adet_kitap <= 15:
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.85}')
        case n if 15 <= adet_kitap <= 20:
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.80}')
        case _:
            print('En fazla 20 kitap satın alabilirsiniz.')