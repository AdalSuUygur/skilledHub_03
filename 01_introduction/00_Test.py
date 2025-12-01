
#? List Comprehensions (01-12-25, ders 14)

lst_1 = []
for i in range(10):
    lst_1.append(i)
print(lst_1)

#YA DA list comprehension ile kısa yoldan:

lst_2 = [i for i in range(10)]
print(lst_2)

#todo rastgele üretilmiş 10 sayı ile list comprehension uygulaması
from random import randint
lst_random = [randint(a=10, b=100) for _ in range(10)]
print(lst_random)

#todo rakamların karesinin list compehension ile oluşturulması
lst_3 = [i**2 for i in range(10)]
print(lst_3)

#todo 0-100 arasındaki çift sayıları listeye eklenmesi
lst_4 = [i for i in range(101) if i%2 == 0] #0 ile 100 dahil olsun diye
print(lst_4)

#todo içerisinde a harfi geçen meyvelerin listeye alınması
fruits = [
    "Apple", "Banana", "Orange", "Mango", "Pineapple",
    "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
    "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
    "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
]

lst_5 = [fruit for fruit in fruits if "a" in fruit.lower()]
print(lst_5)

#todo ternary if ile, meyve içerisinde "an" geçiyorsa true, geçmiyorsa false eklenen list comprehension
lst_6 = [True if "an" in fruit.lower() else False for fruit in fruits]
print(lst_6)

#todo çarpım tablosu, satır-sütun algoritması
#* SATIR SÜTUN ALGORİTMALARINDA: i satırı, j sütunu yönetir, yani i 1. adımındayken j orada belirtilen adım kadar çalışır.

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
    print("-------------------")


