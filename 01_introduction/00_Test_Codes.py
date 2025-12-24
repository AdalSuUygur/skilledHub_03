
#todo Ödev (22 Aralık Ödevi-2): Girilen bilgilerin doğruluğunu check eden fonksiyon yapılarıyla kurulmuş uygulama

#* 1 sign in ve sign up
#* sign up işleminde kullanıcının girdiği password valid mi, user_name unique mi? e_mail valid mi?
#* bu kurallardan geçerse üyelik işlemi tamamlanacak
#* sign inta da yine pass word doğru mu bu sefer, e-mail ve password doğruysa giriş yap
#* veri yapısı: 
#* aşağıda sample data structure

users = {
    "adal": {"adal@skilledhub.com": "Adal.123"},
    "su": {"su@outlook.com": "Su.123"},
    "ahmet": {"ahmet@gmaiwindowslive.com": "Ahmet.123"},
    "mehmet": {"mehmet@skilledhub.com": "Mehmet.123"},
    "kerim": {"kerim@hotmail.com": "Kerim.123"},
    "cemal": {"cemal@yahoo.com": "Cemal.123"},
    }

print(
users.values() # bu liste içinde de sözlük var
)

for item in users.values(): 
    print(item) #item şu an iç sözlük yapısı
    print(item["cemal@yahoo.com"]) #bu şifreler






# def check_login(identity: str, input_password: str) -> bool:
#     # Tüm çekmeceleri (kullanıcıları) tek tek gezelim
#     for username, details in users.items(): 
#         if identity == username or identity == details["email"]: # Eğer girdiğimiz kimlik, kullanıcı adına EŞİTSE veya o çekmecedeki mail'e EŞİTSE
#             if input_password == details.values(): # O zaman şifreyi kontrol et
#                 return True
#     return False

# username = input("Username/mail: ")
# password = input("password: ")
# is_login = check_login(username, password)

# def is_in_domain_names(domain_name: str = "skilledHub.com") -> bool:
#     domain_names = [
#         "gmail.com",
#         "hotmail.com",
#         "windowslive.com",
#         "yahoo.com",
#         "outlook.com",
#         "skilledHub.com"
#     ]
    
#     if domain_name in domain_names:
#         return True
#     else:
#         return False
    
# def user_database(username: str, mail: str, password: str):
#     user_database = {
#         (username, mail) : password
#     }
#     #sözlük olcan, anahtar username ya da e-mail, şifre 1 tane olmalı. yani value da bu











# # Büyük Arşiv Dolabı (Dış Sözlük)
# users = {
#     "maledordana": { # Çekmece ismi (Key)
#         "email": "maledordana@hotmail.com", # Çekmecenin içindeki bilgiler (İç Sözlük)
#         "password": "Sifre123!",
#         "level": 5
#     },
#     "deniz_123": {
#         "email": "deniz@mail.com",
#         "password": "Password99",
#         "level": 2
#     }
# }




















import string
def is_valid_password(password: str) -> bool: #uygunsa true, değilse false olarak döner
    min_character = 6
    if len(password) <= min_character:
        return False
    
    if any(ch.isspace() for ch in password): #burda da boşluk var mı yok mu
        return False

    checks = [
    any(ch.islower() for ch in password),
    any(ch.isupper() for ch in password),
    any(ch.isdigit() for ch in password),
    any(ch for ch in password if ch in string.punctuation)
            ]
    
    return all(checks)


def sign_up():
    pass

def sign_in():
    pass


domain_name = "skilledHub.com"

def verify_email(email: str, domain_name: str) -> str:
    if email == "":
        return "Email kısmı boş bırakılamaz"
    elif not email.endswith(f"@{domain_name}"):
        return "Mailinizin domain ismi sistemimizde kayıtlı değildir, lütfen farklı bir mail adresi ile deneyin."
    else:
        return "Mailinize gönderilen onaylama mailindeki linke tıklayarak üyeliğinizi aktif olarak kullanabilirsiniz."

