


#! join() Metodu
#* join() metodu, bir iterable (liste, tuple, küme, dize vb.) içindeki tüm elemanları birleştirerek 
# tek bir dize (string) oluşturan bir dize (string) metodudur. 
# Birleştirme sırasında, metodun çağrıldığı dize, elemanlar arasına ayırıcı olarak eklenir.
#f formating +larla birleştirmek gibi, +larla neden birleştirmek yeirne join, çünkü stringler değiştirilemez yapılardır ve + ile eklendiğinde yeni bir string oluşturulur
#bu da haliyle maliyet demek, artılarla birleştirme, bu amatörce.


#? join fonksiyonu çok önemli bir fonksiyondur.
#* string birleştirme mevzusu var, iki string ifadeyi birleştirmek için " " = "" + "" gibi kullanılır, fstring içinde de benzer.
#* stringler değiştirilemez yapılardır, iki string ifadeyi birleştirince ramde farklı bir yere yazdırır (memory leake sebep olur) bundan dolayı daha az maliyetli olan join kullanılır.
#stringler immutable olduğu için.
#tekrar yer kaplamasın diye

#* Önemli Not: join() metodu, ayırıcı (separator) olarak kullanılacak olan dize üzerinde çağrılır, birleştirilecek iterable üzerinde değil.



# Built in Methods

Bir metot, bir nesneye ait olan ve o nesne üzerinde işlem yapmak için kullanılan bir fonksiyondur.

Temel olarak, bir metot, bir sınıf (class) içinde tanımlanan bir fonksiyondur ve sadece o sınıftan türetilmiş nesneler (örneğin bir dize, liste veya kendi oluşturduğunuz bir sınıf nesnesi) tarafından çağrılabilir.

## Built in Methods SYNTAX

Metotlar, her zaman bir nesne üzerinden, nokta (.) operatörü kullanılarak çağrılır:
$$\text{nesne}\textbf{.metot\_adı}(\text{argümanlar})$$

**Metodun İlk Argümanı:** selfSınıflar içinde tanımlanan metotların ilk parametresi her zaman self olur.
Bu parametre, metodun çağrıldığı nesnenin kendisine (instance) referans verir ve Python tarafından otomatik olarak sağlanır.

## Metotlar Ne Zaman Kullanılır?

Metotlar, bir nesneye ait eylemleri veya davranışları tanımlamak için kullanılır.
İki ana kullanım alanı vardır:

### Yerleşik (Built-in) Nesnelerin Davranışını Kullanma

Python'da en sık kullanılan veri tiplerinin (dize, liste, sözlük vb.) kendilerine ait hazır metotları vardır.

Dizeler (Strings): Dizeyi büyük harfe çevirmek, belirli bir karakteri aramak, ayırmak/birleştirmek gibi işlemler için kullanılır.

_Örnek: isim = "ali" $\rightarrow$ isim.upper() $\rightarrow$ "ALI"_

_Örnek: yazi = "merhaba dünya" $\rightarrow$ yazi.split(" ") $\rightarrow$ ['merhaba', 'dünya']_

Listeler (Lists): Listeye eleman eklemek, çıkarmak, sıralamak gibi listeyi yönetme işlemleri için kullanılır.

_Örnek: liste = [1, 2] $\rightarrow$ liste.append(3) $\rightarrow$ [1, 2, 3]_

_Örnek: liste.sort()_

### Kendi Sınıflarınızın Davranışını Tanımlama

Nesne Yönelimli Programlama (OOP) yaparken, kendi oluşturduğunuz sınıflara özellikler (attributes) ve metotlar (methods) eklersiniz.

Metotlar, bu nesnelerin yapabileceği eylemleri tanımlar.

Örnek: Bir Araba sınıfı düşünün.
Araba'nın nitelikleri (özellikleri): renk, model, hız.
Araba'nın metotları (davranışları): calistir(), hizlan(), fren_yap().

```py
class Araba:
    def __init__(self, model, hiz=0): # Başlatıcı (constructor) metot
        self.model = model
        self.hiz = hiz

    def hizlan(self, miktar): # Nesnenin kendi metodu
        self.hiz += miktar
        print(f"{self.model} hızı şimdi {self.hiz}.")
```

#### Kullanımı

```py
araba_objesi = Araba("Sedan")
araba_objesi.hizlan(50) # Metot, nesne üzerinden çağrıldı
```

Metotlar, nesneye özel verilerle çalışarak programınızı daha modüler, anlaşılır ve nesne tabanlı hale getirmenin anahtarıdır.

```py
class Araba:
    def __init__(self, model, hiz=0): # Başlatıcı (constructor) metot
        self.model = model
        self.hiz = hiz

    def hizlan(self, miktar): # Nesnenin kendi metodu
        self.hiz += miktar
        print(f"{self.model} hızı şimdi {self.hiz}.")

araba_objesi = Araba("Sedan")
araba_objesi.hizlan(50) # Metot, nesne üzerinden çağrıldı
```
