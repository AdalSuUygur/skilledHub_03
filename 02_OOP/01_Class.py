
#! Object Oriented Programming (OOP)

# **Object Oriented Programming (OOP)** yani **Nesne Tabanlı Programlama** nedir?
# Nesne tabanlı programlama, bize kendi nesnelerimizi yaratma imkanı tanır.

#* Peki, nesne nedir?
# Şimdiye kadar yazdığımız kodlarda Python'da hali hazırda bulunan (built-in) nesnelerden yararlandık: int, str, dict, list.. vb.
# Bunların her birisi nesnedir, şimdi ise artık kendi nesnemizi yaratacağız.
# Nesne, özellikleri olan herhangi bir şey olabilir: bilgisayar, araba, öğretmen, öğrenci vb..

#* Neden OOP önemli?
# Projeler büyüdükçe yönetilemez boyutlara gelebiliyor, bakım ve onarım süreleri uzuyor. 
# OOP, bu artan ihtiyaçlar ve karmaşıklık doğrultusunda ortaya çıkmış bir yaklaşımdır. 
# Bize sağladığı en temel yenilik, kendi özel nesnelerimizi ve yapılarımızı yaratabilmemizdir.

#? Kendi nesnemizi yaratmak
# Kendi nesnemizi yaratmak için sınıflara (class) ihtiyacımız var. Neden? Çünkü
# Bu sınıflar yaratacağımız obje ve objelerin (birden fazla dict yazabiliyoruz ya, öyle düşün) özelliklerini içerlerinde barındırır.

#? Class SYNTAX
# Sınıf (Class) Tanımlama
class Araba: # Araba nesnesinin özelliklerini için 
    door_number = 0
    engine_size = 5.6
    torque = 500
    lenght = 3.1
    width = 1.2
    color = "papaya"
    brand = "Dodge"
    model = "TRX 1500"

#* Sınıfı tanımladıktan sonra o sınıftan nesne üretmeye **instance** (örneklem) çıkartmak denir.

# Sınıftan örneklem çıkartmak için:
a1 = Araba() # a1'in tipi Araba oldu.
# Nokta notasyonu ile a1 üzerinden fonksiyonlarına erişebiliyoruz artık.

#* Örneğin `A1 = Araba()` dediğimizde, `Araba` sınıfından `A1` adında bir nesne üretmiş oluruz. 
# Tıpkı liste veya sözlüklerin kendi sınıflarına ait olması gibi, bizim yarattığımız nesneler de kendi tanımladığımız sınıflara ait olur. İstediğimiz yerde, istediğimiz kadar nesne üretebiliriz.
a1.color = "pink"
print(f"Color: {a1.color}")

# Kendi nesnelerimizi yaratabilmek için öncelikle *sınıflara (Class)* ihtiyacımız vardır. 
# Nesne yaratmadan önce bir sınıf tanımlaması yaparız. 
# Bu sınıflar, yaratacağımız objenin özelliklerini barındıran prototipler gibidir. 
# Üretimde nasıl önce bir prototip üretilip sonra seri üretime geçiliyorsa, 
# burada da önce sınıf yaratılır, sonra bu sınıf üzerinden nesneler üretilir.

#* Kendi sınıf tanımlamam:
class Character:
    age = 29
    skin_tone = "Yellow"
    hair = 0
    accesories = "earrings"

cagirma_nesnem = Character() #sınıftan örneklem çıkartıyoruz
cagirma_nesnem.age = 86 #nokta notasyonu ile obje üzerinden sınıfın özelliklerine erişiyoruz
print(cagirma_nesnem.age)

# built in objelerle custom objeler arasında hiçbir fark yok!

#? Constructor (Yapıcı Fonksiyon): `__init__`

#* Nesne türetilirken arka planda otomatik olarak çalışan özel bir fonksiyon vardır. 
#* Diğer programlama dillerinde buna **Constructor** (yapıcı fonksiyon) denir, 
#* Python'da ise karşılığı `__init__` fonksiyonudur.

# 1. **Sınıfı Başlatmak (Initialize):** Nesneyi RAM'e çıkartır ve hazırlar.
# 2. **Zorunlu Özellikler Belirlemek:** Nesne yaratılırken girilmesi zorunlu olan bilgileri (parametreleri) tanımlar.
# 3. **Atama Yapmak:** Dışarıdan gelen değerleri alıp, objenin kendi özelliklerine (attribute) atar.

# SYNTAX YAPISI
# Eğer `__init__` fonksiyonunu özelleştirip parametreler eklersek (örneğin bir öğrenci için `Ad` ve `ID`), 
# nesne üretirken bu bilgileri girmek zorunlu hale gelir. Aksi takdirde hata alırız.
class Student:
    # bu class attribute
    taken_courses = ["History", "Algorithm"]
    
    def __init__(self, full_name: str, student_id: str):
        self.tam_ad = full_name
        self.ogrenci_id = student_id

# s1 = Student() # Aha burda patladıkkkk neden? çünkü zorunlu parametreleri girmedik.
s2 = Student(full_name="ali veli", student_id="1234")
print(s2.__dict__)

#* Self Anahtar Kelimesi
# `__init__` veya sınıf içindeki diğer fonksiyonlarda kullandığımız `self` kelimesi, **objeyi temsil eder**. 
# O an işlem yapılan nesne ne ise `self` odur. 
# Başka isimler verilebilir ancak "best practice" (en iyi uygulama) olarak `self` kullanılması önerilir.

#? Sınıf Özellikleri ve Nesne Özellikleri (Class vs Object Attributes)

# İki tür özellik tanımlaması mevcuttur:
# 1. **Class Attribute (Sınıf Özelliği):** Sınıfın içine doğrudan yazılan özelliklerdir. Obje yaratılmadan önce de sınıfın içinde var olurlar. Obje yaratıldığında bu özellikler objeye de geçer.
# 2. **Object Attribute (Nesne Özelliği):** `__init__` fonksiyonu içerisinde tanımlanan ve genellikle nesne yaratılma anında (run-time) oluşan özelliklerdir.

# Bir nesne üzerinden çağırdığımızda hem sınıfın genel özelliklerini hem de nesneye özel yaratılmış özellikleri görebiliriz.

print(
    f'Student Name: {s2.tam_ad}\n'
    f'Student Id: {s2.ogrenci_id}\n'
    f'Taken Courses: {s2.taken_courses}'
)

print(dir(Student))
#* ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'taken_courses']
print(dir(s1))
#* ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ogrenci_id', 'taken_courses', 'tam_ad']

boxers = list()
print(dir(boxers))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
