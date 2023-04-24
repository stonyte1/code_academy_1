from datetime import datetime
import calendar


# now_date = datetime.now()
# format_string = '%M:%S'

# date_string = now_date.strftime(format_string)
# print(now_date)

# def age(birthday):
#     now_date = datetime.now()
#     format_string = '%Y-%m-%d'
#     birthday_string = datetime.strptime(birthday, format_string)
#     birthday = birthday_string.replace(year=now_date.year)
    
#     if birthday < now_date:
#         birthday = birthday.replace(year=now_date.year + 1)
    
#     until_birthday = birthday_string - now_date
#     print(f'Iki gimtadienio liko {until_birthday.days} dienų.')
    


# birthday = input('Write your birthday: ')
# age(birthday)

# date = str(input('Wriet a date: '))
# format_string = '%Y-%m-%d %M:%S'
# date = datetime.strptime(date, format_string)
# new_date = date - timedelta(hours=48)
# new_date = datetime.strftime(new_date, format_string)
# print(new_date)


# def difference(timestamp1, timestamp2):
#     date_object1 = datetime.fromtimestamp(timestamp1)
#     date_object2 = datetime.fromtimestamp(timestamp2)
#     answer = abs(timestamp1 - timestamp2)
#     print(answer) 

# timestamp1 = 1671395400
# timestamp2 = 1674000000
# difference(timestamp1, timestamp2)

def what_day(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    days = ['Monday', 'Tuesday', 'Wensday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(dir(date.weekday()))
    return days[date.weekday()]

print(what_day('2023-05-19'))

