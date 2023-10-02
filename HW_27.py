# 1․ Գրել Triangle class, որը․
#    - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
#      եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
#    - կունենա մեթոդ, որը կվերադարձնի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն)։

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         if  not (a + b > c and a + c > b and b + c > a):
#             raise Exception ('No such triangle exists')
        
#     def sides(self):
#         return (f'a = {self.a}, b = {self.b}, c = {self.c}')
    
#     def perimeter(self):
#         self.P = self.a + self.b + self.c
#         return (f'perimeter = {self.P}')
    
#     def surface(self):
#         self.p = self.P / 2
#         self.S = (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5
#         return (f'surface = {self.S}')

#     def regularity(self):
#         if self.a == self.b == self.c:
#             return 'This is an equilateral triangle'
#         elif self.a == self.b or self.a == self.c or self.b == self.c:
#             return 'This is an isosceles triangle'
#         elif self.a ** 2 + self.b ** 2 == self.c ** 2 or \
#             self.a ** 2 + self.c ** 2 == self.b ** 2 or \
#             self.c ** 2 + self.b ** 2 == self.a ** 2:
#             return 'This is a right triangle'
#         else: 
#             return 'This is an irregular triangle'

# triangle1 = Triangle(3, 3, 4)
# print(triangle1.sides())
# print(triangle1.perimeter())
# print(triangle1.surface())
# print(triangle1.regularity())


