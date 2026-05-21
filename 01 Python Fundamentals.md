
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

* Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.
* Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance.
* Python supports modules and packages, which encourages program modularity and code reuse.
* The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.
<https://www.pulumi.com/why-is-python-so-popular/>

1. Python is easy to learn, since its close to standart English
2. Python has an active, supportive community
3. Python is flexible
4. Python offers versatile web-development solutions
5. Python is well suited to data science and analytics
6. Python is efficient, fast, and reliable
7. Python is widely used with IoT Technology
8. Python empowers custom automation
9. Python is the academic language




# Python'a Giriş, Sözdizimi ve Veri Bilimi İçin Temel Yapı Taşları

⚠️ Hayati Kural: Girinti (Indentation)

**UNUTMA Kİ:** Python'da karar blokları, girintileme (indentation) ile belirlenir.

Python der ki: *"Eğer bir satır içeriden başlıyorsa, o satır üstteki bloğa aittir."*

> **Öğretmen Notu:** Python'da "Her şey bir nesnedir (Everything is an object)". Yani 10 sayısı bile bellekte kendine has özellikleri olan bir varlıktır. Değişkenler sadece o varlıkları parmağıyla gösteren işaretçilerdir.


## Neden Python?

**Python is an interpreted (yorumlayıcı), object-oriented(nesne yönelimli), high-level(yüksek seviyeli) programming language with dynamic semantics.**

* Python , Veri Bilimi ve Yapay Zeka için sektör standardıdır.

* Geniş Kütüphane Desteği: NumPy, Pandas, Scikit-learn, TensorFlow gibi YZ ve veri işleme kütüphanelerine kolay erişim sağlar.

1. Python is flexible
2. Python offers versatile web-development solutions
3. Python is well suited to data science and analytics
4. Python is efficient, fast, and reliable
5. Python is widely used with IoT Technology
6. Python empowers custom automation
7. Python is the academic language
