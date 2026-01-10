
#! OOP başlangıcı

class Araba:
    door_number = 0
    engine_size = 5.6
    torque = 500
    lenght = 3.1
    width = 1.2
    color = 'black'
    brand = 'Dodge'
    model = 'TRX 1500'

a1 = Araba()
a1.torque = 1000
print(f'Brand: {a1.brand}\nModel: {a1.model}\Torque: {a1.torque}')

class Boxer:
    alias = ''
    height = 0.0
    weight = 0
    full_name = ''
    win = 0
    lost = 0

boxer1 = Boxer()
boxer1.alias = 'iron'
boxer1.height = 1.80
boxer1.weight = 100
boxer1.win = 66
boxer1.lost = 4
print(boxer1.__dict__)


class Student:
    #* class attribute
    taken_courses = ['History I', 'Algorithm']

    def __init__(self, full_name: str, student_id: str):
        #? object attribute
        self.tam_ad = full_name
        self.ogrenci_id = student_id
    
s1 = Student(full_name='burak yılmaz', student_id='123456789')
print(
    f'Student Name: {s1.tam_ad}\n'
    f'Student Id: {s1.ogrenci_id}\n'
    f'Taken Courses: {s1.taken_courses}'
)

print(dir(Student))
#* ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'taken_courses']
print(dir(s1))
#* ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ogrenci_id', 'taken_courses', 'tam_ad']

boxers = list()
print(dir(boxers))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# __init__()
# kalıtım (single ve multiple inheritance)
# method overriding
# encapsulation
# çok biçimlilik
# abstraction (soyutlama)