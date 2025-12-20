
# #? tuples - demetler
# #* immutable
# #* listelerdeki gibi crud operasyonları yapılamıyor, sabitlerimizi tanımlayabileceğimiz bir yapı
# #* yapısı gereği okuma operasyonlarında daha hızlı

# #örneğin, bir data geliyor ve sadece okuma amaçlı kullanacağım
# #o zaman tuplea dönüştürüyorum
# #sadece okulayacaksam!!

# #data ieçrisinde update yapacaksak, veya manipülasyonlar yapılacaksa, yeni veriler eklenecekse lsite kullanılır
# #SADECE OKUMA YAPILACAKSA TUPLE KULLANILIR!!!

# tuple_1 = ("Galatasaray",
#            "Adana Demirspor",
#            "Beşiktaş",
#            "Trabzonspor",
#            "Fenerbahçe"
#            )

# tuple_2 = ("Red Skins",
#            "Seahawks",
#            "Vikings",
#            "Patriots"
#            )

# tuple_3 = tuple_1 + tuple_2 #max yapılabilecek işlem toplama
# #ve dilimleme/slicing yapılabilir
# print(tuple_3[2:5])

#nested tuple'lar veya liste içinde tuplelar tanımlanılabilir. bunlarda sınırlama yok.
#okuma amaçlı kullanılacağı zaman tuple tercih edilir!!!!

#? tuplelarda built in fonksiyonları yoktur çok çok az (nokta notasyonu, metoddan bahsediyo hoca saırım)