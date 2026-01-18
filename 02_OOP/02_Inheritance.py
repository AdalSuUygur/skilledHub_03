
#! Inheritance (Kalıtım)

# * **Definition:** Biyolojideki kalıtım mantığının yazılıma uyarlanmış halidir. Bir **Parent Class** (Ata sınıf) özelliklerinin (attributes) ve yeteneklerinin (methods), **Child Class** (Alt sınıf) tarafından devralınması işlemidir.
# * **Parent Class (Base Class):** Özellikleri aktaran, genel çatıyı oluşturan sınıf.
# * **Child Class (Sub Class):** Özellikleri devralan, gerektiğinde bunları genişleten sınıf.

# ### Temel Syntax ve Mantık

# Python'da kalıtım, sınıf tanımlanırken parantez içinde ata sınıfın belirtilmesiyle sağlanır: `class Child(Parent):`.

# * **Human Case (Temel Örnek):**
# * **Parent:** `Human` (Attributes: `full_name`, `weight`; Method: `show_info`).
# * **Children:** `FootSoldier`, `Knight`.
# * **Behavior:** `FootSoldier` ve `Knight` sınıflarının içi boş (`pass`) olsa bile, `Human` sınıfındaki tüm özellikleri ve `show_info` metodunu kullanabilirler.



# > **Not:** Bir sınıfın içi boş olsa dahi, miras aldığı ata sınıfın tüm yeteneklerine (instance attributes, methods) otomatik olarak sahip olur.

# ---

# ## The `object` Class

# * **Concept:** "Python is all about object." Python'da her şey objedir ve tüm sınıfların en tepedeki atası **`object`** sınıfıdır.
# * **Implicit Inheritance:** Python 3.x'te bir sınıf oluşturulduğunda (örn: `class Human:`), biz belirtmesek bile arka planda `class Human(object):` şeklinde çalışır.
# * **Magic Methods:** `__doc__`, `__dir__`, `__format__` gibi çift alt çizgili (underscore) metotlar, bu `object` sınıfından gelir.

# ---

# ## Multiple Inheritance (Çoklu Kalıtım)

# Bir **Child Class**'ın birden fazla **Parent Class**'tan aynı anda miras alabilmesidir.

# ### Case Study: Birds (Kuşlar)

# Metinde verilen örnek senaryo şu şekildedir:

# 1. **Parent Classes:**
# * `YuzebilenKus`: `yuzebilmek()` metoduna sahip.
# * `YuruyenKus`: `yurumek()` metoduna sahip.
# * `UcabilenKus`: `ucabilmek()` metoduna sahip.


# 2. **Child Classes:**
# * **Penguen:** `class Penguen(YuzebilenKus, YuruyenKus)` -> Hem yüzme hem yürüme yeteneğini alır.
# * **Kartal:** `class Kartal(UcabilenKus, YuruyenKus)` -> Hem uçma hem yürüme yeteneğini alır.
# * **Tavuk:** `class Tavuk(YuruyenKus)` -> Sadece yürüme yeteneğini alır (Single Inheritance).



# ---

# ## Method Overriding

# **Definition:** Ata sınıftan (Parent) miras alınan bir metodun, alt sınıfta (Child) ihtiyaca göre yeniden tanımlanarak davranışının değiştirilmesi veya geliştirilmesidir.

# ### 1. Enhance (Geliştirme/Genişletme)

# Mevcut ata fonksiyonunun yeteneğini koruyup üzerine ekleme yapma işlemidir.

# * **Key Tool:** `super()` fonksiyonu.
# * **Usage:** `super().__init__(...)` ile önce atadaki kod çalıştırılır, ardından alt sınıfa özgü kodlar eklenir.

# #### Case Study: E-Commerce (Product vs. Category)

# * **BaseEntity (Parent):** Tüm varlıkların ortak özellikleri olan `name` ve `description` tutulur.
# * **Category (Child):** Ekstra bir özelliğe ihtiyaç duymaz. Parent'taki `__init__` ve `show_info` yeterlidir. **Override edilmez.**
# * **Product (Child):**
# * `price` ve `stock` gibi kendine has özelliklere sahiptir.
# * Parent'taki `__init__` yetersiz kalır.
# * **Action:** `__init__` override edilir. `super()` ile isim ve açıklama alınır; fiyat ve stok manuel eklenir. `show_info` metodu da bu yeni bilgileri gösterecek şekilde güncellenir.



# ### 2. Replace (Geçersiz Kılma/Ezme)

# Ata sınıftan gelen metodun tamamen yok sayılıp, yerine yepyeni bir logic yazılmasıdır.

# #### Case Study: Phones (BasePhone)

# * **BasePhone (Parent):** `phone_ring_sound()` metodu "Genel telefon sesi" döndürür.
# * **IPhone (Child):**
# * `__init__` override edilir (`super` ile) -> `Airdrop` özelliği eklenir.
# * `phone_ring_sound()` override edilir -> "iPhone telefon sesi" döndürür (Replace).


# * **Samsung (Child):**
# * `__init__` override edilir (`super` ile) -> `Operating System` özelliği eklenir.
# * `phone_ring_sound()` override edilir -> "Samsung telefon sesi" döndürür (Replace).



# > **Polymorphism Bağlantısı:** `phone_ring_sound` metodu; Base, iPhone ve Samsung sınıflarında aynı isme sahip olmasına rağmen üç farklı çıktı üretir. Bu durum **Polymorphism** (Çok Biçimlilik) kavramının temelidir.

# ---

# ## Uygulama: Fatura Hesaplama (Bill System)

# Verilen ödev/pratik senaryosunun analizi:

# ### Class Structure

# 1. **BaseBill (Parent):**
# * **Attributes:** `bill_name`, `value_added_tax` (KDV).
# * **Methods:**
# * `calculate_bill(amount)`: Vergili tutarı hesaplar.
# * `create_log()`: Fatura detaylarını `.txt` dosyasına yazar.




# 2. **Child Classes:** `WaterBill`, `NaturalGas`, `Electricity`.

# ### Logic Analysis

# * **Override Edilmeyenler:** `create_log`. Çünkü su, gaz veya elektrik faturası fark etmeksizin loglama işlemi (isim ve tutar yazma) standarttır.
# * **Override Edilenler:** `__init__` ve `calculate_bill`.
# * Her faturanın birimi farklıdır (`mill`, `m3`, `kw`).
# * Bu birimler `__init__` içinde tanımlanmalı ve hesaplama (`calculate_bill`) bu birimlere göre özelleştirilmelidir.



# ---

# ## Kariyer ve ML Ops Tavsiyeleri

# Eğitmenin sektör deneyimlerine dayalı kritik tavsiyeler:

# ### Essential Skill Set (Olmazsa Olmazlar)

# Sadece kod yazmak veya algoritma bilmek yeterli değildir. İK filtrelerini geçmek ve mülakatlarda ayrışmak için şu teknolojiler "cephaneliğe" eklenmelidir:

# * **ML Ops:** Modeli canlıya aldıktan sonra izleme (monitoring), uyarı sistemleri (alerting) ve takip (tracking). Mülakatlarda en ayırt edici noktadır.
# * **Containerization:** **Docker**.
# * **Database:**
# * SQL: **PostgreSQL**.
# * NoSQL: **MongoDB**.


# * **Cloud Providers:** AWS, Google Cloud, Azure (İlanların çoğunda bulunur).

# ### Öğrenme Stratejisi

# * **GitBook:** Okunanları kendi cümlelerinizle not alın. ("Kendi yazdığınız bilgi, en hızlı hatırladığınız bilgidir.")
# * **GitHub:** Sadece kod depolamak için değil, teknik yetkinliği kanıtlamak için repolar oluşturun (OOP, AI, ML projeleri).
# * **Keywords:** LinkedIn profilinde ve CV'de RAG, LLM, Fine Tuning, PyTorch, Transformer gibi teknik terimlerin geçmesi, İK algoritmalarına takılmamak için kritiktir.