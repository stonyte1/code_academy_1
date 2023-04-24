import random
import calendar

# def atsitiktinai(a, b):
#     numbers = []
#     for i in range(0, 10):
#         number = random.randint(a, b)
#         numbers.append(number)
#     numbers = sorted(numbers)
#     return numbers
# kauliukas = atsitiktinai(1, 100)
# print(kauliukas)
import random 

def kauliukas():
    metimai = []
    for i in range(0, 3):
        metimas = random.randint(1, 6)
        metimai.append(metimas)
    if 5 in metimai:
        print('Pralaimėjai')
    else:
        print('Laimėjai')

kauliukas()

def calendor_dates(year, month):
    print(calendar.month(year, month))
    month_days = calendar.monthrange(year, month)[1]
    weekdays = 0
    for day in range(1, month_days + 1): 
        weekday = calendar.weekday(year, month, day)
        if weekday == 5 or weekday == 6:
            weekdays += 1
    print(f'Weekdays in this month: {weekdays}')

year = int(input('Write a year: '))
month = int(input('Write a month: '))
calendor_dates(year, month)

print('Sveiki')
print('Hey')