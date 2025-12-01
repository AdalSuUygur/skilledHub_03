
#todo Girilen data sheetten ilkisim.soyisim@outlook.com şeklinde mail_adresses üretilip ekrana yazdırılan uygulama.
#* İpucu1: split() fonksiyonu
#* İpucu2: bir listenin uzunluğu ne olursa olsun son elemanına nasıl ulaşırım
users = ["Burak Yılmaz", "Adal Su Uygur", "Yasemin Uygur Erdem", "Sami Lütfü Esen Berk"]

#region Kendi denemem2
mail_addresses = []
mail_uzantisi = "@outlook.com"

for user in users:
    name_slices = user.split(" ")
    ilkisim = name_slices[0]
    soyisim = name_slices[-1]
    mail_addresses.append(f"{ilkisim}.{soyisim}{mail_uzantisi}")
print(mail_addresses)
#endregion YAPTIM KIZ

#region Kendi denemem1

users_splited = users.split(" ")
mail_adress = []

for user in users:
    user = user.lower()
    name_piece = user.split(" ")
    first_name = name_piece[0]
    last_name = name_piece[1]

#endregion

#region Hocanın çözümü

users = ['Burak Yılmaz', 'Rana Nur Ceylan', 'İpek Yılmaz', 'kerim Abdurrahman Burak Yılmaz']
mail_addresses = []
domain_name = "@outlook.com"
for user in users:
    user_names = user.lower().split(" ")
    mail_address = (f"{user_names[0]}.{user_names[-1]}{domain_name}")
    mail_addresses.append(mail_address)
print(mail_addresses)
#endregion

#todo Girilen sampledaki sesli harfleri, sessiz harfleri, typoları ayrı listelere ekleyen uygulama. İlgili listelerde eleman tekrarı olmamalı. Space ignore.
sample = "buRa1k _Ayi?Lm2aZu"
sesli_harfler = []
sessiz_harfler = []
typo_char = []
space_char = []

#region kendi çözümüm

for char in sample.lower():
    if char.isalpha():
        if char in "aeıioöuü":
            if char not in sesli_harfler:
                sesli_harfler.append(char)
        else:
            if char not in sessiz_harfler:
                sessiz_harfler.append(char)
    else:
        if char == " ":
            continue #ignore attık
        elif char not in typo_char:
            typo_char.append(char)

print(f"{sessiz_harfler}\n{sesli_harfler}\n{typo_char}")
#endregion YAPTIKKKKKK

#region Hocanın çözümü

word = input("Type something: ")

for ch in word.lower():
    if ch.isalpha(): #karakter alfabetik mi diye bakıyoruz.
        if ch not in sesli_harfler and ch not in sessiz_harfler:
            if ch in "aeıioöuü":
                sesli_harfler.append(ch)
            else:
                sessiz_harfler.append(ch)
    else:
        if ch == " ":
            continue
        typo_char.append(ch)

print(sesli_harfler)
print(sessiz_harfler)
print(typo_char)
#endregion

#todo 10ar tane rastgele sayı üretilip 2 listeye eklenecek. 3. listeye aktarılacak. appen kullanılması yasak, index mantığıyla çalışılacak.
lst_1 = []
lst_2 = []
lst_3 = []
from random import randint

#region kendi çözümüm
for i in range(10):
    sayi_1 = randint(a=0,b=100)
    lst_1.insert(i, sayi_1)
    sayi_2 = randint(a=0,b=100)
    lst_2.insert(i, sayi_2)
    lst_3.insert(i, lst_1[i] + lst_2[i])
print(lst_1)
print(lst_2)
print(lst_3)
#endregion

#region hocanın çözümü
for i in range(10):
#    print(randint(a=0,b=100)) #1. adım, ürettik evet 10 tane
    lst_1.insert(i, randint(a=0,b=100)) #2. adım ooh hemen üretilen kodla lst_1'e ekleyek
    lst_2.insert(i, randint(a=0, b=100)) #4. adım, bak bunu da ürettik hatta test edelim yine.

    lst_3.insert(i, lst_1[i]+lst_2[i]) #6. adım, oh misler gibi çalıştı bak, bir deyazdıralım da görelim
#print(lst_1) #3. test adımı, ee düzgün çalışıyor demekki o zaman lst_2'ye de aynı şekilde ekleyek
#print(lst_2) #5. adım, çözdük, o zaman devamke
print(f"{lst_1}\n{lst_2}\n{lst_3}")
#endregion

#todo Login bilgileri eşleşirse, ürün search ve fiyat output.
#todo Yanlış loginde yeni kayıt. username'ler unique

users = [
    ["beast", "123"],
    ["bear", "456"],
    ["keko", "789"]
]

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

#region kendi çözümüm

#endregion

#region hocanın çözümü
while True:
    first_process = input("Sign in için 1, Sign up için 2: ")
    match first_process:

        case 1:
            kullanici_adi = input("Username: ")
            sifre = input("Password: ")
            #burası login işlemi
            is_success = False #login başarılı mı değil mi kontrolümüz
            for user in users:
                if user[0] == kullanici_adi and user[1] == sifre:
                    is_success = True
                    break
            if is_success: #ayrı bir döngüde almamızın sebebi 3 kere aynı yazıyı bastırmamak
                print(f"Giriş başarılı, hoşgeldin {kullanici_adi}")
                #buraya tüm yapılacak işlemler gelecek, bunu dışarda yazıp içeri alabiliriz.

                while True:
                    second_process = input("İşlem adı giriniz: ")

                    match second_process:
                        case "toplam fiyat":
                            for product in products:
                                #1. indexlerde fiyatlar var
                                total += product[1]
                            print(f"Toplam fiyat: {total}")

                        case "laptop toplam fiyat":
                            for product in products:
                                if product[0] == "Laptop":
                                    total += product[1]
                                print(f"Toplam laptop fiyatı: {total}")

                        case "ürün ara":
                            urun_adi = input("Ürün adını giriniz: ")
                            for product in products:
                                if urun_adi == product[0]:
                                    print(f"Ürünün fiyatı: {product[0]}")
                                    break #birden fazla ürün olabilir.
                            else:
                                print("Böyle bir ürün yoktur.")

                        case "fiyat aralığına göre ara":
                            alt_sinir = int(input("Alt limit fiyatı: "))
                            ust_limit = int(input("Üst limit fiyatı: "))
                            for product in products:
                                if alt_sinir <= product[1] <= ust_limit:
                                    print(f"Ürününüz: {product[0]} fiyatı: {product[1]}")

                        case "çıkış":
                            print("Uygulama kapatılıyor.")
                            break

                        case _:
                            print("Lütfen işlem türü girdinizi kontrol ediniz.")

            else:
                print("Yanlış giriş bilgileri.")

        case 2:
            #sign in
            kullanici_adi = input("Username: ")
            sifre = input("Password: ")
            #sign up
            is_exists = False #üyeliği yokmuş ve üye olabilir gibi düşünüyoruz.
            for user in users:
                if user[0] == kullanici_adi: #0.indexinde usernameler var
                    is_exists = True #username var mı hali hazırda kontrol ediyoruz 
                    break
            if is_exists:
                print("Kullanıcı adı zaten var")
            else:
                new_user = [kullanici_adi, sifre]
                users.append(new_user)
                print("Üyelik işleminiz tamamlandı.")
            print(users) #test

        case _:
            print("Lütfen girdinizi kontrol ediniz.")

#endregion