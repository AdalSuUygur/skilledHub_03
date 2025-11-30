
#? FOR DÖNGÜSÜ
* in - range()

? in operatörü
print('s' in 'su') #su içinde s varsa true döner
print('a' in 'su') #içinde mi

? not in operatörü
print('s' not in 'su') #su içinde s yoksa true döner
print('a' not in 'su') #içinde değil mi

? range() fonksiyonu - built in fonksiyon.
for i in range(19):
    print(i) #tek sayı verdik, başlangıç değeri 0, artış miktarı 1

for i in range(3,6):
    print(i) #2 değer verirsek ilk değer başlangıç, ikinci değer bitiş, artış miktarı 1

for i in range(5,65,3):
    print(i) #başlangıç, bitiş, artış miktarı olarak sıralandı.

todo kullanıcıdan başlangıç bitiş ve artış miktarlarını alalım ve bunları yazdıralım
start = int(input("Başlangıç: "))
finish = int(input("Bitiş: "))
step = int(input("Artış miktarı: "))

for i in range(start, finish, step):
    print(i,end=" ")

todo 0-100 arası sayıları ekrana yazdıralım
for i in range(0,100):
    print(i, end="-")

todo 0-100 arası tek sayıların ve çift sayıların toplamını yazdıran program
toplam_cift = 0
toplam_tek = 0

for i in range(0,100,1):
    if i % 2 == 0:
        toplam_cift += i
    else:
        toplam_tek += i

print(f"Çiftlerin toplamı = {toplam_cift}\nTeklerin toplamı = {toplam_tek}")

from random import randint #randomizer gibi, farklı bir modül çağırmadım
#bu pyton içinde ama direkt kullanılmaz, kullanmak istenilince import edilinmeli
#kaynak kodlarda

from random import randint #burada ise random modülünden sadece randint importluyorum, yani daha az maliyetli.
import random #olduğu gibi modül importluyorum

#doğru iş yapmak senaryoya göre değişir.
#bir modülden 1-2 fonk çağıracaksam ilki doğru
#bir modülden 10 tane fnk çağırcaksam ikincisi doğru.


random_number = randint(a = 0, b = 100)
print(random_number)

for i in range(1,11):
    random_number = randint(a = 0, b = 100)
    print(f'{i}. üretilen sayı = {random_number}')

i = 0
while i < 10:
    random_number = randint(a=213, b=32425)
    i += 1
    print(f'{i}. üretilen sayı = {random_number}')

todo random bir sayı üretilir, kullanıcının 3 tahmin hakkı var. Doğru bilirse sayıyı bildiriliyor. Yanlış bilirse bildiriliyor.
from random import randint
deneme = 3
i = 1

random_sayi = randint(a=0,b=10)

while i <= deneme:
    tahmini_sayi = int(input("Tahmininiz: "))
    if tahmini_sayi ==  random_sayi:
        print("Doğru bildiniz")
        break
    else:
        print(f"{i}. hakkınız, yanlış tahmin.")
    i += 1
