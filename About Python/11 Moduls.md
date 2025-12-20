
#! Modülden Fonksiyon Çağırma
from random import randint #C ailesindeki randomizer gibi, farklı bir modül çağırmadım
#bu python içinde tanımlıdır ancak direkt kullanılmaz
#kullanılmak istenilince import edilinmeli

import random #olduğu gibi modülü importlar
from random import randint #burada ise random modülünden sadece randint fonksiyonu impotlanır, yani daha az maliyetli.

#? bir modülden 1-2 fonksiyon çağırılacaksa, spesifik olaral fonksiyonları çağırmak daha doğru (daha az maliyetli)
#? bir modülden 10 tane fonksiyon çağırılacaksa direkt modülün çağırılması daha doğru (daha az iş gücü)

random_number = randint(a = 0, b = 100)
print(random_number)