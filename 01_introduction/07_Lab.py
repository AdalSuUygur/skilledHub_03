
#region 16. Ders 04/12/25 
#any-map olacak yarınki derste
#* any içinde herhangi bir şey tutuyosa true, tutmuyosa false dönüyor






# passwords = ["123", "98a", "12q", "987"]

# print(
#     any(ch.isalpha() for pwd in passwords for ch in pwd)
# )

# #nested for yaptık
# for pwd in passwords:
#     for ch in pwd:
#         print(any(ch.isalpha()))

#todo is password valid uygulaması

#min 16 karakter
#min 1 büyük 1 küçük harf
#min 1 noktalama işareti
#min 1 rakam
#hint: string kütüphanesi noktalama işaretleri hazır olarak var

#region kendi deneme başlangıcım da tam oturmadı kafama
# password = input("şifre: ")
# #sample PWD: beast?Beast1beast

# is_karaktersiniri = len(password)
# is_kucukharf = any(char.isupper for char in password)
# is_buyukharf = any(char.isupper for char in password)
# is_noktalamaisareti = any(char.ispuncti for char in password)
# is_rakam = any(char.isupper for char in password)
#endregion

#region hocanın çözümü
# from string import punctuation

# password = input('Password giriniz: ')

# if len(password) < 16:
#     print("invalid password")
# if not any(ch.isupper() for ch in password):
#     print("invalid password")
# if not any(ch.islower() for ch in password):
#     print("invalid password")
# if not any(ch.isdigit() for ch in password):
#     print("invalid password")
# if not any(ch in punctuation for ch in password):
#     print("invalid password")


# #*logic mantığı

# if (
#     len(pwd) < 16 and
#     not any(ch.isupper() for ch in pwd)
#     #and ile bağlayıp herhangi bir şey
# ):
#     print()

#endregion

#region hasan çözümü
# import string
# password = input("Şifreyi gir: ")
# uzunluk = len(password) >= 16
# b_harf  = any(ch.isupper() for ch in password)
# k_harf  = any(ch.islower() for ch in password)
# rakam  = any(ch.isdigit() for ch in password)
# noktalama = any(ch in string.punctuation for ch in password)

# if uzunluk and b_harf and k_harf and rakam and noktalama:
#     print("Şifre geçerli.")
# else:
#     print("Şifre geçersiz.")
#     if not uzunluk:
#         print("16 karakterden az olamaz.")
#     if not b_harf:
#         print(" büyük harf içermeli.")
#     if not k_harf:
#         print(" küçük harf içermeli.")
#     if not rakam:
#         print("rakam içermeli.")
#     if not noktalama:
#         print(" özel karakter içermeli.")  
# print(f"Girilen şifre: {password}")
#endregion

