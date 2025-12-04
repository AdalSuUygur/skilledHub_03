
#region (01-12-25, ders 14)
#? List Comprehensions 
#* Bir listeyi oluşturmak için gereken adımları (boş liste tanımlama, döngü kurma, .append() ile ekleme) tek bir sözdizimi içine yerleştirmektir.
#* Yani listeyi kısaca oluşturmak için List Comprehensions kullanılır.

#Geleneksel yöntem ile liste oluşturma:
lst_geleneksel = []
for i in range(10):
    lst_geleneksel.append(i)
print(lst_geleneksel)

#YA DA list comprehension ile kısa yoldan liste oluşturma:
lst_comprehension = [i for i in range(10)]
print(lst_comprehension)

#HATTA tek satırda bile yazılabilir:
print(lst_comprehension_shorter = [i for i in range(10)])

#Comprehension kompleksleştikçe yazması da okuması da zorlaşıyor, peki neden tercih ediliyor? 
#Time fonksiyonu ile örnekte göreceğiz ^^

#todo rastgele üretilmiş 10 sayı ile list comprehension uygulaması
from random import randint
lst_random = [randint(a=10, b=100) for _ in range(10)] #randint fonksiyonunu kullanabildik.
print(lst_random)

#todo rakamların karesinin list compehension ile oluşturulması
lst_squares = [i**2 for i in range(10)] #işlem yapabildik.
print(lst_squares)

#todo 0-100 arasındaki çift sayıları listeye eklenmesi
lst_even_numbers = [i for i in range(101) if i%2 == 0] #if ile birlikte kullanabildik.
print(lst_even_numbers)

#todo ternary if ile, meyve içerisinde "an" geçiyorsa true, geçmiyorsa false eklenen list
fruits = [
    "Apple", "Banana", "Orange", "Mango", "Pineapple",
    "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
    "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
    "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
]

lst_includes_an = [True if "an" in fruit.lower() else False for fruit in fruits] #ternary if yapısı ile kullanabildik
print(lst_includes_an)

#? çarpım tablosu, satır-sütun algoritması
#* SATIR SÜTUN ALGORİTMALARINDA: i satırı, j sütunu yönetir, yani i 1. adımındayken j orada belirtilen adım kadar çalışır.

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
    print("-------------------")

#List comprehenstion ile yapılması:

lst_carpim_tablosu = [ i*j 
    for i in range(1,11) for j in range(1, 11)
]
print(lst_carpim_tablosu)

print(
    [
        [f"{i} x {j} = {i*j}"] for i in range(1,11) for j in range(1,11)
    ]
) #bu da hem tek satırda hem de süslüce hali

#? Filter() Function
#* Listeler üzerinde filtrelemeye yarayan fonksiyon
#* Listedeki tüm öğeleri gezer ve koşulu True döndüren öğeleri seçerek yeni bir sonuç dizisi oluşturur.
#* Filtreleme kuralı basit olduğunda, genellikle yerleşik ve isimsiz Lambda fonksiyonları kullanılır, bu da kodu daha kısa yapar:

#todo Fruits listesindeki içinde "an" geçen meyveleri filtreleme uygulaması
print(
    list(
        filter(
            lambda fruit: "an" in fruit, fruits
        )
    )
)

#todo -100 ile 100 aralığındaki 1000 random sayı ile oluşturulan bir listeden pozitif sayıları çekme uygulaması
from random import randint
numbers = [randint(a=-100, b=100) for i in range(1000)] #numbers diye 1000 itemlı liste oluşturuldu

#PATH I --- list comprehension
lst_positive_numbers = [number for number in numbers if number > 0]
print(lst_positive_numbers)

#PATH II --- filter() function
temp_lst = filter(lambda x: x>0, numbers) #geçici bir liste oluşturuldu, lambda fonksiyonunu küme tanımlamalarına benzetebilirsin
#geçici listede, numbers listesi içerisindeki x için, x>0 durumlarını temp_lst değişkenine ekle gibi bir çıkarım var.

lst_positive_numbers_lambda = list(temp_lst) #gelen değişkeni listeye çevirdik.
print(lst_positive_numbers_lambda)

#todo filter fonksiyonu ile çift sayıların filtrelenip ve liste olarak ekrana yazdırılması
temp_lst = filter(lambda x: x % 2 == 0, numbers)
even_numbers = list(temp_lst)
print(even_numbers)

#region 15. ders 03/12/2025
#? isinstance() fonksiyonu
#* içerisine girilen nesnenin belirli bir veri tipine ait olup olmadığını kontrol etmeye yarayan built-in fonksiyondur.
#* Yani: "Bu nesne, bahsettiğim türden bir şey midir?" sorusunun cevabını True veya False olarak verir.

lst = [None, "b", 3.14, False, 9, "Oscar Piastri"]
# Burdan sadece tam ve ondalıklı sayıları almamız gerek.

numbers = list( #listeye convert etmek için.
    filter(lambda x: isinstance(x, (int, float)), lst) #x yani lstedeki eleman int veya float mı
)
print(numbers) #çıktı olarak da: [3.14, False, 9] verir, çünkü isinstance değeri bool döndürür, bundan dolayı direkt öyle bir ifadeyi çıktı olarak verir.

#todo sonu .com ile biten mail adreslerini filter fonksiyonu ile yazdıran ifade
#* Hint: endswith() fonksiyonunu kullan

mails = [
    "burak.yilmaz@outloo.com", 
    "savage@mail.com", 
    "beast@", 
    "keko@com.xyz", 
    "adal@gmail.com"
]

correct_mails = (list(
    filter(
        lambda x: x.endswith(".com"), mails)
    )
)
print(correct_mails)

#todo Verilen listedeki değerlerin karşılığı sayısal ise bunu yazdıran uygulama
#* Hint: isgidit() fonksiyonunu kullan

some_values = ["123", "burak", "zxc", "987", "345"]
number_values = list(
    filter(
        lambda x: x.isdigit(), some_values
    )
)
print(number_values)

#Hocanın çözümü: Lambda fonksiyonu bir performans sorunudur, bunu engellemek için kullanmadan yapalım:
only_digit = list(
    filter(str.isdigit, some_values) #! lambdadan kurtulduk burda 
                                     #! built in fonksiyonlarını tiplerine özel olarak çalıştırabiliriz. 
                                     #! yani lambdayı built in fonksiyonlar özelinde kullanmayabiliriz.
)
print(only_digit)
#* python, içerisindeki built in fonksiyonları kullandığımız zaman daha hızlı çalışır.

#todo Benchmark testing between without tryExcept / tryExcept / raiseException

import time
import tracemalloc

bolunen = 2
bolen = 0
test1 = "IF_ELSE"
test2 = "TRY_EXCEPT"
test3 = "RAISE_EXCEPTION"

#region Kendi çözümüm

def path_1(bolunen, bolen):
    if bolen == 0:
        return "Sıfıra bölünme hatası (IF/ELSE ile yakalandı)"
    else:
        bolum = bolunen / bolen
        return bolum

def path_2(bolunen, bolen):
    try:
        bolum = bolunen / bolen
    except (ZeroDivisionError) as err:
        bolum = f"Sıfıra bölünme hatası (TRY/EXCEPT ile yakalandı): {err}"
    return bolum

def path_3(bolunen, bolen):
# Bu metotta bilerek ZeroDivisionError yerine başka bir hata fırlatıyoruz.
    if bolen == 0:
        # Kendi hata tipimizi fırlatıyoruz.
        raise ValueError("Özel Hata: Bölen sıfır olamaz!")        
    return bolunen / bolen

def benchmart_test(bolunen_deger, bolen_deger, test_adi):
        # 1. TEST FONKSİYONUNU SEÇME
    if test_adi == "IF_ELSE":
        test_func = path_1
    elif test_adi == "TRY_EXCEPT":
        test_func = path_2
    elif test_adi == "RAISE_EXCEPTION":
        test_func = path_3
    else:
        raise ValueError("Tanımsız test adı!")

    tracemalloc.start()
    t1 = time.perf_counter()

    # path_3 (RAISE_EXCEPTION) bir hata fırlatacağı için, onu da yakalamamız lazım.
    try:
        # Seçilen fonksiyonu çağırıyoruz
        result = test_func(bolunen_deger, bolen_deger)
    except ValueError as e:
        # path_3'ten gelen özel hatayı yakala
        result = str(e)

    t2 = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    runtime_ms = (t2 - t1) * 1000 
    peak_memory = peak / 1024
    
    return runtime_ms, peak_memory, result

runtime_memory1, peak_memory1, islem_sonucu1 = benchmart_test(bolunen, bolen, test1)
runtime_memory2, peak_memory2, islem_sonucu2 = benchmart_test(bolunen, bolen, test2)
runtime_memory3, peak_memory3, islem_sonucu3 = benchmart_test(bolunen, bolen, test3)

print(
    f'Method --> {test1}\n'
    f'Runtime: {runtime_memory1:.6f} ms\n'
    f'Peak Memory: {peak_memory1:.6f} KB\n'
    f'Result: {islem_sonucu1}\n'
    '===============================\n'
    f'Method --> {test2}\n'
    f'Runtime: {runtime_memory2:.6f} ms\n'
    f'Peak Memory: {peak_memory2:.6f} KB\n'
    f'Result: {islem_sonucu2}\n'
    '===============================\n'
    f'Method --> {test3}\n'
    f'Runtime: {runtime_memory3:.6f} ms\n'
    f'Peak Memory: {peak_memory3:.6f} KB\n'
    f'Result: {islem_sonucu3}'
)

#endregion

