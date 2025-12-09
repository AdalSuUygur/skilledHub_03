
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