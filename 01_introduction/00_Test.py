#ödev


#! ödev: 10 000 tane sayı üretilir,
#liste oluşturulur (comprehension ise)
#bir timer bunun başına ve sonuna, birbirlerinden çıkartıp kaç nanosecond tuttuğu ve PATH1
#filter fonksiyonunun başına ve sonuna timer koyup çıkartıp kaç nanosecond tuttuğunu PATH2
#bir de for döngüsü ile kurulan listeye bir timer koy PATH3
#pathler içinde benchmark testi
#yetmez, memory de ölçerim diyosan ölç! yabay zekadan yararlan (ne yabay? XDDDD)

from time import time_ns #nanosecond olarak ölçmeye yarayan fonksiyon
from random import randint #random sayı üretmeye yarayan fonksiyon
timer_start = time_ns()
timer_finish = time_ns()

timer_start = time_ns()
#PATH1
path_1_numbers = [randint(a=-100,b=100) for i in range(10000) if path_1_numbers > 0] #10k random sayı üretilen program, list comprehension
timer_finish = time_ns()

#PATH2
path_2_numbers = [randint(a=-100,b=100) for i in range(10000)]
path_2_temp = filter(lambda x: x>0, path_2_numbers)
path_2_positive_numbers = list(path_2_temp)

#PATH3
path_3_numbers = []
path_3_positive_numbers = []
for i in range(10000):
    path_3_numbers.append(i)
for number in numbers:
    if number > 0:
        path_3_positive_numbers.append(number)


