
# LISTS II

## Sıralama Sanatı (Sorting)

Veri biliminde veriyi sıralamak, kritiktir.

print(sorted(numeric_lst)) #çıktı olarak lsite verdi, küçükten büyüğe sıraladı.
print(sorted(alpha_lst))

### A. `.sort()` (Yıkıcı Düzenleme)

Listenin kendisine müdahale eder ve **kalıcı olarak değiştirir**. Geri dönüşü yoktur.

* **Hafıza:** Ekstra yer kaplamaz (Memory efficient), çünkü yeni liste yaratmaz.
* **Tehlike:** Orijinal veriyi kaybedersin.

```python
sayilar = [5, 1, 9]
sayilar.sort() # Listeyi olduğu yerde değiştirdi.
print(sayilar) # Çıktı: [1, 5, 9]

# ⚠️ Sık Yapılan Hata:
# yeni_liste = sayilar.sort() -> YANLIŞ!
# sort() geriye 'None' döndürür. yeni_liste boş kalır.

```

### `sorted()` (Güvenli Kopya)

Orijinal listeye dokunmaz, sana sıralanmış **yeni bir kopya** verir.


#? sorted() buil-in-function
#* Listedeki elemanları sıralayıp YENİ BİR LİSTE döndürür.

* **QA Refleksi:** "Test verisini bozmadan analiz yapmam lazım" diyorsan bunu kullanmalısın.

```python
sayilar = [5, 1, 9]
yeni_sayilar = sorted(sayilar)

print(sayilar)      # Çıktı: [5, 1, 9] (Hala eski halinde, bozulmadı!)
print(yeni_sayilar) # Çıktı: [1, 5, 9] (Yeni kopya)

```

> **İpucu:** Tersten sıralamak için her ikisinde de `reverse=True` parametresini kullanabilirsin.
> `sorted(sayilar, reverse=True)`

---

## 2. Bölüm: Matrix (İç İçe Listeler) 🏢

Excel tabloları, satranç tahtaları veya görüntü işleme (pikseller)... Hepsi aslında satır ve sütunlardan oluşur. Python'da bunu **Liste içinde Liste** (Nested Lists) ile yaparız.

Bunu bir apartman gibi düşün:

* Dış liste: Apartman
* İç listeler: Katlar
* Elemanlar: Daireler

```python
# 3 Satır, 3 Sütunlu bir matris
matris = [
    [1, 2, 3],  # 0. İndeks (Satır 0)
    [4, 5, 6],  # 1. İndeks (Satır 1)
    [7, 8, 9]   # 2. İndeks (Satır 2)
]

# Hedef: 6 sayısını çekmek (Satır 1, Sütun 2)
# Formül: matris[satir_indexi][sutun_indexi]

print(matris[1])    # Çıktı: [4, 5, 6] (Tüm satır gelir)
print(matris[1][2]) # Çıktı: 6 (Nokta atışı)

```

---

## 3. Bölüm: Join & Split (Metin Cerrahlığı) ✂️

Burası Veri Bilimi kariyerinde **en çok** kullanacağın yerlerden biri. Özellikle o bahsettiğin NLP projelerinde, tweetleri kelimelerine ayırırken (`Tokenization`) sürekli bunu yapacaksın.

#### A. `.split()` (Parçala)

Metni, belirlediğin bir "ayırıcıya" göre böler ve **LİSTE** döner.

```python
veri = "Python,Java,C++"
diller = veri.split(",") # Virgüle göre ayır
print(diller) # ['Python', 'Java', 'C++']

```

### B. `.join()` (Birleştir)

Listeyi alır, aralarına belirlediğin "yapıştırıcıyı" koyarak **STRING** (Metin) yapar.
*Dikkat: Yazımı biraz terstir. Önce yapıştırıcı yazılır.*

```python
kelimeler = ["Veri", "Bilimi", "Harika"]
cumle = " ".join(kelimeler) # Boşluk ile birleştir
print(cumle) # "Veri Bilimi Harika"

```

---

### 🛠️ GÖREV ZAMANI (HARDCORE)

Verdiğin görev listesi şahane. Şimdi senden şu **"Veri Temizleme ve Birleştirme"** uygulamasının kodunu bekliyorum.

**Senaryo:** `veri = "ahmet, canan, berke, deniz, elif"`

1. Bu string'i virgüle göre bölüp listeye çevir.
2. Listeyi alfabetik sırala (`sort` veya `sorted`, seçim senin ama neden seçtiğini söyle).
3. İsimlerin ilk harflerini büyütebilirsen bonus puan (Opsiyonel: `.capitalize()` metodu stringlerde çalışır, döngü gerekebilir).
4. Aralarına tire `-` koyarak birleştir.
5. Sonucu ekrana bas.

### 🧠 LeetCode 1470: Shuffle the Array İçin İpucu

Soru sana `[x1, x2, y1, y2]` formatında bir liste ve `n` sayısı (listenin yarısı) verecek.
Senden `[x1, y1, x2, y2]` şeklinde "fermuar gibi" birleştirmeni istiyor.

**Algoritma Önerisi:**

1. Listeyi tam ortadan ikiye böl (`slicing` ile `x_parcasi` ve `y_parcasi` elde et).
2. Bir döngüyle (`range(n)`) her iki parçadan sırayla eleman alıp yeni bir `sonuc` listesine ekle (`append`).

Haydi bakalım! 7. Günü de zaferle kapatalım. Kodlarını bekliyorum! 🚀


Harika bir öfke bu! :) Ciddiyim, bu tepki senin sadece "kodu kopyalayan" biri değil, "sistemi sorgulayan" bir mühendis zihniyetine sahip olduğunu gösteriyor.

**Tespitin %100 doğru.**

Fark tam olarak **Built-in Functions (Gömülü Fonksiyonlar)** ve **Built-in Methods (Gömülü Metotlar)** farkıdır.

Neden şimdiye kadar bu isimlerle ayırmadık? Çünkü programlama pedagojisinde önce **"araba sürmeyi"** (kodu kullanmayı) öğretiriz, sonra **"motorun parçalarını"** (teorik isimleri) anlatırız. Eğer ilk gün "Bu bir metottur, bu bir fonksiyondur" diye girseydik, çoğu kişi "Bu ne karmaşık iş" deyip bırakırdı.

Ama sen 7. günde bu farkı kendi kendine yakaladın. O zaman gel, bu "ezberi" bozalım ve mantığını oturtalım.

---

### Fonksiyon (Function) vs. Metot (Method) Farkı

Bu tabloyu zihnine kazıdığında bir daha asla karıştırmayacaksın.

#### 1. Fonksiyonlar (Functions) - "Genel Hizmetçiler"

Bunlar Python'un her yerinde çalışan, bağımsız araçlardır. Kimi çağırırsan ona hizmet eder.

* **Sözdizimi:** `fonksiyon_ismi(veri)`
* **Özellik:** Parantezin içine veriyi alır, işler ve sonucu verir.
* **Örnekler:**
* `print("Selam")` -> Ekrana basma fonksiyonu.
* `len(liste)` -> Uzunluk ölçme fonksiyonu.
* `type(veri)` -> Tip kontrol etme fonksiyonu.
* `sorted(liste)` -> Sıralama fonksiyonu.



#### 2. Metotlar (Methods) - "Kişisel Yetenekler"

Bunlar bağımsız değildir. Bir nesneye (Object) aittirler. Sadece o nesne türüyle çalışırlar.

* **Sözdizimi:** `nesne.metot_ismi()` (Nokta operatörüne dikkat!)
* **Özellik:** O nesnenin "içindeki" bir özelliktir. Veriyi paranteze almaz, **noktadan önceki** veriyi kullanır.
* **Örnekler:**
* `liste.append(5)` -> Sadece listelerde vardır. (String'e append yapamazsın).
* `metin.upper()` -> Sadece stringlerde vardır. (Sayıyı upper yapamazsın).
* `liste.sort()` -> Listenin kendi metodudur.



---

### Neden İkisi de Var? (sorted vs .sort)

Senin asıl kızdığın nokta: *"Neden hem `sorted()` var hem `.sort()` var?"*

1. **`sorted(veri)` (Fonksiyon):**
* Geneldir. Sadece listeyi değil, her türlü sıralanabilir şeyi (tuple, dictionary keys) sıralar.
* **Görevi:** "Bana verdiğin şeye dokunmadan, onun sıralı bir **kopyasını** sana vereyim."


2. **`veri.sort()` (Metot):**
* Özeldir. Sadece listeler üzerinde tanımlıdır.
* **Görevi:** "Ben direkt bu listenin iç yapısını değiştiririm. Kopya mopya yok, **orijinali bozarım**."



### Özetle

Senin "saçma sapan" dediğin şey aslında Python'un sana sunduğu **"Seçme Özgürlüğü"**:

* Verim kalsın, sonucunu göreyim diyorsan -> **Fonksiyon** (`sorted`)
* Verim değişsin, hafızada yer kaplamasın diyorsan -> **Metot** (`.sort`)

Kızgınlığın geçtiyse ve mantığı oturduysa, bu farkındalıkla görevlere tekrar bakalım mı? Artık ezberlemiyorsun, alet çantasındaki tornavida ile matkabın farkını biliyorsun. :)

Hadi şimdi o "Veri Temizleme ve Birleştirme" görevini bu bilinçle parçala! Bekliyorum.