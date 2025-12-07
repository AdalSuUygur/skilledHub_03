
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

#todo filter fonksiyonu ile çift sayıların filtrelenip ve liste olarak ekrana yazdırılması
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)








# #todo verilen listeden tam ve ondalıklı sayıları alma uygulaması
# lst = [None, "b", 3.14, False, 9, "Oscar Piastri"]
# # Burdan sadece tam ve ondalıklı sayıları almamız gerek.

# numbers = list( #listeye convert etmek için.
#     filter(lambda x: isinstance(x, (int, float)), lst) #x yani lstedeki eleman int veya float mı
# )
# print(numbers) #çıktı olarak da: [3.14, False, 9] verir, çünkü isinstance değeri bool döndürür, bundan dolayı direkt öyle bir ifadeyi çıktı olarak verir.






# #todo sonu .com ile biten mail adreslerini filter fonksiyonu ile yazdıran ifade
# # #* Hint: endswith() fonksiyonunu kullan

# # mails = [
#     "burak.yilmaz@outloo.com", 
#     "savage@mail.com", 
#     "beast@", 
#     "keko@com.xyz", 
#     "adal@gmail.com"
# ]

# correct_mails = (list(
#     filter(
#         lambda x: x.endswith(".com"), mails)
#     )
# )
# print(correct_mails)

# #todo Verilen listedeki değerlerin karşılığı sayısal ise bunu yazdıran uygulama
# #* Hint: isgidit() fonksiyonunu kullan

# some_values = ["123", "burak", "zxc", "987", "345"]
# number_values = list(
#     filter(
#         lambda x: x.isdigit(), some_values
#     )
# )
# print(number_values)

# #Hocanın çözümü: Lambda fonksiyonu bir performans sorunudur, bunu engellemek için kullanmadan yapalım:
# only_digit = list(
#     filter(str.isdigit, some_values) #! lambdadan kurtulduk burda 
#                                      #! built in fonksiyonlarını tiplerine özel olarak çalıştırabiliriz. 
#                                      #! yani lambdayı built in fonksiyonlar özelinde kullanmayabiliriz.
# )
# print(only_digit)
# #* python, içerisindeki built in fonksiyonları kullandığımız zaman daha hızlı çalışır.

