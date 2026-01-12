
#12 01 2026
# class Circle:
#     pi = 3.14

#     def __init__(self, r: int): #dışarıdan bir r değeri gelcek, self yaratılacak objeyi 
#         """buraya da dökümantasyon yapılabilir

#         Args:
#             r (int): _description_
#         """
#         self.radius = r

#     #circle sınıfına 2 tane daha kabiliyet verelim: 

#     def calculate_area(self):
#         return self.pi * self.radius **2
    
#     def calculate_perimeter(self):
#         return 2 * self.pi * self.radius
    
# #self yaratılan objeyi temsil eder

# #obje yaratmak için sınıflar var
# # burada amaacımız circle objesi yaratmaya çalışıyoruz ve bu sınıfı yazmak zorundayız
# # bunun için class attributeü ile yazıyoruz
# # obje yaratıyoruz şimdi:

# c1 = Circle(r = 1.02) #instance alıyoruz yani obje yaraıyoruz ve bu bizden bir yarıçap bekliyor.
# #bunu runtime'da yapacak.

# print(
#     c1.calculate_area()
# ) #bunlara nokta notasyonu ile eriştik.


#todo örnek:
# department diye bir sınıf yaratılır. 

class Department:

    #Bunlar class attributes üretir
    department_name = ""
    employee_count = 0
    
    def __init__(self, name: str, age: int):
        self.adi = name #türkçe obje attribute'u, ingilizce dışardan gelen attribute.
        #yani bu sınıftan örneklem aldığımda bunlar yaratılacak (runtime olarak)
        self.yasi = age
        # self.employee_count += 1 #burda self ile çağırdığımızda hep her seferinde 0dan başlatıldığı için  çıktı olarak 1 1 1  olarak verdi
        #self objeyi temsil eder dedik
        # her seferinde yeni bir obje yaratıyor ve içini dolduruyor.
        #yeni alan yarayıro çünkü
        #ama::::::
        #departmentınb employee count'ını çağırdığımıuzda:
        Department.employee_count += 1
        #bu da sınıfın ve objennin attributeleri arasındaki farkı öğretti


    def show_info(self):
        print(
            f"Name: {self.adi}\n"
            f"Age: {self.yasi}\n"
            f"Department Name: {self.department_name}"
        )

    #her instance alındığında (obje çağrıldığında/yaratıldığında) employee sayısını bir artırıtcaz.

    def show_employee_count(self):
        print(f"Total emplotee: {self.employee_count}")

d1 = Department("Adal", 29)
d1.department_name = "YZTA"
d1.show_info()
d1.show_employee_count()


d2 = Department("Yasemin", 34)
d2.department_name = "Teacher"
d2.show_info()
d2.show_employee_count()

d3 = Department("Habiba", 36)
d3.department_name = "Teacher"
d3.show_info()
d3.show_employee_count()

#ram ile alakalı okuma yap
#heap referans hakkında okuma
#garbage collector hakkında okuma yap
#soyutlama konusu bittiğinde tüm bunları kapsamlı konuşacak seviyeye gelicez
#stack nedir
#fonksiyon tanımlandığında ne oluyor
#x değişkeni tanımladığımda ne oluyor
#bu değişken int ise farkı ne, str ise farkı ne
#soyutlama konusu işlendiğinde tüm bu kapsamlı konu ele alınacak olur
# AI tarafında çk büyük kapsamlı bir uygulama yapılmayacaksa çok umursanmıyor ancak kapsamlı örneklerde yine OOP kullanılacak.
# somut örnek olarak: tedarikçiden gelen dökümanı ocr ile kouma yapıcaz, promp template e opturtup LLM'e göndericez ve o da bize veirleri abstract edip json olarak göndericek
#bu projede OOP yoğun kullanılır nedne? çünkü 50 farklı tedarikçi için hint hazırlanması lazım, AI'ya yol gösterici yol/template hazırlanması lazım
#ve bu templatein de türetilmesi lazım
#projeler büyüdükçe oop'tan kaçılamaz
#nesnelerin lifetime'larını yötetmek
#yarattığımız objelerin lifetime'larını yönetmek de bizim concernlerimiz arasındadır!!!!!!!!
# OOP derin bir konu
# 

#todo bi tane software developer sınıfı yaratalım
# bu sınıfın first_name, last_name object attibuteleri olsun

#knowledge_languages adlı bir liste class attribute'u olsun

#challenge şu, bildiği dilleri bu listeye yazıcaz.

#add_new_language() adlı bir fonksiyon olacak.
#sample input --- "python, c#, go" veya "python" olarak gelebilir. Buna göre parçalayıp her biri bir item olarak listeye eklenecek.

#show_info() 

class SoftwareDeveloper():
    knowledge_languages = [] #class attribute olarak yarattık.
    
    def __init__(self, first_name: str, last_name: str): #bunları obje attribute'u olarak.
        self.first_name = first_name
        self.last_name = last_name

    def add_new_language(self, input_language: str):
        language_lst = input_language.split(',') #language bize string olarak geliyor ancak bunu bölmemiz gerek.

        for item in language_lst:
            if item not in self.knowledge_languages:
                self.knowledge_languages.append(item)

        return "Language has been added."

    def show_info(self):
        print(
            f"Full Name: {self.first_name} {self.last_name}\n"
            f"Known Languages: {self.knowledge_languages}" #burda neden bu şekilde eriştik? çünkü herkesin bildiği dil kendisine
        )

s1 = SoftwareDeveloper("Adal", "Uygur")
print(s1.add_new_language("python, c#, c++, java, vb.net"))
s1.show_info()
# biz bir sınıftan nesne ürettiğimiz zaman ------ Bu örnekleme uygulama bir referans verir, referans heapte yani RAM'de tutulur
# ama first name, last name, knowledge languages gibi somut değerler stackte (yığında) tutulur. Last in, first out gibi düşün.
# instance alındığında init tetiklenir. Dışarıdan gelen değerleri alır ve yarattığı objeye 2 alanı açar ve içini doldurur.

#fonksiyon nerde?
# fonksiyondaki parametreler nerde tutulur?
# ramde ama neresinde?
# listeler nerde tutulur?
# parametreli/parametresiz fonksiyon?
# instance'lar, neyi nerde tutulur?
#bunları okuduktan sonra garbage collector bak 3 sektör var onlar neler bunlara bak ve bunlarla alakalı okumaları yap.

#nesnelerin yaşam döngülerine bak, neymiş ne değilmiş, aşırı detayına girmeden bak

#class attributes vs object attributesleri neye göre seçebiliriz? Gemini ile tartış.
