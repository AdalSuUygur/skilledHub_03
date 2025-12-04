
#! LOOPS: 
#* Tekrarlı işleri yaparken tercih edilen yazılım konsepti.

#region While Loop
#? While Loop
#* Belirli bir koşul True olduğu sürece içerisindeki kod bloğunu çalıştırmaya devam eder. 
#* Ne zaman duracağını, yani sayacı veya koşulu değiştirmeyi programcının kendisi yönetmelidir.

# SYNTAX YAPISI
counter = 0 #Sayaç, çözülen problemin bağlamında başlangıç değeri ile başlar.
while counter <= 9: #Anahtar kelimesi while, ve şart kelimesi.
    print(counter)
    counter = counter + 1 #counter += 1 şeklinde de yazılabilir.
    # Koşulu değiştiren adım yazılmazsa sonsuz döngü olur

#? Sonsuz döngü
#* Bir döngünün durma koşulunun hiçbir zaman sağlanamadığı (yani koşulun sürekli True kaldığı) durumdur. İsteyerek oluşturulur.

#SYNTAX YAPISI
while True:
    print(counter) #Döngüden çıkılmadığı için sonsuza dek counter'ı yazdıracak ne olursa olsun.
    break #Döngüden çıkması için break yazılır.

#todo anket cevapları alınan uygulamada 3 kez hayır girilirse döngünün sonlandığı uygulama
counter = 0
while True:
    cevap = input("Evet/Hayır: ").lower()
    match cevap:
        case "evet":
            counter = 0
        case "hayır":
            counter += 1
            if counter == 3:
                print("Anket katılımı iptal edildi.")
                break
        case _:
            print("Girdiniz evet ya da hayır dışında, lütfen girdinizi kontrol ediniz.")

#endregion

#region For Loop
#? FOR DÖNGÜSÜ
#* bir koleksiyonun elemanları üzerinde veya belirli bir sayı aralığı üzerinde sırayla ilerlemek (iterate etmek) için kullanılan döngüdür.

# SYNTAX YAPISI
isim = "Python"
# 'isim' (string) içindeki her bir harf için döngüyü çalıştır
for harf in isim: #burada harf olarak adlandırılan şey, takma/geçici isim.
    print(harf)

#todo Girilen başlangıç bitiş ve artış miktarlarına göre for döngüsü kurulumu
start = int(input("Başlangıç: "))
finish = int(input("Bitiş: "))
step = int(input("Artış miktarı: "))
for i in range(start, finish, step):
    print(i,end=" ")

#todo 0-100 arası sayıların ekrana yazdırılması uygulaması
for i in range(0,100):
    print(i, end="-")

#endregion