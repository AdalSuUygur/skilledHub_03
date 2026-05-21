
# PYTHON HAKKINDA HER ŞEY

## Müfredat

### Python Fundamentals

* 1\. Değişkenler ve Veri Tipleri
* 2\. Karar Yapıları ve Döngüler
* 3\. Hata Yönetimi
* 4\. Liste, Tuple, Dictionary kullanımı
* 5\. Lambda, List/Dict/Set Comprehension
* 6\. Map, Filter, Reduce, Zip, Enumerate
* 7\. Fonksiyonlar
* 8\. Dosya İşlemleri, HTTP İstekleri, JSON
* 9\. Pythonic Thinking

## Ödev

### 1\. Python Temelleri

* 1\. Python nedir? Neden bu kadar popüler?
* 2\. Değişkenler, veri tipleri (int, float, str, bool, list, dict vs.)
* 3\. Koşul ifadeleri (if, elif, else) nasıl çalışır?
* 4\. Döngüler (for, while) ve kullanımları
* 5\. Fonksiyon tanımı ve parametre yapısı
* 6\. Python’da hata yönetimi (try, except, finally)
* 7\. Python dosya işlemleri (okuma, yazma, append)
* 8\. Python’da modül ve paket kavramı nedir?

## Çözümler

### Python nedir?

<https://www.python.org/doc/essays/blurb/>

**Python is an interpreted(yorumlayıcı), object-oriented(nesne yönelimli), high-level(yüksek seviyeli) programming language with dynamic semantics.**

* Yüksek Seviyeli Programlama Dili (High-level Programming Language): Günlük hayattaki konuşma diline yakın komutlar içeren programlama dilleridir.

*Programlama dili makine diline yaklaştıkça yüksek seviyeden low level'a geçiş yapar.*

Bilgisayar 0-1'lerden oluşan makine kodlarını (low level code) anlar, insanlar ise yüksek seviyeli dil ile program yazar.

Program dili ile yazılan kodun bilgisayarda çalışabilmesi için makine koduna çevrilmesi gerekir, bu da "Compiler" veya "Interpreter" ile sağlanır.

Yani: compiler ve interpreter, yüksek seviyeli bir dil ile yazılmış programı, bilgisayarın anlıyacağı makine koduna çeviren programlardır.

* Compiler tüm kodu alıyor, hepsini bilgisayarın anlayabileceği bir ara koda dönüştürüyor ve ondan sonra bilgisayar hepsini okuyor. Bu da toptan hata vermesi demek, tekrar bir kod çevirmesi yaptığı için de memory maliyeti demek.

* Interpreter dili ise aslında aynı işi yapıyor ancak toptan kodu çevirmek yerine satır satır çeviriyor, bu yüzden compiler dillere nazaran daha yavaş çalışıyor. Burdaki avantaj ise hataları teker teker vermesi, sırasıyla ilerlediği için ilk hata gördüğü noktada program duruyor.

*In a compiler, the process requires two steps in which firstly source code is translated to target program then executed. While in Interpreter It’s a one-step process in which Source code is compiled and executed at the same time.*

**Dynamic semantics dilde ise tanımlanan değişkenin türü program çalıştırılırken(runtime) belirlenir.**

Diğer programlama dillerinde önce tip çapalanır (tanımlanır) ancak python'da buna gerek yoktur çünkü pythonda değişkenler içerisine atılan value'nun tipine bürünür. Yani Pythonda değişkenler tip bağımlı değillerdir.

* Interpreter, siz bir değer atadığınız anda (runtime sırasında) o değeri kontrol eder ve değişkenin tipini otomatik olarak belirler. *Bunun tamamına duck typing denir.*

#### Duck Typing

* Duck Typing (Ördek Tiplemesi), Python'ın dinamik tiplendirmesinin bir uzantısıdır. Temel felsefesi şudur: *"Eğer bir şey ördek gibi yürüyorsa ve ördek gibi vaklıyorsa, onun ne olduğunun önemi yok, o bir ördektir."*

**Programlamadaki anlamı:** Bir nesnenin tipi değil, sahip olduğu metodlar ve özellikler önemlidir. Python, bir nesnenin belirli bir işlemi yapıp yapamayacağını, nesnenin resmi tipini kontrol etmeden, doğrudan o metodu çağırarak dener.

OOP NEDİR

### Python neden bu kadar popüler?

----------

### 2. Boşlukların Önemi (Indentation)

*Pythonda boşluklar çok önemli.*&#x20;

*IndentationError: unexpected indent (beklenmedik boşluk).*&#x20;

*Boşluklu bir tanımlama yapınca bu hata gelir. Çünkü Syntax yapısında boşluklar oldukça önemli. Pythonda bırakılan boşluklar kodların yaşam alanını belirler.*
{% endhint %}

* Python'da diğer dillerdeki gibi kod bloklarını tanımlamak için süslü parantezler veya farklı ifadeler yerine girinti (identation) kullanılır. Bu, Python kodunun doğal olarak daha okunaklı ve düzenli olmasını sağlar (zorunlu okunaklılık).

----------------

`+` ile String Birleştirme: Bu doğrudur. Python'da stringleri birleştirmek için `+` operatörü kullanılır. Ancak performans açısından büyük birleştirme işlemleri için `.join()` metodunun kullanılması daha iyi bir uygulamadır.

.py Uzantısı: Python kaynak kod dosyaları `.py` uzantısını kullanır.

### Modül Nedir?

Bir Modül (Module), basitçe bir `.py` uzantılı Python dosyasıdır. Bu dosya, başka bir programda kullanabileceğiniz sınıflar, değişkenler ve özellikle fonksiyonlar gibi kod tanımlamaları içerir.

Modüller, kodunuzu mantıksal olarak organize etmenizi ve parçalara ayırmanızı sağlar.

**Neden Önemlidir?**

1. Kod Tekrarı Önleme (Reusability): Bir kere yazılan bir fonksiyonu (örneğin bir matematik hesaplaması) farklı projelerde tekrar tekrar kullanabilme imkanı sunar.
2. Organize Etme: Büyük projeleri daha küçük, yönetilebilir dosyalara bölerek kodun okunurluğunu artırır.
3. Python Standart Kütüphanesi: Python, kurulumla birlikte gelen standart kütüphane adı verilen devasa bir modül koleksiyonuna sahiptir (örneğin, notlarınızdaki `random`, `math`, `os` gibi).

### `import` Nedir ve Nasıl Kullanılır?

`import` ifadesi, Python'da bir modülde tanımlanmış kodları mevcut programınıza dahil etmek için kullanılan anahtar kelimedir. Bir modülü içeri aktarmanın temelde iki yolu vardır ve bu yollar verimlilik ve kullanım kolaylığı açısından farklılık gösterir:

#### 1. Tam Modül İçe Aktarma (`import modül_adı`)

Bu yöntem, modüldeki tüm içeriği programa dahil eder.

```py
import random
```

Kullanım: İçerideki bir fonksiyonu kullanmak için modül adını ön ek olarak kullanmanız gerekir.

```py
rastgele_sayi = random.randint(0, 100)
#               ^ Modül adı
```

* Ne Zaman Kullanılır?
  * O modülden çok sayıda fonksiyon veya nesne çağıracaksanız.
  * Farklı modüllerde aynı isimde fonksiyonlar varsa, isim çakışmasını önlemek için.

#### 2. Belirli Fonksiyonları İçe Aktarma (`from modül import fonksiyon`)

Bu yöntem, bir modülün tamamını değil, sadece ihtiyaç duyduğunuz belirli işlevleri programa dahil eder.

```py
from random import randint
```

Kullanım: Fonksiyonu çağırırken modül adını kullanmaya gerek yoktur.

```py
rastgele_sayi = randint(0, 100) # Doğrudan çağırıldı
```

* Ne Zaman Kullanılır?
  * Bir modülden sadece 1-2 fonksiyon çağıracaksanız.
  * Bu, daha az maliyetli ve daha temiz bir koddur çünkü Python'ın belleğine sadece gerekli olan kod yüklenir.

### Control Flow Statements (If-elif-else, match-case)

Belirli bir koşulun sağlanıp sağlanmamasına göre farklı kod bloklarının çalıştırılmasının standart yoludur.

### LOOPS

Python dilinde tekrarlı işlemleri gerçekleştirmek için kullanılan iki temel döngü (loop) yapısı vardır: `while` döngüsü ve `for` döngüsü. Bu döngüler, bir görevi belirli koşullar altında veya belirli bir eleman koleksiyonu üzerinde tekrar tekrar çalıştırmak için tercih edilen yazılım konseptleridir.



### TRY-EXCEPT-FINALLY

`try-except-finally` bloğu, programın çalışması sırasında oluşabilecek istisnaları (exceptions) yönetmek için kullanılan bir mekanizmadır. Bu kullanılıyorsa, uygulama arka tarafta exception vermiştir yani developerın kestiremediği bir durum oluşmuştur.
