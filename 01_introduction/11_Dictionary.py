
#! DICTIONARIES - SÖZLÜKLER
#* Koleksiyondur, key-value ile çalışır.
#* Sırasızlardır ve değiştirilebilirler ancak key value'ları eşsizdir. Değiştirlemezler, sabitlerdir.
#* Key(anahtar) tanımlanır karşılığında value tanımlanır.
#* key value ile çalışır

#? SYNTAX Yapısı
# Sözlükler süslü parantez "{}" ile tanımlanır. Set'ten farkı ne? Sette Key:Value şeklinde tanımlama yapılamaz.
# Sözlükte ise yapısından gereği tanımlama key:value şeklinde olmalıdır.

# sözlük_ismi = {key : value} şeklinde tanımlama yapılır.

release_year_movie = { #Sözlüğün ismi,
    'Fight Club': 1999, #İlk elemanı, Key: Fight Club, Value: 1999.
    #Neden key ismi? Çünkü aynı isimde tek film olur, ancak 1999 yılında 1 film olmaz.
    'Matrix': 1999,
    'Interstaller': 2014,
    'Inception': 2018,
    'Dune': 2021
}

#? CRUD Operasyonları

#* Create:
# Sözlüğe yeni bir item ekleneceğinde key:value şeklinde eklenmelidir.

release_year_movie["Dune II"] = 2023 # "Dune II" keyiyle bir item ekledik, value'su da 2023

#* Read: "Fight Club" anahtarında tutulan value değerlerini okumak için
# Path I
print(release_year_movie["Fight Club"])

# Path II
print(release_year_movie.get("Fight Club"))

# get ALL values: #Tüm VALUEları okur
for value in release_year_movie.values():
    print(value)

# get ALL keys: #Tüm KEYleri okur
for keys in release_year_movie.keys():
    print(keys)

#get ALL items: #HER ŞEYİ OKUR
for key,value in release_year_movie.items():
    print(
        f"Movie name: {key}\n"
        f"Release year: {value}"
    )

#* Update: "Dune II"nin çıkış tarihini yanlış yazdığımızı varsayalım ve value değerini 2024 yapalım

release_year_movie.update( #update fonksiyonu bizden sözlük ister
    {
        "Dune II": 2024
    }
)

#* Delete:

del release_year_movie["Dune II"]
print(release_year_movie)
