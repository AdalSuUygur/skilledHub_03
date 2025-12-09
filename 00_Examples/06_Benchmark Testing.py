
#region listComprehension / lambdaFilter / forLoop
#todo Benchmark testing between listComprehension / lambdaFilter / forLoop
#Random sayılardan oluşan bir liste üretilir (a=-100, b=100)
#Path1 ile list comprehension, Path2 ile lambda filter, Path3 ile for loop ile pozitif sayılar ayıklanır.
#Bu pathler arasında benchmark testi yapılır.

"""
numbers list comprehension ile üretilmiş çıktılar  |    numbers generator pattern kullanılarak üretilmiş çıktılar
------------------------------------------------------------------------------------------------------------------
Kullanılan path: List Comprehension                |    Kullanılan path: List Comprehension  
Çalışma Süresi: 83.36 ms                           |    Çalışma Süresi: 10282.66 ms
Hafıza Kullanımı: 3.98 MB                          |    Hafıza Kullanımı: 3.99 MB
------------------------------------------------------------------------------------------------------------------
Kullanılan path: Filter Lambda                     |    Kullanılan path: Filter Lambda  
Çalışma Süresi: 450.64 ms                          |    Çalışma Süresi: 10715.42 ms
Hafıza Kullanımı: 3.98 MB                          |    Hafıza Kullanımı: 3.99 MB
------------------------------------------------------------------------------------------------------------------
Kullanılan path: For Loop                          |    Kullanılan path: For Loop
Çalışma Süresi: 300.29 ms                          |    Çalışma Süresi: 10633.53 ms
Hafıza Kullanımı: 3.98 MB                          |    Hafıza Kullanımı: 3.99 MB
------------------------------------------------------------------------------------------------------------------
"""

from random import randint #random sayı üretmeye yarayan fonksiyon
import tracemalloc #memory hesabı için kullanacağız
import time #timer kurmamız için gerekli olan hesap

# def benchmark_start():
#     timer_start = time.perf_counter()
#     tracemalloc.start()
# #döndürdüğümüz değer:
#     return timer_start

# def benchmark_finish(timer_start):
#     timer_finish = time.perf_counter() #zamanlayıcıyı durdurduk
#     current, peak = tracemalloc.get_traced_memory() #current ve peak memory değerlerini aldık
#     tracemalloc.stop() # ve bellek izlemeyi de durdurduk
# # Şimdi hesaplamalar:
#     runtime_ms = (timer_finish - timer_start) * 1000 #saniyeyi milisaniyeye çevirmek için 1000 ile çarptık
#     peak_memory_mb = peak / 1024 / 1024 #byte'ı mb'a çevirdik.
# # Döndürdüğümüz değerler:
#     return runtime_ms, peak_memory_mb

# ADET = 1_000_000 #100milyon
# print(f"{ADET} adet sayı üretiliyor, lütfen bekleyiniz")

#* Sayı yaratırken list comprehension kullanmak yerine generator pattern kullanılsaydı sayı üretim hızı dramatik birşekilde artardı ve zaman maliyeti artırırdı.
#numbers = [randint(a=-100, b=100) for _ in range(ADET)] #list comprehension ile
#numbers = (randint(a=-100, b=100) for _ in range(ADET)) #generator pattern ile

#path i -- List comprehension
# p1_start = benchmark_start()
# p1 = [number for number in numbers if number > 0]
# p1_runtime, p1_peak = benchmark_finish(p1_start)

# print(f"Kullanılan path: List Comprehension\n"
#       f"Çalışma Süresi: {p1_runtime:.2f} ms\n"
#       f"Hafıza Kullanımı: {p1_peak:.2f} MB")

#path ii - filter lambda function
# p2_start = benchmark_start()
# p2 = list(
#     filter(
#         lambda x: x > 0, numbers
#     )
# )
# p2_runtime, p2_peak = benchmark_finish(p2_start)

# print(f"Kullanılan path: Filter Lambda\n"
#       f"Çalışma Süresi: {p2_runtime:.2f} ms\n"
#       f"Hafıza Kullanımı: {p2_peak:.2f} MB")


#path iii - for loop
# p3_start = benchmark_start()
# p3 = []
# for number in numbers:
#     if number > 0:
#         p3.append(number)
# p3_runtime, p3_peak = benchmark_finish(p3_start)

# print(f"Kullanılan path: For Loop\n"
#       f"Çalışma Süresi: {p3_runtime:.2f} ms\n"
#       f"Hafıza Kullanımı: {p3_peak:.2f} MB")

#endregion

#region without tryExcept / tryExcept / raiseException
# todo Benchmark testing between without tryExcept / tryExcept / raiseException
import time
import tracemalloc
bolunen = 2
bolen = 0

"""
0'a bölünemez.
Çözüm yolu: If Bloğu (without tryExcept)
Runtime ms: 297.80 micro seconds
Peak memory: 664.00 Bytes
----------------------------------------------------
Because of division by zero program cannot continue.
Çözüm yolu: With tryExcept
Runtime ms: 288.20 micro seconds
Peak memory: 664.00 Bytes
----------------------------------------------------
Sıfıra bölünen bir sonuçta type error veririm.
Çözüm yolu: raiseException
Runtime ms: 298.10 micro seconds
Peak memory: 664.00 Bytes
"""

# def benchmark_start():
#     timer_start = time.perf_counter()
#     tracemalloc.start()
#     return timer_start

# def benchmark_finish(timer_start):
#     timer_finish = time.perf_counter()
#     current, peak = tracemalloc.get_traced_memory()
#     tracemalloc.stop()
#     runtime_micros = (timer_finish - timer_start) * 1000 * 1000
#     return runtime_micros, peak

#path i -- without TryExcept
# p1_start = benchmark_start()
# if bolen == 0:
#     print("0'a bölünemez.")
# else:
#     sonuc = bolunen/bolen
# p1_runtime, p1_memory = benchmark_finish(p1_start)
# print(f"Çözüm yolu: If Bloğu (without tryExcept)\n"
#       f"Runtime ms: {p1_runtime:.2f} micro seconds\n"
#       f"Peak memory: {p1_memory:.2f} Bytes")

#path ii -- with tryExcept
# p2_start = benchmark_start()
# try:
#     result = bolunen / bolen
# except ZeroDivisionError as err:
#     print(f"Because of {err} program cannot continue.")
# p2_runtime, p2_memory = benchmark_finish(p2_start)
# print(f"Çözüm yolu: with tryExcept\n"
#       f"Runtime ms: {p2_runtime:.2f} micro seconds\n"
#       f"Peak memory: {p2_memory:.2f} Bytes")

#path iii -- raiseException
# p3_start = benchmark_start()
# try:
#     if bolen == 0:
#         raise TypeError("Sıfıra bölünen bir sonuçta type error veririm.")
#     result = bolunen / bolen
# except TypeError as err:
#     print(err)
# p3_runtime, p3_memory = benchmark_finish(p3_start)
# print(f"Çözüm yolu: raiseException\n"
#       f"Runtime ms: {p3_runtime:.2f} micro seconds\n"
#       f"Peak memory: {p3_memory:.2f} Bytes")

#endregion

#region listComprehension / forLoop
#todo Satır sutün algoritması için de time ve memory cost hesapla.
#* SATIR SÜTUN ALGORİTMALARINDA: i satırı, j sütunu yönetir, yani i 1. adımındayken j orada belirtilen adım kadar çalışır.
import time
import tracemalloc

"""
Çözüm yolu: Geleneksel yöntem
Runtime ms: 6622.30 micro seconds
Peak memory: 664.00 Bytes
---------------------------------------
Çözüm yolu: List comprehension
Runtime ms: 592.70 micro seconds
Peak memory: 12708.00 Bytes
"""

# def benchmark_start():
#     timer_start = time.perf_counter()
#     tracemalloc.start()
#     return timer_start

# def benchmark_finish(timer_start):
#     timer_finish = time.perf_counter()
#     current, peak = tracemalloc.get_traced_memory()
#     tracemalloc.stop()
#     runtime_micros = (timer_finish - timer_start) * 1000 * 1000
#     return runtime_micros, peak

#forLoop:
# timer_forLoop = benchmark_start()
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i * j}")
# runtime_forLoop, peak_forLoop = benchmark_finish(timer_forLoop)
# print(f"Çözüm yolu: forLoop\n"
#       f"Runtime ms: {runtime_forLoop:.2f} micro seconds\n"
#       f"Peak memory: {peak_forLoop:.2f} Bytes")

#List comprehension ile yapılması:
# timer_comprehension = benchmark_start()
# print(  [
#     f"{i} x {j} = {i * j}" #yazdırılacak sonuç 
#     for i in range(1,11) #en dış döngü
#     for j in range(1, 11) #en iç döngü
#     ]   )
# runtime_comprehension, peak_comprehension = benchmark_finish(timer_comprehension)
# print(f"Çözüm yolu: List comprehension\n"
#       f"Runtime ms: {runtime_comprehension:.2f} micro seconds\n"
#       f"Peak memory: {peak_comprehension:.2f} Bytes")

#endregion
