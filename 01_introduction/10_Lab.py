
#! Listelerde Sıklıkla Kullanılan Built-In-Fonksiyonlar (Built-in Function) 4

numeric_lst = [1,2,3,4,5,6,7,8,9,0]
alpha_lst = ["a","b","c","d","e","f","g","h"]

#? zip() built-in-function
#* Listeleri, tupleları, numply arraylerini YANİ koleksiyonları birbirleriyle eşleyerek birleştiren bir fonksiyon
#* Elemanları sırasıyla birleştirir, Tuple çiftlerinden oluşan YENİ bir zip nesnesi (kendine özgü bir tip) oluşturur.
#* Zip fonksiyonu ile transpoz işlemi sıklıkla yapılır (satır sütun bilgilerini sütur satın olarak güncelleme, yani yerlerini değiştirme)

esleştirilmiş_veri = zip(alpha_lst, numeric_lst) #bu bir veridir, bunu listeye çevirmek gerekir.
eslestirilmiş_lst = list(esleştirilmiş_veri)
print(eslestirilmiş_lst)

#* En başta, her iki listenin de uzunluğunu yazdırdık ve birbirlerinden farklılardı, peki bu zip ile patlamadıysa zip kaç elemanlı oldu?
print(
    len(
        eslestirilmiş_lst 
    )
) #uzunluğu küçük olanı aldı, yani, verinin karşılığı yoksa bunu paketlemedi.

#? Unzipping (* operatörü ile)
#* Genellikle zip() yerleşik fonksiyonu ile oluşturulmuş bir veri yapısını geri açma(unboxing) bağlamında kullanılır.
unzipped_numeric, unzipped_alpha = zip(*eslestirilmiş_lst)
print(unzipped_numeric) #burda ziplenmiş veriyi geri aldık ancak orijinal listedeki 9,0'ı almadı çünkü eşleştirilmiş listede kesip atılmıştı bunlar
print(unzipped_alpha)

#region Examples
#todo Örnek zip() fonksiyonu uygulaması, 2 listede 10ar adet random sayılar üretilecek ve indexlerdeki değerler toplanarak sonuçları liste olarak veren uygulama
from random import randint
# number1 = [randint(a= 0, b=100) for _ in range(10)]
# number2 = [randint(a= 0, b=100) for _ in range(10)]

# numbers = list(zip(number1, number2))
# addition = [n1+n2 for n1, n2 in numbers]
# print(numbers)
# print(addition)

#todo Index ve itemı ziplenen uygulama (zip ile enumerateyi taklit etme)
# lst = ['ayhan', 'elton', 'adal', 'merve']

# print(
#     list(
#         zip(
#             range(len(lst)), lst #indexi nasıl alabiliriz, range nerde durmalı, listenin uzunluğu kadar durmalı, buyrun yaptık
#             ) #ve böylece enumerate() built in fonksiyonunu zip ile taklit ettik.
#         )
#     )

#todo Ödev: Transpoz ödevi, 3 line 10ar tane rastgele sayı ile doldurulacak ve index değerleri olarak çıktı alınacak
# matrix = [
#     [34, 56, 123, 56], # --> bu iç listeler list comprehnsion ile rastgele sayılar ile doldurulacak
#     [23, 67, 12, 45],
#     [11, 54, 89, 22], # --> 3 line yeterli
# ]
# Output:
# [(34, 23, 11), (56, 67, 54), (123, 12, 89), ....]

# matrix = [
#     [randint(0,100) for _ in range(10)] #0-100 arasında 10 tane sayı ürettim
#     for _ in range(3) #bundan 3 tane üretmem gerekiyordu bunu da list comprehension ile ürettik
# ]
#print(matrix) #test

#path i
# matrix_transpose = list(    zip(  matrix[0], matrix[1], matrix[2]  )   )
# print(matrix_transpose)

#path ii
# print(list(zip(*matrix)))


# print(matrix[i][j]) 
# i = range(len(matrix))
# j = range(10)
#endregion
