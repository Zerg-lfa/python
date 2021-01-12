def my_func(a, b, c):
   if a < b and a < c:
       print(b + c)
   elif b < a and b < c:
       print(a + c)
   else:
       print(a + b)



my_func(int(input('Число - ')), int(input('Число - ')), int(input('Число - ')))


#Не покидает чувство , что есть более простое и локоничное решение.