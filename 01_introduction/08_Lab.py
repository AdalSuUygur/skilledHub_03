
#? Zip fonksiyonu
#listeleri, tupleları, numply arraylerini yani koleksiyonları birbirleriyle eşleyerek birleştiren bir fonksiyon

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