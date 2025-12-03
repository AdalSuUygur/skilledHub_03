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
    filter(str.isdigit, some_values) #lambdadan kurtulduk burda
)
print(only_digit)
#python içerisindeki built in fonksiyonları kullandığımız zaman daha hızlı çalışır.
#built in fonksiyonlarını tiplerine özel olarak çalıştırabiliriz. yani lambdayı built in fonksiyonlar özelinde kullanmayabiliriz.

#any-map olacak yarınki derste
