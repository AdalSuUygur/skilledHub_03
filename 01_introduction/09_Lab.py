
#! Listelerde Sıklıkla Kullanılan Built-In-Fonksiyonlar (Built-in Function) 3

numeric_lst = [1,2,3,4,5,6,7,8,9,0]
alpha_lst = ["a","b","c","d","e","f","g","h"]

#? any() buil-in-function
#* Listedeki elemanları gezer, istenilen en az bir tane varsa true döndürür, yoksa false döndürür.
#* Yani, any içinde herhangi bir şey tutuyosa true, tutmuyosa false dönüyor

bos_lst = [0, False, "", (), []] # Tüm elemanlar boş (0, False, boş string, boş liste)
print(any(bos_lst)) # Sonuç: False (Çünkü listede True kabul edilen tek bir değer bile yok.)
print(any(numeric_lst)) #Sonuç: True çünkü 0 haricindeki sayılar True döner.

#todo any() fonksiyonu uygulaması
# programming_languages = [   "python",  "java", "go"    ]
# print(  any(    pl == "python" for pl in programming_languages  )   ) #1 tane şart tutarsa true döner, yani true çıkar.
# print(  any(    pl == "c#" for pl in programming_languages  )   ) #hiçbir şartı tutmuyor. False döner.

#todo any fonksiyonu ile verilen listede 10'dan büyük sayı var mı kontrol eden uygulama
# numbers = [3,4,5,6,7,8,9]
# result = any(number > 10 for number in numbers)
# print(result)

#todo any() fonksiyonu list comprehension örnekleri ile daha iyi anlaşılabilir.
passwords = ["123", "98a", "12q", "987"]
print(
    any(
        ch.isalpha() for pwd in passwords for ch in pwd #password listesindeki her pwd adlı itemın ch adlı karakterinin alfabetik olup olmadığına bakar
        ) #True döner çünkü bir tane bile elemanının içinde olması yeterli.
) #çıktı olarak da True alırız.

# List comprehension ile nested for yaptık, daha sonra beynim yanarsa diye buraya açık halini ekliyorum:
# for pwd in passwords:
#     for ch in pwd:
#         print(any(ch.isalpha()))

#todo is_valid Password uygulaması
# Şartlar: min 16 karakter, min 1 büyük; 1 küçük harf, min 1 noktalama işareti, min 1 rakam
# Hint: String kütüphanesi içerisinde noktalama işaretleri hazır olarak var
import string
password = input("Enter a password: ")

#region kendi çözümüm
# def is_valid(password):
#     karakter = len(password) #min 16 karakter olmalı
#     buyuk_harf = any(char.isupper() for char in password)
#     kucuk_harf = any(char.islower() for char in password)
#     noktalama_isareti = any(char in string.punctuation for char in password) #bunu yine kullanmada sıkıntı çektim.
#     rakam = any(char.isnumeric() for char in password)
#     if karakter <= 16:
#         return False, "minimum karakter sınırı"
#     elif not buyuk_harf:
#         return False, "büyük harf eksik"
#     elif not kucuk_harf:
#         return False, "küçük harf eksik"
#     elif not noktalama_isareti:
#         return False, "noktalama işareti eksik"
#     elif not rakam:
#         return False, "rakam eksik"
#     return True, "valid password"

# gecerli_mi, ciktisi = is_valid(password)

# if gecerli_mi:
#     print("hoşgeldiniz " + ciktisi)
# else:
#     print(ciktisi)
#endregion

# region hocanın çözümü
# if len(password) < 16:
#     print("invalid password")
# if not any(ch.isupper() for ch in password):
#     print("invalid password")
# if not any(ch.islower() for ch in password):
#     print("invalid password")
# if not any(ch.isdigit() for ch in password):
#     print("invalid password")
# if not any(ch in punctuation for ch in password):
#     print("invalid password")

#*logic mantığı
# if (
#     len(pwd) < 16 and
#     not any(ch.isupper() for ch in pwd)
#     #and ile bağlayıp herhangi bir şey
# ):
#     print()

# endregion