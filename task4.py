# 4) Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
print('Введите строку: ')
user_string = input().split()
print(user_string)
count = 1
for el in user_string:
    print(count, el[:10])
    count += 1


