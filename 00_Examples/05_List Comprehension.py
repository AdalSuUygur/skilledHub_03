
#todo Girilen data sheetten ilkisim.soyisim@outlook.com şeklinde mail_adresses üretilip ekrana yazdırılan uygulama.
#* İpucu1: split() fonksiyonu
#* İpucu2: bir listenin uzunluğu ne olursa olsun son elemanına nasıl ulaşırım
users = ["Burak Yılmaz", "Adal Su Uygur", "Yasemin Uygur Erdem", "Sami Lütfü Esen Berk"]
domain_name = "@outlook.com"

#path i - list comprehension
# for names in users:
#     #print(names) #test
#     divided_names = names.lower().split(" ")
#     print(divided_names) #test
#     mail_adresses = [f"{divided_names[0]}.{divided_names[-1]}{domain_name}" for item in divided_names]
#     print(mail_adresses) #test

#path ii - for loop
# mail_addresses = []
# mail_uzantisi = "@outlook.com"
# for user in users:
#     name_slices = user.split(" ")
#     ilkisim = name_slices[0]
#     soyisim = name_slices[-1]
#     mail_addresses.append(f"{ilkisim}.{soyisim}{mail_uzantisi}")
# print(mail_addresses)

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

