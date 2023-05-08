from functools import wraps

# class Student():
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
    
#     @property
#     def full_name(self):
#         return f'{self.name} {self.surname}'

#     @staticmethod
#     def is_adult(age):
#         if age > 17:
#             return True
#         else:
#             return False
    
#     @classmethod
#     def create_student(cls, name: str, surname: str, age: int):
#         return cls(name, surname, age)
    
# student1 = Student.create_student('Mark', 'Luf', 15)
# student2 = Student.create_student('Paul', 'Haris', 20)

# print(student1.full_name)
# print(Student.is_adult(student1.age))
# print(student2.full_name)
# print(Student.is_adult(student2.age))

def upper_letters(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) == str:
                arg = arg.upper()
        for kwarg in kwargs:
            if type(kwarg) == str:
                kwargs[kwarg] = kwargs[kwarg].upper()
        result = function(*args, **kwargs)
        if type(result) == str:
            result = result.upper()
        return result
    return wrapper

@upper_letters
def make_lower(string='Hey You'):
    print(f'MAking {string} lowercase')
    return string.lower()

print(make_lower())
print(make_lower('Works'))


