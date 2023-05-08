# numbers = [1, 2, 5, 6, 3, 9]

# iterator = iter(numbers)

# while True:
#     try:
#         elements = next(iterator)
#         if elements % 2 == 0:
#             print(elements)
#     except StopIteration:
#         break

# dictionary = {'o': 2, 'k': 5, 'e': 1, 't': 10}
# iterator = iter(dictionary.items())

# while True:
#     try:
#         key, value = next(iterator)
#         if value > 4:
#             print(value)
#     except StopIteration:
#         break

# text = 'You are beatiful same'
# words_lenght = (len(word) for word in text.split())

# for lengh in words_lenght:
#     print(lengh)

def is_primary(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def pirminiai_skaiciai(n):
    for number in range(2, n + 1):
        if number in range(2, n + 1):
            if is_primary(number):
                yield number

generator = pirminiai_skaiciai(20)

for number in generator:
    print(number)
