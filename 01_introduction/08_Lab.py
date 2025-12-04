
#? Zip fonksiyonu
#listeleri, tupleları, numply arraylerini yani koleksiyonları birbirleriyle eşleyerek birleştiren bir fonksiyon

names = ["burak", "hakan", "ipek"]
age = [36, 39, 41]

# result = list(
#     zip(names, age)
# )
# print(result)

occupation = ["developer", "chemist"]

result = list(
    zip(names, age, occupation)
)
print(result)
