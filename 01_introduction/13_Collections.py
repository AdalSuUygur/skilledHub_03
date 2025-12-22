
#todo E-Ticaret Sepet Analizi
#* Sistemde bir hata olmuş ve bazı ürünlerin fiyatı negatif (`-`) girilmiş. Ayrıca 100 TL üzerindeki ürünlere %10 indirim yapman gerekiyor.
# fiyatlar = [150, -20, 300, 50, -5, 120]

# pozitif_fiyatlar = [(fiyat * -1) if fiyat < 0 else fiyat for fiyat in fiyatlar]
# print(pozitif_fiyatlar) #test, pozitifleri gördük

# indirimli_fiyatlar = [(fyt * 0.9) if fyt > 100 else fyt for fyt in ((fiyat * -1) if fiyat < 0 else fiyat for fiyat in fiyatlar)]
#tekrar list comprehension ile yaptım
#memory efficienct için generator kullandım pozitif fiyatlar için
#bunu ayrıca bir liste oluşturarak tanımlamadım ki hepsini list comp. içine alabileyim.
# print(indirimli_fiyatlar)

#todo Gelen iki data sheetten biri "İstanbul Müşterileri", diğeri "Geçen Ay Alışveriş Yapanlar". Ortak olanları sil ve istanbulda oturup geçen ay alışveriş yapmayanları bul.
# istanbul = ["a@mail.com", "b@mail.com", "a@mail.com", "c@mail.com"]
# alanlar = ["b@mail.com", "d@mail.com", "b@mail.com"]

# print(set(item for item in istanbul)) #set comprehension
# print(set(item for item in alanlar)) #tekrar eden elemanlardan arındırdık

# print(
# set(item for item in istanbul) #istanbulda oturup
# - #fark operatorü
# set(item for item in alanlar) #geçen ay alışveriş yapmayanları
# )

#todo Kelime Frekansı (Dictionary) Elinde bir cümle var ve hangi kelimenin kaç kere geçtiğini bulman gerekiyor.
metin = "elma armut elma kiraz elma armut"
meyveler = metin.split()

#Path I:
# frekanslar = {}
# for meyve in meyveler:
#     if meyve not in frekanslar.keys():
#         frekanslar[meyve] = 1
#     else:
#         frekanslar[meyve] += 1
# print(frekanslar)

#Path II: Dict Comprehension denedim ama çalışmadı çünkü bu blok içinde atama veya artırma yapamıyorum.
#frekanslar = {frekanslar[meyve] = 1 if meyve not in frekanslar else frekanslar[meyve] += 1 for meyve in meyveler}

#onun yerine gemini illaki oluşturcaksa böyle oluşturalım dedi.

# "Her meyve için: Anahtar=Meyve, Değer=Listede Kaç Tane Var?"
# frekanslar = {meyve: meyveler.count(meyve) for meyve in meyveler}
# print(frekanslar)

#todo List, Dict ve Zip (fermuar) mantığı

isimler = ["Ali", "Ayşe", "Mehmet"]
notlar = [85, 90, 70]

#Path I:
# sozluk = {
#     isim: score for isim,score in zip(isimler, notlar)
# }

#Path II:
# sozluk = dict(zip(isimler, notlar))
# print(sozluk)
