
#todo 17. Ders ödevi #2
#* -100 ile + 100 arasında 10 tane rastegele sayı üretelim
#* sadece pozitif sayıları string dönüştürerek bir liste içerisinde çıktı verin

# from random import randint
# numbers = [randint(-100,100) for _ in range(10)]
# print(numbers) #test


# print( #4. adım : terminale çıktısını verdik
#     list( #3. adım : yazdırabilmek veya tutabilmek adına listeye çevirdik
#         map(str, #2. adım : map ile, gelen int değerleri str'ye çevirdik
#                 filter(lambda x: x>0, numbers) #1. adım : 0'dan büyük olan sayıları çektim
#             )
#         )
#     )

#todo 17. Ders ödevi #1
#* list comprehension ile 2 tane rastgele sayılar içeren liste oluşturun
#* üretilecek sayı aralıkları -100, +100
#* her iki listedeki sayıları toplayalım
#* toplamları negatif olanları pozitif dönüştürerek bir liste içerisinde yazdıralım

from random import randint
numbers_1 = [randint(-100,100) for _ in range(10)]
numbers_2 = [randint(-100,100) for _ in range(10)]
# print(numbers_1) #test
# print(numbers_2) #test

# print( #5. adım : terminale çıktısını verdik
#     list( #4. adım : bulunan değerleri listeye çevirdik.
#         map(abs, #3. adım : burda da hesaplanan değerlerin mutlak değerini aldık
#             map(lambda x: x[0] + x[1], #2. adım : map fonksiyonu ile tupledaki değerleri topladık
#                 zip(numbers_1, numbers_2)) #1. adım : iterable nesnemizi yarattık ve 2 farklı listenin indexlerini birleştirdik
#         )
#     )
# )

#derste örneğin çözümü ve hocanın esktraları:
# result = [abs(x+y) for x,y in zip(numbers_1,numbers_2)]
# lst_result = list(map(str, result))
# print(list(map(str, result)))
#çıktının "-" ifadelerle bağlanmasını istiyoruz.
# print("-".join(lst_result)) #stringe dönüştürmemizin sebebi join fonksiyonunu kullanmak.



#todo Girilen sampledaki sesli harfleri, sessiz harfleri, typoları ayrı listelere ekleyen uygulama. İlgili listelerde eleman tekrarı olmamalı. Space ignore.
sample = "buRa1k _Ayi?Lm2aZu"
# sesli_harfler = list(
#     {ch for ch in sample if ch in "aeıioöuü"}) #set comprehension :D set de küme, tekrarlı eleman olmaz.
# sessiz_harfler = set(
#     [ch for ch in sample if ch in "bcçdfgğhjklmnprsşvyz"])
# typo_char = list(
#     {ch for ch in sample if not ch.isalpha()}
# )
# print(sesli_harfler, sessiz_harfler, typo_char)

#todo rastgele üretilmiş 10 sayı ile list comprehension uygulaması
from random import randint
# lst_random = [randint(a=10, b=100) for _ in range(10)] #i yerine underscore yani _ kullandık sayaç yerine zaten çok da önemli değil.
# print(lst_random)

# #geleneksel yöntemle:
# lst_random_geleneksel = []
# for i in range(10):
#     lst_random_geleneksel.append(randint(0,100))
# print(lst_random_geleneksel)

#todo rakamların karesinin list compehension ile oluşturulması
# lst_squares = [i**2 for i in range(10)] #işlem yapabildik.
# print(lst_squares)

#todo 0-100 arasındaki çift sayıları listeye eklenmesi
#deneme = [i % 2 = 0, for i in range(101)] #* Bak bu olmadı, gördün mü? Çünkü if'e ihtiyaç var.
                                           #* List Comprehension uygulamarında içine if de ekleyebiliriz.
# lst_even_numbers = [i for i in range(101) if i%2 == 0] #if ile birlikte kullanabildik.
# print(lst_even_numbers)

#todo -100 ile 100 aralığındaki 1000 random sayı ile oluşturulan bir listeden pozitif sayıları çekme uygulaması
numbers = [randint(a=-100, b=100) for i in range(1000)] #numbers diye 1000 itemlı liste oluşturuldu

#PATH I --- list comprehension
# lst_positive_numbers = [number for number in numbers if number > 0]
# print(lst_positive_numbers)

#PATH II --- filter() function
# temp_lst = filter(lambda x: x>0, numbers) #geçici bir liste oluşturuldu, lambda fonksiyonunu küme tanımlamalarına benzetebilirsin
#* Geçici listede, numbers listesi içerisindeki x için, x>0 durumlarını temp_lst değişkenine ekle gibi bir çıkarım var.
# lst_positive_numbers_lambda = list(temp_lst) #gelen değişkeni listeye çevirdik.
# print(lst_positive_numbers_lambda)


