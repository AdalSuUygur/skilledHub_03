
#! Listelerde Sıklıkla Kullanılan Built-In-Fonksiyonlar (Built-in Function)
#* Doğrudan adıyla, nesneyi argüman olarak vererek çağrılırlar ve listelere özel değildir, yani herhangi bir nesneye bağlı değillerdir.
#* Bu fonksiyonlar "genelde" iterable olan tüm nesnelerde kullanılabilir.

numeric_lst = [1,2,3,4,5,6,7,8,9,0]
alpha_lst = ["a","b","c","d","e","f","g","h"]

#? len() built-in-function
#* Var olan listenin uzunluğu (kaç elemanı olduğunu) verir.

print(len(numeric_lst))
print(len(alpha_lst))

#? sum() buil-in-function
#* Listedeki tüm SAYISAL elemanların toplamını verir.

print(sum(numeric_lst))
# print(sum(alpha_lst)) # Çalışmadı, neden? ÇÜNKÜ STR + INT yapmaya çalıştı ve hata gönderdi. Type error.

#? max() - min() buil-in-functions
#* Listedeki en büyük ve en küçük değeri bulur (str de kabul eder)

print(max(numeric_lst), min(numeric_lst))
print(max(alpha_lst), min(alpha_lst))

#? sorted() buil-in-function
#* Listedeki elemanları sıralayıp YENİ BİR LİSTE döndürür.

print(sorted(numeric_lst)) #çıktı olarak lsite verdi, küçükten büyüğe sıraladı.
print(sorted(alpha_lst))

#? any() buil-in-function
#* Listedeki elemanları gezer, istenilen en az bir tane varsa true döndürür, yoksa false döndürür.
#* Yani, any içinde herhangi bir şey tutuyosa true, tutmuyosa false dönüyor

bos_lst = [0, False, "", (), []] # Tüm elemanlar boş (0, False, boş string, boş liste)
print(any(bos_lst)) # Sonuç: False (Çünkü listede True kabul edilen tek bir değer bile yok.)
print(any(numeric_lst)) #Sonuç: True çünkü 0 haricindeki sayılar True döner.

#todo any() fonksiyonu list comprehension örnekleri ile daha iyi anlaşılabilir.
passwords = ["123", "98a", "12q", "987"]
print(
    any(ch.isalpha() for pwd in passwords for ch in pwd) #password listesindeki her pwd adlı itemın ch adlı karakterinin alfabetik olup olmadığına bakar
) #True döner çünkü bir tane bile elemanının içinde olması yeterli.

# List comprehension ile nested for yaptık, daha sonra beynim yanarsa diye buraya açık halini ekliyorum:
# for pwd in passwords:
#     for ch in pwd:
#         print(any(ch.isalpha()))

#region BURAYA BAK
# # todo is password valid uygulaması
# # min 16 karakter
# # min 1 büyük 1 küçük harf
# # min 1 noktalama işareti
# # min 1 rakam
# # hint: string kütüphanesi noktalama işaretleri hazır olarak var

password = input("Enter a password: ")

sinirlamalar = []
uzunluk = len(password)
buyuk_harf = any(ch.isupper for ch in password)

if len(password) < 3:
    print("min 16 karakter")
elif password.islower:
    print("min 1 karakter büyük harf")
elif password.isupper:
    print("min 1 küçük harf")


# # region kendi deneme başlangıcım da tam oturmadı kafama
# # password = input("şifre: ")
# # #sample PWD: beast?Beast1beast

# # is_karaktersiniri = len(password)
# # is_kucukharf = any(char.isupper for char in password)
# # is_buyukharf = any(char.isupper for char in password)
# # is_noktalamaisareti = any(char.ispuncti for char in password)
# # is_rakam = any(char.isupper for char in password)
# # endregion

# # region hocanın çözümü
# # from string import punctuation

# # password = input('Password giriniz: ')

# # if len(password) < 16:
# #     print("invalid password")
# # if not any(ch.isupper() for ch in password):
# #     print("invalid password")
# # if not any(ch.islower() for ch in password):
# #     print("invalid password")
# # if not any(ch.isdigit() for ch in password):
# #     print("invalid password")
# # if not any(ch in punctuation for ch in password):
# #     print("invalid password")


# # #*logic mantığı

# # if (
# #     len(pwd) < 16 and
# #     not any(ch.isupper() for ch in pwd)
# #     #and ile bağlayıp herhangi bir şey
# # ):
# #     print()

# # endregion

# # region hasan çözümü
# # import string
# # password = input("Şifreyi gir: ")
# # uzunluk = len(password) >= 16
# # b_harf  = any(ch.isupper() for ch in password)
# # k_harf  = any(ch.islower() for ch in password)
# # rakam  = any(ch.isdigit() for ch in password)
# # noktalama = any(ch in string.punctuation for ch in password)

# # if uzunluk and b_harf and k_harf and rakam and noktalama:
# #     print("Şifre geçerli.")
# # else:
# #     print("Şifre geçersiz.")
# #     if not uzunluk:
# #         print("16 karakterden az olamaz.")
# #     if not b_harf:
# #         print(" büyük harf içermeli.")
# #     if not k_harf:
# #         print(" küçük harf içermeli.")
# #     if not rakam:
# #         print("rakam içermeli.")
# #     if not noktalama:
# #         print(" özel karakter içermeli.")  
# # print(f"Girilen şifre: {password}")
# # endregion
#end region

#? filter() buil-in-function
#* Bir kurala tanımlanır ve kurala uyan elemanları ayıklar
#* Listeler üzerinde filtrelemeye yarayan fonksiyon
#* Listedeki tüm öğeleri gezer ve koşulu True döndüren öğeleri seçerek yeni bir sonuç dizisi oluşturur.
#* Filtreleme kuralı basit olduğunda, genellikle yerleşik ve isimsiz Lambda fonksiyonları kullanılır, bu da kodu daha kısa yapar:
#* Filter fonksiyonu obje içinde obje yarattığı için (Lambda aslında bir fonksiyon) aslında oldukça maliyetli O(N**2) kadar maliyetli oluyor.

print( #filter fonksiyonu ile üretilen liste, geçiçi bir liste olduğu için
    list( #eldeki veriyi listeye çevirdik (çevirmezsek çalışmaz)
        filter(lambda x: x < 5, numeric_lst) #kümelere benzer, x öyle ki, numberic_lst'te 5'ten küçük olan x'leri al.
        )
    )

#todo Verilen listedeki değerlerin karşılığı sayısal ise bunu yazdıran uygulama
#* Hint: isgidit() fonksiyonunu kullan
#* Lambda fonksiyonu bir performans sorunudur, bunu engellemek için kullanmadan yapalım:

some_values = ["123", "su", "zxc", "987", "345"]

only_digit = list(
    filter(str.isdigit, some_values) #! lambdadan kurtulduk burda 
                                     #! built in fonksiyonlarını tiplerine özel olarak çalıştırabiliriz. 
                                     #! yani lambdayı built in fonksiyonlar özelinde kullanmayabiliriz.
)
print(only_digit)
#* Python programlama dili, içerisindeki built in fonksiyonları kullandığımız zaman daha hızlı çalışır.

#? enumarete() built-in-function
#* Bir koleksiyonu döngüde gezerken hem elemana hem de sırasına (indeksine) ihtiyacınız olduğunda bunları veren fonksiyon

for index, item in enumerate(alpha_lst):
    print(
        f"Index value: {index}", end=" - "
        f"Item Value: {item}\n"
    )

#? isinstance() built-in-function
#* içerisine girilen nesnenin belirli bir veri tipine ait olup olmadığını kontrol etmeye yarayan built-in fonksiyondur.
#* Yani: "Bu nesne, bahsettiğim türden bir şey midir?" sorusunun cevabını True veya False olarak verir.

print(isinstance(alpha_lst, str)) #alpha_lst öğesi string midir? HAYIR çünkü bir listedir :)
print(isinstance(alpha_lst, list))

#todo Verilen listeden tam ve ondalıklı sayıları alma uygulaması
lst = [None, "b", 3.14, False, 9, "Oscar Piastri"]

numbers = list( #listeye convert etmek için.
    filter(
        lambda x: isinstance(x, (int, float)), lst) #x yani lst'teki eleman int veya float mı
)
print(numbers) #çıktı olarak da: [3.14, False, 9] verir, çünkü isinstance değeri bool döndürür, bundan dolayı direkt öyle bir ifadeyi çıktı olarak verir.

#? zip() built-in-function
#* Listeleri, tupleları, numply arraylerini YANİ koleksiyonları birbirleriyle eşleyerek birleştiren bir fonksiyon
#* Elemanları sırasıyla birleştirir, Tuple çiftlerinden oluşan YENİ bir zip nesnesi oluşturur.

esleştirilmiş_veri = zip(alpha_lst, numeric_lst) #bu bir veridir, bunu listeye çevirmek gerekir.
eslestirilmiş_lst = list(esleştirilmiş_veri)
print(eslestirilmiş_lst)

#* En başta, her iki listenin de uzunluğunu yazdırdık ve birbirlerinden farklılardı, peki bu zip ile patlamadıysa zip kaç elemanlı oldu?
print(
    len(
        eslestirilmiş_lst
    )
)
#küçük olanı aldı, yani, verinin karşılığı yoksa bunu paketlemedi.

#? map() built-in-function
#* Her elemana bir fonksiyon uygular. (Genellikle list() ile kullanılır.)