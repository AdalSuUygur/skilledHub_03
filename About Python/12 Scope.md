# 📚 Python Temelleri ve Yapay Zeka Hazırlık Müfredatı (Ders 1-4)

Bu müfredat, bir Yapay Zeka ve Veri Bilimi uzmanı olmak için gerekli olan temel Python programlama ve bilgisayar bilimi kavramlarını kapsar.

---

## I. Ders 1: Python'a Giriş, Sözdizimi ve Değişkenler

### 1. Neden Python?
* Sektör Standardı (Veri Bilimi, YZ, Makine Öğrenimi).
* Yüksek Okunabilirlik ve Basit Sözdizimi (Syntax).
* Geniş Kütüphane Ekosistemi (NumPy, Pandas, vb.).

### 2. Python Ortamı ve Sözdizimi
* **Yorumlayıcı (Interpreter):** Kodun çalıştırıldığı araç.
* **Jupyter Notebooks:** Etkileşimli kod çalıştırma ortamı (Veri Biliminde temel araç).
* **Girintileme (Indentation):** Python'da kod bloklarını tanımlar (**4 boşluk**).

### 3. Veri ve Değişkenler
* **Değişkenler:** Bellekteki değerlere atanan etiketler (`=` operatörü).
* **Temel Veri Tipleri:**
    * `int` (Tam Sayılar: `42`).
    * `float` (Ondalıklı Sayılar: `3.14`).
    * `str` (Karakter Dizileri/Metin: `"Python"`).
    * `bool` (Doğruluk Değeri: `True` / `False`).

### 4. Operatörler ve Fonksiyonlar
* **Aritmetik Operatörler:** `+`, `-`, `*`, `/`, `**` (Üs alma).
* **Built-in Functions (Yerleşik Fonksiyonlar):** Her zaman ve her yerden çağrılabilen genel komutlar.
    * `print()`: Ekrana çıktı verme.
    * `type()`: Bir değişkenin tipini kontrol etme.

---

## II. Ders 2: Kontrol Akışı ve Listelere Giriş

### 1. Karar Verme ve Mantıksal Operatörler
* **Boolean Mantık:** Karar verme mekanizmasının temelini oluşturan `True` ve `False` değerleri.
* **Karşılaştırma Operatörleri:** Değerleri karşılaştırmak için kullanılır (`==`, `!=`, `>`, `<`).
* **Mantıksal Operatörler:** Koşulları birleştirmek için kullanılır.
    * `and` (VE): Tüm koşullar doğru olmalı.
    * `or` (VEYA): En az bir koşul doğru olmalı.

### 2. Kontrol Akışı (If/Elif/Else)
* `if`: Bir koşulun doğru olup olmadığını kontrol eder.
* `elif`: Başka bir koşulu kontrol eder (önceki `if` yanlışsa).
* `else`: Yukarıdaki hiçbir koşul doğru değilse çalışır.

### 3. Veri Yapıları: Listeler
* **Tanım:** Sıralı, **değiştirilebilir (Mutable)** öğe koleksiyonları. Köşeli parantez (`[]`) ile oluşturulur.
* **İndeksleme:** Öğelere pozisyon numarası ile erişim (**0'dan başlar**).
* **Dilimleme (Slicing):** Listenin bir bölümünü alma (`liste[başlangıç:bitiş:adım]`).
* **Liste Metotları (Methods):** Listeye ait, nokta (`.`) ile çağrılan eylemler.
    * `.append()`: Sona eleman ekleme.
    * `.pop()`: Eleman çıkarma.
    * `.sort()`: Sıralama.

---

## III. Ders 3: Döngüler ve Gelişmiş Veri Yapıları

### 1. Döngüler (Loops) - Otomasyon
* **`for` Döngüsü:** Bir koleksiyondaki her öğe üzerinde sırayla (iterasyon) işlem yapmak için kullanılır.
    * `range()`: Belirli bir sayı aralığında döngü oluşturmak için kullanılır.
* **`while` Döngüsü:** Bir koşul doğru olduğu sürece çalışmaya devam eden döngü.
* **Kontrol İfadeleri:**
    * `break`: Döngüyü anında durdurur.
    * `continue`: Mevcut iterasyonu atlar, bir sonrakine geçer.

### 2. İkinci Seviye Veri Yapıları
* **Tuples (Demetler):** Sıralı, **değiştirilemez (Immutable)** koleksiyonlar. Parantez (`()`) ile oluşturulur.
* **Sets (Kümeler):** **Sırasız**, **benzersiz** öğeler koleksiyonu. Yinelenen verileri filtrelemede kullanılır.
* **Dictionaries (Sözlükler):** **Anahtar-Değer (Key-Value)** çiftleri halinde veri depolama.
    * Metotlar: `.keys()`, `.values()`, `.items()`.

### 3. İleri Kodlama Teknikleri
* **List Comprehension (Liste Anlayışları):** Döngüleri ve koşulları tek bir satırda birleştirerek listeler oluşturmanın hızlı ve okunaklı yolu.

---

## IV. Ders 4: Fonksiyonlar, Modüller ve Kapsam

### 1. Fonksiyonlar - Yeniden Kullanılabilirlik
* **Tanımlama:** `def` anahtar kelimesi ile bir görevi yerine getiren kod bloğu oluşturma.
* **`return`:** Fonksiyonun hesapladığı değeri geri döndürmesi.
* **Parametreler/Argümanlar:** Fonksiyonun dışarıdan aldığı girdiler.
    * **Varsayılan Argümanlar:** Fonksiyon çağrılmazsa kullanılan önceden belirlenmiş değerler.
* **Lambda Fonksiyonları:** Tek satırlık basit işlemler için hızlıca yazılan anon