
# # #challenge CRUD sözlük üzerinden create, read, update, delete yapmaya çalış
# # list vs tuple
# # prons & cons
# # set()
# # dictionary, built-in, CRUD operasyonularını sözlük üzerinden uygulayın.




#? DICTIONARIES
#süslü parantez ile tanımlanır
#key value ile çalışır
#anahtar tanımlanır karşılığında anahtar tanımlanır
#genelde keyler için tuplelar kullanılır

release_year_movie = { #sol taraf key sağ taraf value
    'Fight Club': 1999,
    'Matrix': 1999,
    'Interstaller': 2014,
    'Inception': 2018,
    'Dune': 2021
}

# #region read
# #todo fight club anahtarında tutulan value ekrana yazdırın
# #path i
# print(release_year_movie["Fight Club"])
# #path ii
# print(release_year_movie.get("Fight Club"))

# #end region

# #get ALL values:
# for value in release_year_movie.values():
#     print(value)

# #get ALL keys: 
# for keys in release_year_movie.keys():
#     print(keys)

# #get ALL items:
# for key,value in release_year_movie.items():
#     print(
#         f"Movie name: {key}\n"
#         f"Release year: {value}"
#     )

# #endregion

#region create item
# yeni bir item eklerken de: key - value olarak eklemek gerek sözlüğün yapısından dolayı
release_year_movie["Dune II"] = 2023
print(release_year_movie)

#endregion

#region update
#dune ii'nin çıkış tarihini 2024 yapalım:

release_year_movie.update( #update fonksiyonu bizden sözlük ister
    {
        "Dune II": 2024
    }
)

#endregion

#region delete
#path i
del release_year_movie["Dune II"]
print(release_year_movie)

#endregion

#todo ödev

