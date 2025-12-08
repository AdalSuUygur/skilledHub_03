
boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewix', "Evander Holyfiled", "George Foreman"]
#? Listenin sonuna "Rocky Marciano"
# boxers.append("Rocky Marciano") #Listenin sonuna ekler
# #nokta notasyonu = bir objenin sonuna nokta konulduğunda ona ait features/functions gelir.
# print(boxers)

#? Kullanıcıdan alınan boksör ismini yine kullanıcıdan alınan index değerine yazdıralım
# boxer_name = input("Name: ")
# index_value = int(input("Index: "))
# boxers.insert(index_value, boxer_name)
# print(boxers)

#? Merge Two Lists 
# royal_division = ["Antorny Jasua", "Tyson Fury", "Deantony Wilder"]
# boxers.extend(royal_division)
# print(boxers)

#? Read an Item
# print(boxers[2])

#? 5. indexte bulunan itemı "Joe Frazeir" ile değiştirin.
# boxers[5] = "Joe Frazeir"
# print(boxers)

#? 0. Indexteki elemanı silelim
# boxers.pop(0)
# print(boxers)

#YA DA

# #boxers.remove("Lenox Lewix")
# print(boxers)

#? Listedeki içindeki itemları alıp işleme sokulması, yani teker teker sırayla dolaşılması
# for boxer in boxers: #boxer geçiçi bir isim olarak verildi burada.
#     print(boxer)

# for i in range(len(boxers)): #boxers listesinin uzunluğu kadar
#     print(boxers[i])

# for ch in 'adal su': #"adal su" kısım da string aslında liste mantığı gibi çalışabilir.
#     print(ch,end='-') #bundaki her karakteri de teker teker dolaşabiliyorum.

#todo 10ar tane rastgele sayı üretilip 2 listeye eklenecek. 3. listeye aktarılacak. append kullanılması yasak, index mantığıyla çalışılacak.
lst_1 = []
lst_2 = []
lst_3 = []
from random import randint

#region kendi çözümüm
for i in range(10):
    sayi_1 = randint(a=0,b=100)
    lst_1.insert(i, sayi_1)
    sayi_2 = randint(a=0,b=100)
    lst_2.insert(i, sayi_2)
    lst_3.insert(i, lst_1[i] + lst_2[i])
print(lst_1)
print(lst_2)
print(lst_3)
#endregion

#region hocanın çözümü
for i in range(10):
#    print(randint(a=0,b=100)) #1. adım, ürettik evet 10 tane
    lst_1.insert(i, randint(a=0,b=100)) #2. adım ooh hemen üretilen kodla lst_1'e ekleyek
    lst_2.insert(i, randint(a=0, b=100)) #4. adım, bak bunu da ürettik hatta test edelim yine.
    lst_3.insert(i, lst_1[i]+lst_2[i]) #6. adım, oh misler gibi çalıştı bak, bir deyazdıralım da görelim
#print(lst_1) #3. test adımı, ee düzgün çalışıyor demekki o zaman lst_2'ye de aynı şekilde ekleyek
#print(lst_2) #5. adım, çözdük, o zaman devamke
print(f"{lst_1}\n{lst_2}\n{lst_3}")
#endregion

