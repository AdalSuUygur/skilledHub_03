
#! TEKRAR ET, DERS NOTLARINI DÜZELT
# names = ["burak", "hakan", "ipek"]
# age = [36, 39, 41]

# # result = list(
# #     zip(names, age)
# # )
# # print(result)

# occupation = ["developer", "chemist"]

# result = list(
#     zip(names, age, occupation)
# )
# print(result)


#todo rastgele 10 tane sayı ile number1 ve number2 doldurulacak
# aynı indexlerde depolanan değerler toplanarak sonuçları liste olarak verilecek

from random import randint

#kendi çözümüm
# number1 = [randint(a= 0, b=100) for _ in range(10)]
# number2 = [randint(a= 0, b=100) for _ in range(10)]

# numbers = list(
#     zip(number1, number2)
# )
# print(numbers)

#region hocanın çözümü

number1 = [randint(a= 0, b=100) for _ in range(10)]
number2 = [randint(a= 0, b=100) for _ in range(10)]

temp_lst = list(
    zip(number1, number2)
)
print(temp_lst)
#buraya kadar okayiz, bunubende yaptım

result = [x+y for x,y in temp_lst]
print(result)

#fonksiyon açıklamalarındaki strict nedir araştır

#unzip
#notları tekrarla.
#list vs tuple
#dictionary ve onun built in fonksiyonları
#challenge CRUD sözlük üzerinden create, read, update, delete yapmaya çalış

#ödev:

matrix = [
    [34, 56, 123, 56], #bu iç listeler list comprehensytion ile rastgele sayılarla doldurulacak
    [23, 67, 12, 45] # 3 line yeterli
]

#output:
#[(34, 23, .. ) ... ] #zip ile

#mor küp fonksiyon
#yeşilimsi sembol class demek? 
#bunlara bir bakmak lazım, aralarında fark ne
#sadece belli classlara uygulanan fonksiyonlara ne deniyor?
#generic class da var mesela






















lst = ['ayhan', 'elton', 'adal', 'merve']

print(
    list(zip(range(len(lst)), lst))
)

character_1 = 'xyz'
character_2 = 'XYZ'

print(
    list(
        zip(character_1, character_2)
    )
)

matrix = [
    [34, 56, 123, 56], # --> bu iç listeler list comprehnsion ile rastgele sayılar ile doldurulacak
    [23, 67, 12, 45],
    [11, 54, 89, 22], # --> 3 line yeterli
]

# Output:
# [(34, 23, 11), (56, 67, 54), (123, 12, 89), ....]

# list vs tuple
# prons & cons

# dictionary, built-in, CRUD operasyonularını sözlük üzerinden uygulayın.

#* Derin sulara atlarsak beceremediğimizde arzu ve şevke ket vuran hormonlar salgılanabilir.
#* Ama başarılı olursa bu sefer de inanılmaz seratonin hormonları salgılanır. 
#* Bu yüzden aslında çok bilmediğimiz noktalara ayak basmamak lazım bazen heves kırmamak için.