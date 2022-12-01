# 5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с
# тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

integers_list = [46, 17, 11, 9, 2]
print(f'Текущий рейтинг: {integers_list}')
print('Введите число: ')
user_int = int(input())
for el in range(len(integers_list)):
    if integers_list[el] == user_int:
        integers_list.insert(el + 1, user_int)
        break
    elif integers_list[0] < user_int:
        integers_list.insert(0, user_int)
    elif integers_list[-1] > user_int:
        integers_list.append(user_int)
    elif integers_list[el] > user_int and integers_list[el + 1] < user_int:
        integers_list.insert(el + 1, user_int)
print(f"Новый рейтинг - {integers_list}")

