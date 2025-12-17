
#! Variables (Değişkenler)
#* Programlamada değişken (variable), verileri geçici olarak saklamak için kullanılan, isimlendirilmiş bir bellek alanıdır.
#* Değişkenin adı, programda runtime'da çalıştırılır.
#* Python özelinde: Değişkenler içerisine atılan değerin tipine bürünürler, önceden tanımlama gerektirmez.

#? SYNTAX
x = 10 #integer
y = 3.14 #float
is_active = True #boolean
isim = "Su" #string

#todo Matematiksel işlemler
number_1 = 2 #Dümmmmdüz tanımladık
number_2 = input("Type a number: ") #Kullanıcıdan isteyerek tanımladık ama baktık ki input metodu ile bize string geliyor
number_3 = int(input("Type a number: ")) #Bu sebeple burda int metodu içine alarak gelen ifadeyi integer'a çevirdik.

print(number_1 + number_3) #Bu şekilde iki değerin toplamını yazdırabiliriz ancak
addition = number_1 + number_3 #Best practice olarak (DRY Prensibine de uyması açısından)
print(addition) #bu şekilde yazdırılması daha sağlıklı

substraction = number_1 - number_3
#Neden number_2 değişkenini almıyoruz? Çünkü o string bir ifade, ve integer + string ifadesi hata verir program patlar.
print(substraction)

#region Examples

#todo Kullanıcıdan kenar bilgisi alınarak kare alan&çevre hesabı
edge = float(input("Edge: "))
square_area = edge * edge
square_premiter = 4* edge

print(f'Square premiter: {square_premiter} - Square area: {square_area}') #f string ile değişkenleri de burada yazdırdık.
#f string best practice olarak oldukça işimize yarar, çünkü dinamik olarak gerekli olan ifadeyi çağırır.

#todo Kullanıcıdan kısa ve uzun kenar bilgisi alınarak dikdörtgenin alan&çevre hesabı
short_edge = float(input("Edge 1: "))
long_edge = float(input("Edge 2: "))
rectangle_area = short_edge * long_edge
rectangle_premiter = 2 * (short_edge + long_edge) #kodlamada matematiksel işlem önceliği aynen geçerli olduğu için paranteze aldık.
print(f'Rectangle premiter: {rectangle_premiter} - Rectangle area: {rectangle_area}')

#todo Kullanıcıdan taban ve yükseklik bilgisi alınarak üçgenin alan&çevre hesabı
taban = int(input("Üçgenin tabanı: "))
h = int(input("Üçgenin yüksekliği: "))
ucgen_alani = h * taban / 2
print(f'Üçgenin alanı: {ucgen_alani}')

#todo Kullanıcıdan yarıçap alınarak dairenin alan&çevre hesabı
r = float(input("Dairenin yarıçapı: "))
pi = 3.1415926535
alan = pi * (r * r)
cevre = 2 * pi * r
print(f"Dairenin alanı {alan:.2f} birim ve çevresi {cevre:.2f} birimdir.") #:.2f ifadesi ondalıktan sonraki 2 basamağı göster anlamına geliyor.

#todo Kullanıcıdan tabanlar ve yükseklik bilgisi alınarak yamuğun alan hesabı
alt_taban = int(input("Yamuk alt kenarı: "))
ust_taban = int(input("Yamuk üst kenar: "))
h = int(input("Yamuk yükseklik: "))
print(f"Yamuğun alanı {(alt_taban + ust_taban) * h / 2:.2f} kadardır.")

#todo Ürünün adı ve fiyatını kullanıcıdan alıp fstring ile yazdırılması
urun_adi = input("Ürünün adı: ")
fiyat = input("Ürünün fiyatı: ")
print(f"Ürünün adı {urun_adi}'dır ve fiyatı {fiyat}'tır.")

#todo Kenarını kullanıcının verdiği karenin alanını f-string içerisinde hesaplayıp yazdırdık.
#burda f-string içerisindeki {} içerisinde işlem yapılabildiğini öğrendik.
kenar = int(input("Karenin kenarı = "))
print(f"Karenin alanı = {kenar * kenar}")

#endregion

#! Built-in Functions (Yerleşik Fonksiyonlar)
#* Python programlama dilinin en temel ve en sık kullanılan işlemler için doğrudan dilin içine gömülmüş olarak gelen fonksiyonlardır.
#* Bu fonksiyonları kullanmak için herhangi bir kütüphane veya modül indirmenize gerek yoktur. Python'ı kurduğunuz anda kullanıma hazırdırlar.

#? range() fonksiyonu - built in fonksiyon.
for i in range(19):
    print(i) #tek sayı verdik, başlangıç değeri 0, artış miktarı 1

for i in range(3,6):
    print(i) #2 değer verirsek ilk değer başlangıç, ikinci değer bitiş, artış miktarı 1

for i in range(5,65,3):
    print(i) #başlangıç, bitiş, artış miktarı olarak sıralandı.

