
#? List Comprehensions (01-12-25, ders 14)

lst_1 = []
for i in range(10):
    lst_1.append(i)
print(lst_1)

#YA DA list comprehension ile kısa yoldan:

lst_2 = [i for i in range(10)]
print(lst_2)

#rastgele üretilmiş 10 sayı ile list comprehension uygulaması
from random import randint
lst_random = [randint(a=10, b=100) for _ in range(10)]
print(lst_random)

#rakamların karesinin list compehension ile oluşturulması
lst_3 = [i**2 for i in range(10)]
print(lst_3)

#

