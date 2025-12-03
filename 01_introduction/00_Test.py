
#region Benchmark Testing Hocanın Çözümü
from random import randint
import time
import tracemalloc


tracemalloc.start()
t1 = time.perf_counter()

# Sayı yaratırken aşağıdaki list comprehension kullanmak yerine generator pattern kullansaydınız işin rengi baya değişirdi. 
# Sayı üretim hızı dramatik birşekilde artardı ve zaman maliyeti azalırdı.
# numbers = [randint(a=-100, b=100) for _ in range(1000000)]
numbers = (randint(a=-100, b=100) for _ in range(1000000))

# List Comprehension
positive_number = [number for number in numbers if number > 0]

# Filter Func
# positive_number = list(filter(lambda x: x > 0, numbers))

# With For Loop
# positive_number = []
# for number in numbers:
#     if number > 0:
#         positive_number.append(number)

print(positive_number)

t2 = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

runtime_ms = (t2 - t1) * 1000
peak_memory = peak / 1024 / 1024

print(
    '===============================\n'
    'Method --> List Comprehension\n'
    f'Runtime: {runtime_ms}\n'
    f'Peak Memory: {peak_memory}'
    
)

"""
===============================
Method --> List Comprehension
Runtime: 5728.366099996492
Peak Memory: 28.39721393585205
===============================
Method --> Filter Func
Runtime: 3872.5149999954738
Peak Memory: 28.40944004058838
===============================
Method --> With For Loop
Runtime: 4765.219499997329
Peak Memory: 28.41720485687256
"""
