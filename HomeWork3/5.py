
def sum():
   result = 0
   power = True

   while power:
       user_numbers = input('Введите числа через пробел , если хотите выйти введите "G" - ').split()

       for i in user_numbers:
           if i.upper() == 'G' :
               power = False
               break
           else:
               result += int(i)
       print(result)






sum()
