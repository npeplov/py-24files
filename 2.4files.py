cook_book = {}
temp_book = []
dish = ''
ingredients_list = []


def ingredients_lines_to_dict():
    ingredients_dict = {}
    # берем список ингредиентов
    ingredients = line
    # получаем строку ingredients:
    # 'Яйцо | 2 | шт'
    # преобразуем в список:
    ingredients = ingredients.split('|')
    # получаем список ingredients = ['Яйцо ', ' 2 ', ' шт']
    # преобразуем в словарь ingredients_dict:
    # 0-й элемент это значение ключа ingredient_name и тд
    # вырезаем пробелы из элементов .strip():
    ingredients_dict = {"ingredient_name": ingredients[0].strip(), "quantity": ingredients[1].strip(),
                        "measure": ingredients[2].strip()}

    # добавляем в ingredients_list append значения из ingredients_dict
    ingredients_list.append(ingredients_dict)
    # получили список словарей
    # [{'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'},..]


with open('recipes.txt', 'r', 1, 'utf-8') as fi:
    for line in fi:
        temp_book.append(line.strip())

for i, line in enumerate(temp_book):
    # если 0 элемент или i-1 элемент == ''
    # берем значение записываем в переменную название блюда
    if i == 0 or temp_book[i-1] == '':
        dish = temp_book[i]
    # если line содержит '|'
    elif '|' in line:
        ingredients_lines_to_dict()

    # как встретили '' в строке или это последняя строка файла - записываем в словарь:
    if (line == '') or (i == len(temp_book)-1):
        # в ключ cook_book['Омлет']
        # записываем значение = список словарей ingredients_list
        cook_book[dish] = ingredients_list
        # и обнуляем ingredients_list
        ingredients_list = []

# 2.4.2 Функция, которая на вход принимает список блюд из cook_book
# и количество персон для кого мы будем готовить


def get_shop_list_by_dishes(dishes, person_count):
    cook_calc = {}
    # Цикл по элементам списка dishes:
    for dish_name in dishes:
        # найти блюдо dish_name (Омлет) в словаре cook_book:
        ingredient_list = cook_book[dish_name]
        # получаем список
        # [{'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'},..]
        # цикл по элементам списка:
        for ingredient in ingredient_list:
            # получаем словари:
            # {'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'},..
            # 1 умножить ingredient[quantity] на person_count
            measure = ingredient['measure']
            ingredient_name = ingredient['ingredient_name']
            quantity = int(ingredient["quantity"]) * person_count
            # 2 записать в новый словарь cook_calc
            cook_calc[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return cook_calc


res = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
for key, val in res.items():
    print(key, val)

for item in cook_book.items():
    print(item)
