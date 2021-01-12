def questionnaire(**kwargs):
    for data in kwargs.values():
        print(data, end=' ')


questionnaire(name='Tom', surname='Petrov', Date_of_Birth=1995, city='Moscow', email = '1235@mail.ru', telephone = 1234578899)


