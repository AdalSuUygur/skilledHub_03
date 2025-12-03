
#todo Benchmark testing between listComprehension / lambdaFilter / forLoop
#Random sayılardan oluşan bir liste üretilir (a=-100, b=100)
#Path1 ile list comprehension, Path2 ile lambda filter, Path3 ile for loop ile pozitif sayılar ayıklanır.
#Bu pathler arasında benchmark testi yapılır.

from time import time_ns #nanosecond olarak ölçmeye yarayan fonksiyon
from random import randint #random sayı üretmeye yarayan fonksiyon
timer_start = time_ns()
timer_finish = time_ns()
import sys #sys modülünü çektik

#numbers = [randint(a=-100, b=100) for i in range(10000)] #numbers diye 10000 itemlı liste oluşturuldu
#bilgisayar zorlansın diye adet değişkeni tanımladım, ayrıca teste de yardımcı oldu.

ADET = 1_000_000 
print(f"{ADET} adet sayı üretiliyor, lütfen bekleyiniz")
# Sayı üretme süresini teste dahil etmiyoruz, o yüzden dışarıda yapıyoruz.
numbers = [randint(a=-100, b=100) for i in range(ADET)]
print("Sayılar üretildi, yarış başlıyor!\n" + "-"*50)


# --- PATH 1: List Comprehension ---
timer_start = time_ns() # Kronometreyi başlat

path_1 = [number for number in numbers if number > 0]
#print(path_1) #test

timer_finish = time_ns() # Kronometreyi durdur
sure_path1 = timer_finish - timer_start

size_path1 = sys.getsizeof(path_1) # Bellek Boyutu Ölçümü

print(f"Path 1 (List Comp) : {sure_path1:,} ns") #Okunabilirlik için binlik ayırıcı (,)
print(f"  Bellek Boyutu (Tahmini): {size_path1:,} byte")

del path_1 # Belleği serbest bırak


# --- PATH 2: Filter + Lambda ---
timer_start = time_ns() # Kronometreyi başlat

path_2_temp = filter(lambda x: x>0, numbers)
path_2 = list(path_2_temp)
#print(path_2) #test

timer_finish = time_ns() # Kronometreyi durdur

sure_path2 = timer_finish - timer_start
size_path2 = sys.getsizeof(path_2) # Bellek Boyutu Ölçümü

print(f"Path 2 (Filter)    : {sure_path2:,} ns")
print(f"  Bellek Boyutu (Tahmini): {size_path2:,} byte")

del path_2


#PATH3 for loop
timer_start = time_ns() # Kronometreyi başlat

path_3 = []
for number in numbers:
    if number > 0:
        path_3.append(number)
#print(path_3) #test

timer_finish = time_ns() # Kronometreyi durdur
sure_path3 = timer_finish - timer_start

size_path3 = sys.getsizeof(path_3)

print(f"Path 3 (For Loop)  : {sure_path3:,} ns")
print(f"  Bellek Boyutu (Tahmini): {size_path3:,} byte")
del path_3


print("-" * 30)


en_hizli = min(sure_path1, sure_path2, sure_path3)
if en_hizli == sure_path1: print("KAZANAN: Path 1 (List Comprehension)")
elif en_hizli == sure_path2: print("KAZANAN: Path 2 (Filter)")
else: print("KAZANAN: Path 3 (For Loop)")