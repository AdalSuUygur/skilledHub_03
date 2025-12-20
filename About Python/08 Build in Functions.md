
# Built-In Functions

Built-in Fonksiyonlar (Yerleşik Fonksiyonlar), Python programlama dilinin en
temel ve en sık kullanılan işlemler için doğrudan dilin içine gömülmüş olarak
gelen fonksiyonlardır.

Bu fonksiyonları kullanmak için herhangi bir kütüphane veya modül indirmenize gerek yoktur. Python'ı kurduğunuz anda kullanıma hazırdırlar.

Yerleşik fonksiyonlar, geliştiricilerin yaygın görevleri hızlı ve kolay bir şekilde yerine getirmesi için tasarlanmıştır. Kullanım amaçları şunlardır:

1. <mark style="color:$success;">Girdi/Çıktı İşlemleri:</mark> Kullanıcıdan veri almak (`input()`) veya ekrana bilgi yazdırmak (`print()`).
2. <mark style="color:$success;">Veri Tipi Dönüşümü:</mark> Bir verinin tipini değiştirmek (Örn: metni sayıya çevirmek için`int()`, sayıyı metne çevirmek için`str()`).
3. <mark style="color:$success;">Matematiksel İşlemler:</mark> Sayısal işlemler (Örn:`abs()` mutlak değer alma, `sum()`toplam alma).
4. <mark style="color:$success;">Veri Yapısı İşlemleri:</mark> Dizilerin, listelerin veya metinlerin uzunluğunu bulma (`len()`).

***ÖNEMLİ***:\
Fonksiyonlar, bir görevi yerine getiren komut gruplarıdır.\
Parantezler (`()`), Python'a bir fonksiyon çağrısı yaptığınızı gösterir.\
Parantez içine yazılan değerler (Örn: `print("Bu bir argümandır")` içindeki metin), fonksiyona gönderilen argümanlar (arguments) olarak adlandırılır.

## Built-in Functions vs Built-in Methods

Python'da metotlar (methods) ve fonksiyonlar (functions) birbiriyle yakından ilişkili kavramlardır, ancak önemli bir farkları vardır.

| **Özellik** | **Function** | **Method** |
| ------- | ------- | ------- |
| Ait Olduğu Yer | Bağımsızdır, herhangi bir nesneye ait değildir. | Belirli bir sınıfa ve o sınıfın nesnesine aittir. |
| Çağırma Şekli | Doğrudan adıyla çağrılır. (Örn: len(liste)) | Nesne üzerinden nokta ile çağrılır. (Örn: liste.append(eleman)) |
| Kullanım Amacı | Genel amaçlı görevler. | Nesnenin verilerini işlemek veya nesnenin durumunu değiştirmek. |
