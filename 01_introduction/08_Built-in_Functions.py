
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





tempolar = [22, 18, 35, 14, 42, 10, 27, -5, 50]
sabah_verileri = tempolar[:3]
orta_eleman = len(tempolar) // 2
sicak_gunler = []

for tempo in tempolar:
    if tempo >= 30:
        sicak_gunler.append(tempo)


#### 🧠 LeetCode 2011: Final Value of Variable After Performing Operations

Bu soru tam bir "Liste içinde For döngüsü ile gezinme" sorusudur.

* `X++` veya `++X` görürsen değeri 1 artır.
* `X--` veya `--X` görürsen değeri 1 azalt.
* Başlangıç değerin 0.

Notlarını, "Bozma Testi" sonucunu ve kodlarını bekliyorum! Bu konuyu halledersek veri biliminin %50'si cebe girdi demektir. Başlayalım! 🚀

