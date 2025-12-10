
#hatalarım
# u_plus_p = list(zip(*(username for username in users))) #bu yapı bana usernames listesi ve şifreler listesi verdi, ben burdan usernames çekmeye çalışıyorum

#todo Doğru loginde, ürün search ve fiyat output. Yanlış loginde yeni kayıt. Username'ler unique olacak.

#bütün ürünlerin toplam fiyatı nedir
#ürün adı laptop olan ürünlerin fiyatlarını toplayalım
#kullanıcı ürün search edebilsin, yani ürün search etti monitör yazdı varsa fiyatını verdi
#fiyatı 200 tl altında olan ürünler listelensin
#register olsun, yani kayıt da olsun; username varsa hali hazırda ekleyemesin

users = [
    ["beast", "123"],
    ["bear", "456"],
    ["keko", "789"]
]

def is_login(user_name, pass_word):
    for USERNAME, PASSWORD in users:
        if user_name == USERNAME and pass_word == PASSWORD:
            return True
    return False

username = input("Username: ").lower()
password = input("Password: ")
case_login = is_login(username, password)

while not case_login:
    sign_in = input("Wrong entry, would you like to sign up(1) or try to sign in again?(0): ")
    match sign_in:
        case "1":
            #* case1 içini çalıştıramadım, şu an giriş alsa bile eklemiyor sanırım listeye, debug gerek
            # new_username = input("Please enter a username: ").lower()
            # usernames = list(zip(*users))[0]
            # if new_username not in usernames:
            #     new_password = input("Please enter password: ")
            #     users.append([new_username, new_password])
            #     print("Welcome, you can login with new informations now.")
            #     username = input("Username: ").lower()
            #     password = input("Password: ")
            #     new_case_login = is_login(username, password)
            # else:
            #     new_case_login = False
            # if not new_case_login:
            #     break
#* case0 sorunsuz çalışıyor, kendime hayran kaldım :D
        case "0":
            username = input("Username: ").lower()
            password = input("Password: ")
            case_login = is_login(username, password)
        case _:
            print("Try again.")




            # if new_username not in USERNAME:

            #     
            #     print("Welcome, you can login with new informations now.")




products = [
    ["Laptop", 850],
    ["Smartphone", 499],
    ["Headphones", 79],
    ["Keyboard", 45],
    ["Monitor", 220],
    ["Mouse", 25],
    ["Smartwatch", 150],
    ["Tablet", 310],
    ["External Hard Drive", 95],
    ["Webcam", 60],
    ["Laptop", 850]
]


# print(
#     list(
#         map(
#             lambda x: x[0], [user for user in users]
#         )
#     )
# )