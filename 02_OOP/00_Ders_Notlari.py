
#! PyCharm ve OOP (Object-Oriented Programming) Temelleri
# Bu bölüm, PyCharm IDE'sinin **OOP** prensiplerini görselleştirmede sağladığı avantajları ve **Inheritance** (Kalıtım) mekanizmasının teknik detaylarını kapsar.

#? PyCharm Visual Indicators (Görsel İşaretçiler)
# PyCharm, kodun okunabilirliğini artırmak için **Base Class** (Ata Sınıf) ve **Child Class** (Alt Sınıf) arasındaki ilişkiyi sembollerle gösterir:

#* **Is overridden in [ChildClass]:** Ata sınıftaki bir metodun yanında, aşağı yönlü bir ok bulunur. Bu, metodun alt sınıfta yeniden yazıldığını gösterir.
#* **Overrides method in [BaseClass]:** Alt sınıftaki metodun yanında, yukarı yönlü (genellikle kırmızı/mavi) bir ok bulunur. 
# Bu, metodun atadan miras alındığını ve değiştirildiğini belirtir.

#? Method Overriding ve `__init__` Yönetimi

# Method Overriding, ata sınıftan gelen bir metodun alt sınıfta ihtiyaca göre yeniden tanımlanmasıdır.

#* **Override Zorunluluğu:** Teknik olarak zorunlu değildir. Alt sınıf, ata sınıfın metodunu aynen kullanabilir. Ancak özelleştirme gerekiyorsa override edilir.
#* **`super().__init__` Kullanımı:**
#* Eğer bir **Child Class** içinde `__init__` fonksiyonu tanımlanırsa, Python ata sınıfın `__init__` fonksiyonunu otomatik olarak **çağırmaz**.
#* **BaseEntity** (Ata) içindeki özelliklerin (attributes) de yüklenmesi için `super().__init__()` (veya `BaseClass.__init__`) çağrısı **zorunludur**.
#* *Uyarı:* IDE (Örn: PyCharm), ata sınıfın `__init__`'i çağrılmadığında "Call to init of super class is missed" uyarısı verir.

# **Önemli Not:** Bir sınıfta `__init__` fonksiyonu override edildiğinde, var olan fonksiyonu "genişletmiş" (extend) olursunuz. Ancak aynı scope içinde `__init__` iki kere tanımlanamaz; bu "Redeclared defined above" hatasına yol açar.


#todo ## Case Study: Phone Architecture (Extend vs. Replace)

# `BasePhone` (Ata Sınıf) üzerinden `iPhone` ve `Samsung` (Alt Sınıflar) türetilmesi örneği.

# 1. **Extend (Genişletme):** `iPhone` sınıfı, `BasePhone`'dan gelen özelliklere ek olarak `AirDrop` özelliğine sahiptir. Bu nedenle `__init__` override edilir ve `super()` çağrılır.
# 2. **Replace (Geçersiz Kılma):** `phone_ring_sound` (Zil sesi) metodu. Her telefonun sesi farklıdır. Ata sınıftaki genel ses **tamamen** iptal edilir ve yeni ses tanımlanır.
# 3. **Enhance (İyileştirme):** `show_info` fonksiyonu, yeni eklenen özellikleri de gösterecek şekilde güncellenir.


#todo ## Case Study: Fatura Sistemi (Inheritance & Polymorphism)

# Gerçek hayat senaryosu: Farklı fatura tiplerini (Su, Elektrik, Doğalgaz) yöneten bir sistem tasarımı.

# ### Class Structure (Sınıf Yapısı)

# * **BaseBill (Ata Sınıf):**
# * **Attributes:** `bill_name`, `value_added_tax` (KDV), `amount`.
# * **Methods:**
# * `calculate_bill`: `tax * amount` işlemini yapar.
# * `create_log`: Fatura bilgilerini `.txt` dosyasına yazar.




# * **WaterBill (Child Class):**
# * **Extra Attribute:** `mill` (Sayaç dönme miktarı).



# ### Critical Logic: Override Kararları

# Bu senaryoda hangi fonksiyonun override edileceği, iş mantığına (Business Logic) göre belirlenir.

# 1. **`calculate_bill` Metodu:**
# * **Durum:** **Override Edilmeli.**
# * **Sebep:** Standart hesaplama (Vergi * Tutar) su faturası için yeterli değildir. İşin içine `mill` (sayaç) çarpanı girmektedir.
# * **Yöntem:** Ata sınıfın hesaplaması kullanılabilir (`super().calculate_bill() * self.mill`) veya formül tamamen yeniden yazılabilir.


# 2. **`create_log` Metodu:**
# * **Durum:** **Override Edilmemeli.**
# * **Sebep:** Loglama işlemi (dosyaya yazma) su, elektrik veya doğalgaz fark etmeksizin aynıdır.
# * **Polymorphism Triği:** `create_log` içinde `self.calculate_bill()` çağrılır. Burada `self`, o anki objeyi (örneğin `WaterBill` objesini) temsil ettiği için, `BaseBill`'deki değil, `WaterBill` içinde override edilmiş hesaplama metodu çalışır.



# ### Architecture & Maintainability (Sürdürülebilirlik)

# * **Eski Yöntem (Hard Coding):** Her yeni kurum (Örn: BEDAŞ, İSKİ) için kodu kopyala-yapıştır yapmak.
# * **Doğru Mimari (OOP):** `BaseBill` yapısı kurulduktan sonra sisteme yeni bir fatura tipi (Örn: Elektrik) eklemek, sadece yeni bir sınıf oluşturup parametreleri girmekten ibarettir.
# * **Sonuç:** Geliştirme süresi (Development Time) ve Bakım maliyeti (Maintenance Cost) minimize edilir.

# ---

# ## Encapsulation (Kapsülleme / Bilgi Gizleme)

# Sınıfın hassas verilerinin dış dünyadan (diğer sınıflardan veya dosyalardan) doğrudan erişime kapatılmasıdır.

# * **Syntax:** Değişken adının başına iki alt çizgi (`__`) getirilir. (Örn: `__status`, `__ip_addresses`).
# * **Access Rule (Erişim Kuralı):**
# * `object.__attribute` şeklinde dışarıdan erişilemez.
# * Sınıf içindeki metotlar (`self.__attribute`) erişebilir.



# ### Setters & Getters (Erişim Yöntemleri)

# Private (gizli) değişkenleri yönetmek için aracı fonksiyonlar kullanılır.

# 1. **Setter (Değer Atama):** Dışarıdan gelen veriyi kontrol ederek (Validation) private değişkene atar.
# * *Örnek:* `Product` sınıfında `price` ve `stock` bilgisi dışarıdan alınır. Setter fonksiyonu, bu değerlerin **0'dan büyük** olup olmadığını kontrol eder. Büyükse atama yapar, değilse işlemi reddeder.


# 2. **Getter (Değer Okuma):** Private değişkenin değerini güvenli bir şekilde dışarıya döner.

# ---

# ## Enum & Constants (Sabitler)

# * **Tanım:** Değişmesi beklenmeyen sabit değerlerin tutulduğu yapıdır. `Enum` sınıfından kalıtım alınarak oluşturulur.
# * **Best Practice:**
# * Sık değişen veriler (Örn: Kullanıcı Rolleri, Dinamik Statüler) için **KULLANILMAMALIDIR**.
# * Bir veriyi değiştirmek için kodun tekrar **Deploy** (Canlıya alınması) edilmesini gerektirir.


# * **Deployment Riski:** Canlıya alma işlemleri (Deployment) genellikle mesai dışı saatlerde (Cuma akşamı, hafta sonu) yapılır ve risklidir. Kod değişikliği gerektiren yapılar bu riski artırır.

# ---

# ## Future Roadmap: Data Science & AI

# Eğitimin bundan sonraki aşamalarında kod yazma yoğunluğu azalacak, analitik düşünme artacaktır.

# ### 1. Pandas (Veri Analizi)

# * SQL benzeri bir yapıdır ancak daha yeteneklidir.
# * **Fonksiyonlar:** Eksik veri saptama (Missing Data), İstatistiksel analiz, Veri Çarpıklığı (Skewness), Normalizasyon/Scaling.

# ### 2. Machine Learning (Scikit-Learn)

# * **Regresyon Modelleri:** Tahminleme.
# * **Evaluation Metrics (Değerlendirme):** R2 Score, Mean Squared Error (MSE).
# * **Algoritmalar:** KNN, Decision Tree, Logistic Regression.

# ### 3. Deep Learning (PyTorch)

# * Google'ın TensorFlow'u yerine, Hugging Face ve modern AI projelerinde yaygın olduğu için **PyTorch** kullanılacaktır.
# * **Konular:** Transformers, RAG (Retrieval-Augmented Generation), Fine-Tuning.

# ---

# ## Kariyer ve Başvuru Tavsiyeleri

# ### "Blacklist" Riski

# * Eğitim biter bitmez, hazır olmadan iş ilanlarına başvurmak stratejik bir hatadır.
# * İK (İnsan Kaynakları), yetersiz görülen bir adayı veritabanında işaretleyebilir (üstünü çizebilir). Gelişim gösterseniz bile aynı firmaya tekrar başvurmanız zorlaşır.

# ### Hazırlık Süreci (Checklist)

# Başvurudan önce tamamlanması gerekenler:

# 1. **GitHub Portföyü:** Kurstaki projelere benzer, özgün projeler eklenmeli.
# 2. **MLOps & Docker:** Modellerin deploy edilmesi süreçleri öğrenilmeli.
# 3. **Database:** En az birer tane SQL ve NoSQL projesi eklenmeli.

# > **Eğitmen Desteği:** Kod debug etme (hata ayıklama) talepleri karşılanmaz (ChatGPT bu konuda daha iyidir). Ancak proje vizyonu, mimari kararlar ve "nasıl daha iyi olur?" soruları için danışmanlık verilir.