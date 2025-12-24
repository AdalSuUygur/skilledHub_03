
#todo Ödev (22 Aralık Ödevi-2):

#* 1 sign in ve sign up
#* sign up işleminde kullanıcının girdiği password valid mi, user_name unique mi? e_mail valid mi?
#* bu kurallardan geçerse üyelik işlemi tamamlanacak
#* sign inta da yine pass word doğru mu bu sefer, e-mail ve password doğruysa giriş yap
#* veri yapısı: 
#* aşağıda sample data structure

users = {
    "xyz.xyz@skilledhub.com": "şifresineyse artık",

    }



#todo Ödev (22 Aralık Ödevi-1): Rakamlardan oluşan bir liste içerisinde bulunan rakamların geçme sıklığını bulan fonksiyonları main() fonksiyonu ile execute eden uygulama
#* Çıktısı aşağıdaki formatta olmalı:

{
    1: 10, #1den 10 tane üretti
    2: 30, #2den 30 tane üretti
    #... böyle tüm rakamları saydıran
}

def main():

    from random import randint

    def random_figure_generator(count: int = 100) -> list:
        """Verilen sayı kadar rastgele rakam üreten fonksiyon
        :param count: Üretilecek sayı miktarı
        :type count: int
        :return: Üretilen sayıların geri dönüşü
        :rtype: list
        """
        return [randint(a= 0, b=9) for _ in range(count)]

    def number_counter(number_list: list = []) -> dict:
        """Verilen listedeki sayıları sayan fonksiyon
        
        :param number_list: Integer sayılardan oluşan bir liste.
        :type number_list: list
        :return: Keylerin sayıları ve valueların kaç kere döndürdüğünü veren blok.
        :rtype: dict
        """
    # Path III: Pythonic yol?
        counter = {}
        for n in number_list: counter[n] = counter.get(n, 0) + 1
        return counter
    # Path II: Bence daha amatörce yol:
    # for number in number_list:
    #     if number in counter:
    #         counter[number] += 1
    #     else:
    #         counter[number] = 1
    # pprint(f"In list {number_list} ve have {counter}")
    # Path I:
    # (counter[number] += 1 if number in counter else counter[number] = 1 for number in number_list)
    # bu kodum çalışmyıor çünkü generator bir işlem yapmıyor bu da syntax hatası veriyor. Ayrıca dict comprehensiona da uygun değil
    # yine işlem sonucunda ekleme yapmak yerine sözlüğe ekleme yaptığım için list comprehension falan da yapamıyorum.

    def print_dict(input_dict: dict = None):
        if input_dict is None:
            input_dict = {}
        print("{") 
        for key in sorted(input_dict.keys()): #Tüm keyleri çekiyoruz, ve sıralı şekilde yazdırmak istiyoruz.
            value = input_dict[key]
            print(f"  {key}: {value}") # Her satırın başına boşluk (indent) ekleyerek daha düzenli yapıyoruz
        print("}")

    print_dict(number_counter(random_figure_generator(100)))

#pprint ile çıktıyı güzelleştirebilirdik.
#Counter ile saydırabilirdik.
#Muhtemelen random sayı üreten de bir fonksiyon vardır ama biz kendimiz yazdık hepsini.
main()
